# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
import functools
import os
from typing import TYPE_CHECKING

from .._internal.managed_identity_base import AsyncManagedIdentityBase
from .._internal.managed_identity_client import AsyncManagedIdentityClient
from ..._constants import EnvironmentVariables
from ..._credentials.cloud_shell import _get_request

if TYPE_CHECKING:
    from typing import Any, Optional


class CloudShellCredential(AsyncManagedIdentityBase):
    def get_client(self, **kwargs: "Any") -> "Optional[AsyncManagedIdentityClient]":
        url = os.environ.get(EnvironmentVariables.MSI_ENDPOINT)
        if url:
            return AsyncManagedIdentityClient(
                request_factory=functools.partial(_get_request, url), base_headers={"Metadata": "true"}, **kwargs
            )
        return None

    def get_unavailable_message(self) -> str:
        return "Cloud Shell managed identity configuration not found in environment"
