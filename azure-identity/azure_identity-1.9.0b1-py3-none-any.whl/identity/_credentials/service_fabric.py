# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
import functools
import os
from typing import TYPE_CHECKING

from azure.core.pipeline.transport import HttpRequest

from .._constants import EnvironmentVariables
from .._internal.managed_identity_base import ManagedIdentityBase
from .._internal.managed_identity_client import ManagedIdentityClient

if TYPE_CHECKING:
    from typing import Any, Optional


class ServiceFabricCredential(ManagedIdentityBase):
    def get_client(self, **kwargs):
        # type: (**Any) -> Optional[ManagedIdentityClient]
        client_args = _get_client_args(**kwargs)
        if client_args:
            return ManagedIdentityClient(**client_args)
        return None

    def get_unavailable_message(self):
        # type: () -> str
        return "Service Fabric managed identity configuration not found in environment"


def _get_client_args(**kwargs):
    # type: (**Any) -> Optional[dict]
    url = os.environ.get(EnvironmentVariables.IDENTITY_ENDPOINT)
    secret = os.environ.get(EnvironmentVariables.IDENTITY_HEADER)
    thumbprint = os.environ.get(EnvironmentVariables.IDENTITY_SERVER_THUMBPRINT)
    if not (url and secret and thumbprint):
        # Service Fabric managed identity isn't available in this environment
        return None

    return dict(
        kwargs,
        base_headers={"Secret": secret},
        connection_verify=False,
        request_factory=functools.partial(_get_request, url),
    )


def _get_request(url, scope, identity_config):
    # type: (str, str, dict) -> HttpRequest
    request = HttpRequest("GET", url)
    request.format_parameters(dict({"api-version": "2019-07-01-preview", "resource": scope}, **identity_config))
    return request
