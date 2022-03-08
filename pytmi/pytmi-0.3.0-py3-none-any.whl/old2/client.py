"""Module containing the main client class (TmiClient)."""

import abc
import random
import asyncio
import ssl
from typing import Optional, Type, cast
from contextlib import suppress

from old2.message import TmiMessage, make_privmsg
from old2.stream import TmiBaseStream, TmiStream
from old2.buffer import TmiBuffer


# Twitch IRC server `https://dev.twitch.tv/docs/irc/guide#connecting-to-twitch-irc`
TMI_SERVER = "irc.chat.twitch.tv"
TMI_SERVER_PORT = 6667
TMI_SERVER_SSLPORT = 6697

TMI_PING_MESSAGE = b"PING :tmi.twitch.tv\r\n"
TMI_PONG_MESSAGE = b"PONG :tmi.twitch.tv\r\n"

TMI_CAPS = [
    (
        f"CAP REQ :twitch.tv/{cap}\r\n".encode(),
        f":tmi.twitch.tv CAP * ACK :twitch.tv/{cap}\r\n".encode(),
    )
    for cap in ["membership", "tags", "commands"]
]


# Default client limits
# These are arbitrary values
CLIENT_MAX_RETRY = 8
CLIENT_MAX_BUFFER_SIZE = 128
CLIENT_MESSAGE_INTERVAL = 0.5


class TmiBaseClient(abc.ABC):
    """Base Client for handling IRC-TMI streams and messages."""


class TmiClient(TmiBaseClient):
    """Asynchronous client for handling IRC-TMI streams and messages."""

    def __init__(
        self,
        use_ssl: bool = True,
        use_task: bool = False,
        stream: Type[TmiBaseStream] = TmiStream,
        max_buffer_size: int = CLIENT_MAX_BUFFER_SIZE,
        message_interval: float = CLIENT_MESSAGE_INTERVAL,
    ) -> None:
        self.__stream_type = stream
        self.__buf = TmiBuffer(max_buffer_size)

        self.__use_ssl = use_ssl
        self.__stream = self.__stream_type()

        self.__joined: Optional[str] = None
        self.__logged: bool = False

        self.__use_task: bool = use_task
        self.__task: Optional[asyncio.Task] = None
        self.__interval: float = message_interval  # Seconds

    async def login_oauth(
        self, token: str, nick: str, retry: int = CLIENT_MAX_RETRY
    ) -> None:
        if self.__logged:
            raise AttributeError("Alredy logged in")

        if not token.startswith("oauth:"):
            token = "oauth:" + token

        nick = nick.lower()

        if retry < 0:
            retry = CLIENT_MAX_RETRY

        backoff = 0

        # TODO: Improve connection error handling
        while retry > 0:
            retry -= 1
            try:
                await self.__login(token, nick)
                return
            except Exception as e:
                if not isinstance(e, (AssertionError, ConnectionError)):
                    raise

                # Wait a bit before retrying
                if backoff <= 1:
                    backoff += 1
                else:
                    backoff *= 2
                    await asyncio.sleep(backoff / 1.5)

        raise ConnectionError("Connection failed")

    async def login_anonymous(self, retry: int = CLIENT_MAX_RETRY) -> None:
        token = "random_string"
        nick = "justinfan" + str(random.randint(12345, 67890))
        await self.login_oauth(token, nick, retry=retry)

    async def __login(self, token: str, nick: str) -> None:
        if self.__use_ssl:
            await self.__stream.connect(
                TMI_SERVER, TMI_SERVER_SSLPORT, ssl_ctx=ssl.create_default_context()
            )
        else:
            await self.__stream.connect(TMI_SERVER, TMI_SERVER_PORT)

        pass_command = "PASS " + token + "\r\n"
        await self.__stream.write_buf(pass_command.encode())

        nick_command = "NICK " + nick.lower() + "\r\n"
        await self.__stream.write_buf(nick_command.encode())

        welcome1 = f":tmi.twitch.tv 001 {nick} :Welcome, GLHF!\r\n"
        assert await self.__stream.read_buf() == welcome1.encode()

        welcome2 = f":tmi.twitch.tv 002 {nick} :Your host is tmi.twitch.tv\r\n"
        assert await self.__stream.read_buf() == welcome2.encode()

        welcome3 = f":tmi.twitch.tv 003 {nick} :This server is rather new\r\n"
        assert await self.__stream.read_buf() == welcome3.encode()

        welcome4 = f":tmi.twitch.tv 004 {nick} :-\r\n"
        assert await self.__stream.read_buf() == welcome4.encode()

        welcome5 = f":tmi.twitch.tv 375 {nick} :-\r\n"
        assert await self.__stream.read_buf() == welcome5.encode()

        welcome6 = f":tmi.twitch.tv 372 {nick} :You are in a maze of twisty passages, all alike.\r\n"
        assert await self.__stream.read_buf() == welcome6.encode()

        welcome7 = f":tmi.twitch.tv 376 {nick} :>\r\n"
        assert await self.__stream.read_buf() == welcome7.encode()

        # Capabilities
        for req, ack in TMI_CAPS:
            await self.__stream.write_buf(req)
            assert await self.__stream.read_buf() == ack

        self.__logged = True

        if self.__use_task:
            self.__task = asyncio.get_event_loop().create_task(self.__recv_task())

    async def __recv_message(self) -> bytes:
        line = await self.__stream.read_buf()

        if line == TMI_PING_MESSAGE:
            await self.__stream.write_buf(TMI_PONG_MESSAGE)
            line = await self.__stream.read_buf()

        return line

    async def __recv_task(self) -> None:
        while self.__logged:
            line = await self.__recv_message()
            self.__buf.append(line)
            await asyncio.sleep(self.__interval)

    async def logout(self) -> None:
        if not self.__logged:
            raise AttributeError("Not logged in")

        try:
            if self.__joined is not None:
                await self.part(self.__joined)
        except:
            self.__joined = None # FIXME

        self.__logged = False
        await self.__stream.disconnect()

        if self.__use_task:
            # assert self.__task is not None
            # self.__task.cancel()

            # with suppress(asyncio.CancelledError):
            #    asyncio.get_event_loop().run_until_complete(self.__task)

            self.__task = None

    async def join(self, channel: str) -> None:
        if not self.__logged:
            raise AttributeError("Not logged in")

        if not channel.startswith("#"):
            channel = "#" + channel

        self.__joined = channel

        command = "JOIN " + channel + "\r\n"
        await self.__stream.write_buf(command.encode())

    async def part(self, channel: Optional[str] = None) -> None:
        if not self.__logged:
            raise AttributeError("Not logged in")

        if channel is None:
            channel = self.__joined
            if channel is None:
                raise AttributeError("Unspecified channel")

        channel = cast(str, channel)
        if not channel.startswith("#"):
            channel = "#" + channel

        command = "PART " + channel + "\r\n"
        await self.__stream.write_buf(command.encode())

        self.__joined = None

    async def send_privmsg(self, message: str, channel: Optional[str] = None) -> None:
        if not self.__logged:
            raise AttributeError("Not logged in")

        if channel is None:
            channel = self.__joined
            if channel is None:
                raise AttributeError("Unspecified channel")

        channel = cast(str, channel)
        if not channel.startswith("#"):
            channel = "#" + channel

        await self.__stream.write_buf(make_privmsg(channel, message))

    async def get_raw_message(self) -> bytes:
        if not self.__logged:
            raise AttributeError("Not logged in")

        if self.__use_task:
            while self.__buf.empty():
                await asyncio.sleep(self.__interval)

            return self.__buf.pop()

        return await self.__recv_message()

    async def get_message(self) -> TmiMessage:
        return TmiMessage(await self.get_raw_message())

    @property
    def logged(self) -> bool:
        return self.__logged


__all__ = [
    "TmiBaseClient",
    "TmiClient",
]
