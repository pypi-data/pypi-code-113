# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
import functools
import os
from typing import TYPE_CHECKING

from azure.core.pipeline.policies import AsyncHTTPPolicy

from .._internal.managed_identity_base import AsyncManagedIdentityBase
from .._internal.managed_identity_client import AsyncManagedIdentityClient
from ..._constants import EnvironmentVariables
from ..._credentials.azure_arc import _get_request, _get_secret_key

if TYPE_CHECKING:
    # pylint:disable=unused-import,ungrouped-imports
    from typing import Any, Optional
    from azure.core.pipeline import PipelineRequest, PipelineResponse


class AzureArcCredential(AsyncManagedIdentityBase):
    def get_client(self, **kwargs: "Any") -> "Optional[AsyncManagedIdentityClient]":
        url = os.environ.get(EnvironmentVariables.IDENTITY_ENDPOINT)
        imds = os.environ.get(EnvironmentVariables.IMDS_ENDPOINT)
        if url and imds:
            return AsyncManagedIdentityClient(
                _per_retry_policies=[ArcChallengeAuthPolicy()],
                request_factory=functools.partial(_get_request, url),
                **kwargs
            )
        return None

    def get_unavailable_message(self) -> str:
        return "Azure Arc managed identity configuration not found in environment"


class ArcChallengeAuthPolicy(AsyncHTTPPolicy):
    """Policy for handling Azure Arc's challenge authentication"""

    async def send(self, request: "PipelineRequest") -> "PipelineResponse":
        request.http_request.headers["Metadata"] = "true"
        response = await self.next.send(request)

        if response.http_response.status_code == 401:
            secret_key = _get_secret_key(response)
            request.http_request.headers["Authorization"] = "Basic {}".format(secret_key)
            response = await self.next.send(request)

        return response
