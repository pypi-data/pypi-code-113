from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.bad_request_error import BadRequestError
from ...models.plates_archival_change import PlatesArchivalChange
from ...models.plates_archive import PlatesArchive
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: PlatesArchive,
) -> Dict[str, Any]:
    url = "{}/plates:archive".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()

    json_json_body = json_body.to_dict()

    return {
        "url": url,
        "headers": headers,
        "cookies": client.get_cookies(),
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[PlatesArchivalChange, BadRequestError]]:
    if response.status_code == 200:
        response_200 = PlatesArchivalChange.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = BadRequestError.from_dict(response.json())

        return response_400
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[PlatesArchivalChange, BadRequestError]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: PlatesArchive,
) -> Response[Union[PlatesArchivalChange, BadRequestError]]:
    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    response = httpx.post(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    json_body: PlatesArchive,
) -> Optional[Union[PlatesArchivalChange, BadRequestError]]:
    """ Archive plates and any containers of the plates """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: PlatesArchive,
) -> Response[Union[PlatesArchivalChange, BadRequestError]]:
    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    json_body: PlatesArchive,
) -> Optional[Union[PlatesArchivalChange, BadRequestError]]:
    """ Archive plates and any containers of the plates """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
