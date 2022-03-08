# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from collections import OrderedDict
import functools
import re
from typing import Dict, Optional, Sequence, Tuple, Type, Union
import pkg_resources

from google.api_core.client_options import ClientOptions
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.oauth2 import service_account  # type: ignore

try:
    OptionalRetry = Union[retries.Retry, gapic_v1.method._MethodDefault]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.Retry, object]  # type: ignore

from google.cloud.servicecontrol_v2.types import service_controller
from google.rpc import status_pb2  # type: ignore
from .transports.base import ServiceControllerTransport, DEFAULT_CLIENT_INFO
from .transports.grpc_asyncio import ServiceControllerGrpcAsyncIOTransport
from .client import ServiceControllerClient


class ServiceControllerAsyncClient:
    """`Service Control API
    v2 </service-infrastructure/docs/service-control>`__

    Private Preview. This feature is only available for approved
    services.

    This API provides admission control and telemetry reporting for
    services that are integrated with `Service
    Infrastructure </service-infrastructure>`__.
    """

    _client: ServiceControllerClient

    DEFAULT_ENDPOINT = ServiceControllerClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = ServiceControllerClient.DEFAULT_MTLS_ENDPOINT

    common_billing_account_path = staticmethod(
        ServiceControllerClient.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        ServiceControllerClient.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(ServiceControllerClient.common_folder_path)
    parse_common_folder_path = staticmethod(
        ServiceControllerClient.parse_common_folder_path
    )
    common_organization_path = staticmethod(
        ServiceControllerClient.common_organization_path
    )
    parse_common_organization_path = staticmethod(
        ServiceControllerClient.parse_common_organization_path
    )
    common_project_path = staticmethod(ServiceControllerClient.common_project_path)
    parse_common_project_path = staticmethod(
        ServiceControllerClient.parse_common_project_path
    )
    common_location_path = staticmethod(ServiceControllerClient.common_location_path)
    parse_common_location_path = staticmethod(
        ServiceControllerClient.parse_common_location_path
    )

    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            info.

        Args:
            info (dict): The service account private key info.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            ServiceControllerAsyncClient: The constructed client.
        """
        return ServiceControllerClient.from_service_account_info.__func__(ServiceControllerAsyncClient, info, *args, **kwargs)  # type: ignore

    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            file.

        Args:
            filename (str): The path to the service account private key json
                file.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            ServiceControllerAsyncClient: The constructed client.
        """
        return ServiceControllerClient.from_service_account_file.__func__(ServiceControllerAsyncClient, filename, *args, **kwargs)  # type: ignore

    from_service_account_json = from_service_account_file

    @classmethod
    def get_mtls_endpoint_and_cert_source(
        cls, client_options: Optional[ClientOptions] = None
    ):
        """Return the API endpoint and client cert source for mutual TLS.

        The client cert source is determined in the following order:
        (1) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is not "true", the
        client cert source is None.
        (2) if `client_options.client_cert_source` is provided, use the provided one; if the
        default client cert source exists, use the default one; otherwise the client cert
        source is None.

        The API endpoint is determined in the following order:
        (1) if `client_options.api_endpoint` if provided, use the provided one.
        (2) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is "always", use the
        default mTLS endpoint; if the environment variabel is "never", use the default API
        endpoint; otherwise if client cert source exists, use the default mTLS endpoint, otherwise
        use the default API endpoint.

        More details can be found at https://google.aip.dev/auth/4114.

        Args:
            client_options (google.api_core.client_options.ClientOptions): Custom options for the
                client. Only the `api_endpoint` and `client_cert_source` properties may be used
                in this method.

        Returns:
            Tuple[str, Callable[[], Tuple[bytes, bytes]]]: returns the API endpoint and the
                client cert source to use.

        Raises:
            google.auth.exceptions.MutualTLSChannelError: If any errors happen.
        """
        return ServiceControllerClient.get_mtls_endpoint_and_cert_source(client_options)  # type: ignore

    @property
    def transport(self) -> ServiceControllerTransport:
        """Returns the transport used by the client instance.

        Returns:
            ServiceControllerTransport: The transport used by the client instance.
        """
        return self._client.transport

    get_transport_class = functools.partial(
        type(ServiceControllerClient).get_transport_class, type(ServiceControllerClient)
    )

    def __init__(
        self,
        *,
        credentials: ga_credentials.Credentials = None,
        transport: Union[str, ServiceControllerTransport] = "grpc_asyncio",
        client_options: ClientOptions = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the service controller client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Union[str, ~.ServiceControllerTransport]): The
                transport to use. If set to None, a transport is chosen
                automatically.
            client_options (ClientOptions): Custom options for the client. It
                won't take effect if a ``transport`` instance is provided.
                (1) The ``api_endpoint`` property can be used to override the
                default endpoint provided by the client. GOOGLE_API_USE_MTLS_ENDPOINT
                environment variable can also be used to override the endpoint:
                "always" (always use the default mTLS endpoint), "never" (always
                use the default regular endpoint) and "auto" (auto switch to the
                default mTLS endpoint if client certificate is present, this is
                the default value). However, the ``api_endpoint`` property takes
                precedence if provided.
                (2) If GOOGLE_API_USE_CLIENT_CERTIFICATE environment variable
                is "true", then the ``client_cert_source`` property can be used
                to provide client certificate for mutual TLS transport. If
                not provided, the default SSL client certificate will be used if
                present. If GOOGLE_API_USE_CLIENT_CERTIFICATE is "false" or not
                set, no client certificate will be used.

        Raises:
            google.auth.exceptions.MutualTlsChannelError: If mutual TLS transport
                creation failed for any reason.
        """
        self._client = ServiceControllerClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

    async def check(
        self,
        request: Union[service_controller.CheckRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> service_controller.CheckResponse:
        r"""Private Preview. This feature is only available for approved
        services.

        This method provides admission control for services that are
        integrated with `Service
        Infrastructure </service-infrastructure>`__. It checks whether
        an operation should be allowed based on the service
        configuration and relevant policies. It must be called before
        the operation is executed. For more information, see `Admission
        Control </service-infrastructure/docs/admission-control>`__.

        NOTE: The admission control has an expected policy propagation
        delay of 60s. The caller **must** not depend on the most recent
        policy changes.

        NOTE: The admission control has a hard limit of 1 referenced
        resources per call. If an operation refers to more than 1
        resources, the caller must call the Check method multiple times.

        This method requires the ``servicemanagement.services.check``
        permission on the specified service. For more information, see
        `Service Control API Access
        Control <https://cloud.google.com/service-infrastructure/docs/service-control/access-control>`__.


        .. code-block:: python

            from google.cloud import servicecontrol_v2

            def sample_check():
                # Create a client
                client = servicecontrol_v2.ServiceControllerClient()

                # Initialize request argument(s)
                request = servicecontrol_v2.CheckRequest(
                )

                # Make the request
                response = client.check(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.servicecontrol_v2.types.CheckRequest, dict]):
                The request object. Request message for the Check
                method.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.servicecontrol_v2.types.CheckResponse:
                Response message for the Check
                method.

        """
        # Create or coerce a protobuf request object.
        request = service_controller.CheckRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.check,
            default_retry=retries.Retry(
                initial=1.0,
                maximum=10.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=5.0,
            ),
            default_timeout=5.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    async def report(
        self,
        request: Union[service_controller.ReportRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> service_controller.ReportResponse:
        r"""Private Preview. This feature is only available for approved
        services.

        This method provides telemetry reporting for services that are
        integrated with `Service
        Infrastructure </service-infrastructure>`__. It reports a list
        of operations that have occurred on a service. It must be called
        after the operations have been executed. For more information,
        see `Telemetry
        Reporting </service-infrastructure/docs/telemetry-reporting>`__.

        NOTE: The telemetry reporting has a hard limit of 1000
        operations and 1MB per Report call. It is recommended to have no
        more than 100 operations per call.

        This method requires the ``servicemanagement.services.report``
        permission on the specified service. For more information, see
        `Service Control API Access
        Control <https://cloud.google.com/service-infrastructure/docs/service-control/access-control>`__.


        .. code-block:: python

            from google.cloud import servicecontrol_v2

            def sample_report():
                # Create a client
                client = servicecontrol_v2.ServiceControllerClient()

                # Initialize request argument(s)
                request = servicecontrol_v2.ReportRequest(
                )

                # Make the request
                response = client.report(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.servicecontrol_v2.types.ReportRequest, dict]):
                The request object. Request message for the Report
                method.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.servicecontrol_v2.types.ReportResponse:
                Response message for the Report
                method. If the request contains any
                invalid data, the server returns an RPC
                error.

        """
        # Create or coerce a protobuf request object.
        request = service_controller.ReportRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.report,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.transport.close()


try:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
        gapic_version=pkg_resources.get_distribution(
            "google-cloud-service-control",
        ).version,
    )
except pkg_resources.DistributionNotFound:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo()


__all__ = ("ServiceControllerAsyncClient",)
