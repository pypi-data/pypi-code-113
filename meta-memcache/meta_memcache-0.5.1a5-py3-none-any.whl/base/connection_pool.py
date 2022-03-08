import itertools
import logging
import socket
import time
from contextlib import contextmanager
from queue import Empty, Full, Queue
from collections import deque
from typing import Callable, Deque, Generator, NamedTuple, Optional

from meta_memcache.base.memcache_socket import MemcacheSocket, log
from meta_memcache.errors import MemcacheServerError
from meta_memcache.protocol import ServerVersion
from meta_memcache.settings import DEFAULT_MARK_DOWN_PERIOD_S, DEFAULT_READ_BUFFER_SIZE

_log: logging.Logger = logging.getLogger(__name__)


class PoolCounters(NamedTuple):
    # Available connections in the pool, ready to use
    available: int
    # The # of connections active, currently in use, out of the pool
    active: int
    # Current stablished connections (available + active)
    stablished: int
    # Total # of connections created. If this keeps growing
    # might meen the pool size is too small and we are
    # constantly needing to create new connections:
    total_created: int
    # Total # of connection or socket errors
    total_errors: int


class ConnectionPool:
    def __init__(
        self,
        server: str,
        socket_factory_fn: Callable[[], socket.socket],
        initial_pool_size: int,
        max_pool_size: int,
        mark_down_period_s: float = DEFAULT_MARK_DOWN_PERIOD_S,
        read_buffer_size: int = DEFAULT_READ_BUFFER_SIZE,
        version: ServerVersion = ServerVersion.STABLE,
    ) -> None:
        self.server = server
        self._socket_factory_fn = socket_factory_fn
        self._initial_pool_size: int = min(initial_pool_size, max_pool_size)
        self._max_pool_size = max_pool_size
        self._mark_down_period_s = mark_down_period_s
        self._created_counter: itertools.count[int] = itertools.count(start=1)
        self._created = 0
        self._errors_counter: itertools.count[int] = itertools.count(start=1)
        self._errors = 0
        self._destroyed_counter: itertools.count[int] = itertools.count(start=1)
        self._destroyed = 0
        self._marked_down_until: Optional[float] = None
        # self._pool: Queue[MemcacheSocket] = Queue(self._max_pool_size)
        self._pool: Deque[MemcacheSocket] = deque(maxlen=self._max_pool_size)
        self._read_buffer_size = read_buffer_size
        self._version = version
        for _ in range(self._initial_pool_size):
            try:
                # self._pool.put_nowait(self._create_connection())
                self._pool.append(self._create_connection())
            except MemcacheServerError:
                pass

    def get_counters(self) -> PoolCounters:
        # available = self._pool.qsize()
        available = len(self._pool)
        total_created, total_destroyed = self._created, self._destroyed
        stablished = total_created - total_destroyed
        active = available - stablished

        return PoolCounters(
            available=available,
            active=active,
            stablished=stablished,
            total_created=total_created,
            total_errors=self._errors,
        )

    def _create_connection(self) -> MemcacheSocket:
        if marked_down_until := self._marked_down_until:
            if time.time() < marked_down_until:
                raise MemcacheServerError(
                    self.server, f"Server marked down: {self.server}"
                )
            self._marked_down_until = None

        try:
            conn = self._socket_factory_fn()
            log(
                conn,
                f"*** Connection pool {self} created conn. Current pool is {len(self._pool)} in size.".encode(),
            )
        except Exception as e:
            _log.exception("Error connecting to memcache")
            self._errors = next(self._errors_counter)
            self._marked_down_until = time.time() + self._mark_down_period_s
            raise MemcacheServerError(
                self.server, f"Server marked down: {self.server}"
            ) from e

        self._created = next(self._created_counter)
        return MemcacheSocket(conn, self._read_buffer_size, version=self._version)

    def _discard_connection(self, conn: MemcacheSocket, error: bool = False) -> None:
        try:
            conn.close()
        except Exception:  # noqa: S110
            pass
        if error:
            self._errors = next(self._errors_counter)
        self._destroyed = next(self._destroyed_counter)

    @contextmanager
    def get_connection(self) -> Generator[MemcacheSocket, None, None]:
        try:
            # conn = self._pool.get_nowait()
            conn = self._pool.popleft()
            mode = f"from pool conn: {conn} ({conn._conn})"
        except (Empty, IndexError):
            conn = self._create_connection()
            mode = "CREATED"

        log(conn._conn, f">>> Connection {mode}".encode())
        try:
            yield conn
        except Exception:
            # Errors, assume connection is in bad state
            _log.exception(f"Error during cache conn context (discarding connection)")
            self._discard_connection(conn, error=True)
            log(conn._conn, b"XXX Connection DISCARDED")
            raise
        else:
            try:
                # self._pool.put_nowait(conn)
                self._pool.append(conn)
                log(conn._conn, b"<<< Connection returned to pool")
            except Full:
                self._discard_connection(conn)
                log(conn._conn, b"XXX Connection discarded (POOL FULL)")
