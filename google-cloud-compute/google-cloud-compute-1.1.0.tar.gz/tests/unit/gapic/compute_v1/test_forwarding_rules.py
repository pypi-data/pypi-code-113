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
import os
import mock

import grpc
from grpc.experimental import aio
from collections.abc import Iterable
import json
import math
import pytest
from proto.marshal.rules.dates import DurationRule, TimestampRule

from requests import Response
from requests import Request, PreparedRequest
from requests.sessions import Session

from google.api_core import client_options
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1
from google.api_core import grpc_helpers
from google.api_core import grpc_helpers_async
from google.api_core import path_template
from google.auth import credentials as ga_credentials
from google.auth.exceptions import MutualTLSChannelError
from google.cloud.compute_v1.services.forwarding_rules import ForwardingRulesClient
from google.cloud.compute_v1.services.forwarding_rules import pagers
from google.cloud.compute_v1.services.forwarding_rules import transports
from google.cloud.compute_v1.types import compute
from google.oauth2 import service_account
import google.auth


def client_cert_source_callback():
    return b"cert bytes", b"key bytes"


# If default endpoint is localhost, then default mtls endpoint will be the same.
# This method modifies the default endpoint so the client can produce a different
# mtls endpoint for endpoint testing purposes.
def modify_default_endpoint(client):
    return (
        "foo.googleapis.com"
        if ("localhost" in client.DEFAULT_ENDPOINT)
        else client.DEFAULT_ENDPOINT
    )


def test__get_default_mtls_endpoint():
    api_endpoint = "example.googleapis.com"
    api_mtls_endpoint = "example.mtls.googleapis.com"
    sandbox_endpoint = "example.sandbox.googleapis.com"
    sandbox_mtls_endpoint = "example.mtls.sandbox.googleapis.com"
    non_googleapi = "api.example.com"

    assert ForwardingRulesClient._get_default_mtls_endpoint(None) is None
    assert (
        ForwardingRulesClient._get_default_mtls_endpoint(api_endpoint)
        == api_mtls_endpoint
    )
    assert (
        ForwardingRulesClient._get_default_mtls_endpoint(api_mtls_endpoint)
        == api_mtls_endpoint
    )
    assert (
        ForwardingRulesClient._get_default_mtls_endpoint(sandbox_endpoint)
        == sandbox_mtls_endpoint
    )
    assert (
        ForwardingRulesClient._get_default_mtls_endpoint(sandbox_mtls_endpoint)
        == sandbox_mtls_endpoint
    )
    assert (
        ForwardingRulesClient._get_default_mtls_endpoint(non_googleapi) == non_googleapi
    )


@pytest.mark.parametrize(
    "client_class,transport_name", [(ForwardingRulesClient, "rest"),]
)
def test_forwarding_rules_client_from_service_account_info(
    client_class, transport_name
):
    creds = ga_credentials.AnonymousCredentials()
    with mock.patch.object(
        service_account.Credentials, "from_service_account_info"
    ) as factory:
        factory.return_value = creds
        info = {"valid": True}
        client = client_class.from_service_account_info(info, transport=transport_name)
        assert client.transport._credentials == creds
        assert isinstance(client, client_class)

        assert client.transport._host == (
            "compute.googleapis.com{}".format(":443")
            if transport_name in ["grpc", "grpc_asyncio"]
            else "https://{}".format("compute.googleapis.com")
        )


@pytest.mark.parametrize(
    "transport_class,transport_name",
    [(transports.ForwardingRulesRestTransport, "rest"),],
)
def test_forwarding_rules_client_service_account_always_use_jwt(
    transport_class, transport_name
):
    with mock.patch.object(
        service_account.Credentials, "with_always_use_jwt_access", create=True
    ) as use_jwt:
        creds = service_account.Credentials(None, None, None)
        transport = transport_class(credentials=creds, always_use_jwt_access=True)
        use_jwt.assert_called_once_with(True)

    with mock.patch.object(
        service_account.Credentials, "with_always_use_jwt_access", create=True
    ) as use_jwt:
        creds = service_account.Credentials(None, None, None)
        transport = transport_class(credentials=creds, always_use_jwt_access=False)
        use_jwt.assert_not_called()


@pytest.mark.parametrize(
    "client_class,transport_name", [(ForwardingRulesClient, "rest"),]
)
def test_forwarding_rules_client_from_service_account_file(
    client_class, transport_name
):
    creds = ga_credentials.AnonymousCredentials()
    with mock.patch.object(
        service_account.Credentials, "from_service_account_file"
    ) as factory:
        factory.return_value = creds
        client = client_class.from_service_account_file(
            "dummy/file/path.json", transport=transport_name
        )
        assert client.transport._credentials == creds
        assert isinstance(client, client_class)

        client = client_class.from_service_account_json(
            "dummy/file/path.json", transport=transport_name
        )
        assert client.transport._credentials == creds
        assert isinstance(client, client_class)

        assert client.transport._host == (
            "compute.googleapis.com{}".format(":443")
            if transport_name in ["grpc", "grpc_asyncio"]
            else "https://{}".format("compute.googleapis.com")
        )


def test_forwarding_rules_client_get_transport_class():
    transport = ForwardingRulesClient.get_transport_class()
    available_transports = [
        transports.ForwardingRulesRestTransport,
    ]
    assert transport in available_transports

    transport = ForwardingRulesClient.get_transport_class("rest")
    assert transport == transports.ForwardingRulesRestTransport


@pytest.mark.parametrize(
    "client_class,transport_class,transport_name",
    [(ForwardingRulesClient, transports.ForwardingRulesRestTransport, "rest"),],
)
@mock.patch.object(
    ForwardingRulesClient,
    "DEFAULT_ENDPOINT",
    modify_default_endpoint(ForwardingRulesClient),
)
def test_forwarding_rules_client_client_options(
    client_class, transport_class, transport_name
):
    # Check that if channel is provided we won't create a new one.
    with mock.patch.object(ForwardingRulesClient, "get_transport_class") as gtc:
        transport = transport_class(credentials=ga_credentials.AnonymousCredentials())
        client = client_class(transport=transport)
        gtc.assert_not_called()

    # Check that if channel is provided via str we will create a new one.
    with mock.patch.object(ForwardingRulesClient, "get_transport_class") as gtc:
        client = client_class(transport=transport_name)
        gtc.assert_called()

    # Check the case api_endpoint is provided.
    options = client_options.ClientOptions(api_endpoint="squid.clam.whelk")
    with mock.patch.object(transport_class, "__init__") as patched:
        patched.return_value = None
        client = client_class(transport=transport_name, client_options=options)
        patched.assert_called_once_with(
            credentials=None,
            credentials_file=None,
            host="squid.clam.whelk",
            scopes=None,
            client_cert_source_for_mtls=None,
            quota_project_id=None,
            client_info=transports.base.DEFAULT_CLIENT_INFO,
            always_use_jwt_access=True,
        )

    # Check the case api_endpoint is not provided and GOOGLE_API_USE_MTLS_ENDPOINT is
    # "never".
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "never"}):
        with mock.patch.object(transport_class, "__init__") as patched:
            patched.return_value = None
            client = client_class(transport=transport_name)
            patched.assert_called_once_with(
                credentials=None,
                credentials_file=None,
                host=client.DEFAULT_ENDPOINT,
                scopes=None,
                client_cert_source_for_mtls=None,
                quota_project_id=None,
                client_info=transports.base.DEFAULT_CLIENT_INFO,
                always_use_jwt_access=True,
            )

    # Check the case api_endpoint is not provided and GOOGLE_API_USE_MTLS_ENDPOINT is
    # "always".
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "always"}):
        with mock.patch.object(transport_class, "__init__") as patched:
            patched.return_value = None
            client = client_class(transport=transport_name)
            patched.assert_called_once_with(
                credentials=None,
                credentials_file=None,
                host=client.DEFAULT_MTLS_ENDPOINT,
                scopes=None,
                client_cert_source_for_mtls=None,
                quota_project_id=None,
                client_info=transports.base.DEFAULT_CLIENT_INFO,
                always_use_jwt_access=True,
            )

    # Check the case api_endpoint is not provided and GOOGLE_API_USE_MTLS_ENDPOINT has
    # unsupported value.
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "Unsupported"}):
        with pytest.raises(MutualTLSChannelError):
            client = client_class(transport=transport_name)

    # Check the case GOOGLE_API_USE_CLIENT_CERTIFICATE has unsupported value.
    with mock.patch.dict(
        os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": "Unsupported"}
    ):
        with pytest.raises(ValueError):
            client = client_class(transport=transport_name)

    # Check the case quota_project_id is provided
    options = client_options.ClientOptions(quota_project_id="octopus")
    with mock.patch.object(transport_class, "__init__") as patched:
        patched.return_value = None
        client = client_class(client_options=options, transport=transport_name)
        patched.assert_called_once_with(
            credentials=None,
            credentials_file=None,
            host=client.DEFAULT_ENDPOINT,
            scopes=None,
            client_cert_source_for_mtls=None,
            quota_project_id="octopus",
            client_info=transports.base.DEFAULT_CLIENT_INFO,
            always_use_jwt_access=True,
        )


@pytest.mark.parametrize(
    "client_class,transport_class,transport_name,use_client_cert_env",
    [
        (
            ForwardingRulesClient,
            transports.ForwardingRulesRestTransport,
            "rest",
            "true",
        ),
        (
            ForwardingRulesClient,
            transports.ForwardingRulesRestTransport,
            "rest",
            "false",
        ),
    ],
)
@mock.patch.object(
    ForwardingRulesClient,
    "DEFAULT_ENDPOINT",
    modify_default_endpoint(ForwardingRulesClient),
)
@mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "auto"})
def test_forwarding_rules_client_mtls_env_auto(
    client_class, transport_class, transport_name, use_client_cert_env
):
    # This tests the endpoint autoswitch behavior. Endpoint is autoswitched to the default
    # mtls endpoint, if GOOGLE_API_USE_CLIENT_CERTIFICATE is "true" and client cert exists.

    # Check the case client_cert_source is provided. Whether client cert is used depends on
    # GOOGLE_API_USE_CLIENT_CERTIFICATE value.
    with mock.patch.dict(
        os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": use_client_cert_env}
    ):
        options = client_options.ClientOptions(
            client_cert_source=client_cert_source_callback
        )
        with mock.patch.object(transport_class, "__init__") as patched:
            patched.return_value = None
            client = client_class(client_options=options, transport=transport_name)

            if use_client_cert_env == "false":
                expected_client_cert_source = None
                expected_host = client.DEFAULT_ENDPOINT
            else:
                expected_client_cert_source = client_cert_source_callback
                expected_host = client.DEFAULT_MTLS_ENDPOINT

            patched.assert_called_once_with(
                credentials=None,
                credentials_file=None,
                host=expected_host,
                scopes=None,
                client_cert_source_for_mtls=expected_client_cert_source,
                quota_project_id=None,
                client_info=transports.base.DEFAULT_CLIENT_INFO,
                always_use_jwt_access=True,
            )

    # Check the case ADC client cert is provided. Whether client cert is used depends on
    # GOOGLE_API_USE_CLIENT_CERTIFICATE value.
    with mock.patch.dict(
        os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": use_client_cert_env}
    ):
        with mock.patch.object(transport_class, "__init__") as patched:
            with mock.patch(
                "google.auth.transport.mtls.has_default_client_cert_source",
                return_value=True,
            ):
                with mock.patch(
                    "google.auth.transport.mtls.default_client_cert_source",
                    return_value=client_cert_source_callback,
                ):
                    if use_client_cert_env == "false":
                        expected_host = client.DEFAULT_ENDPOINT
                        expected_client_cert_source = None
                    else:
                        expected_host = client.DEFAULT_MTLS_ENDPOINT
                        expected_client_cert_source = client_cert_source_callback

                    patched.return_value = None
                    client = client_class(transport=transport_name)
                    patched.assert_called_once_with(
                        credentials=None,
                        credentials_file=None,
                        host=expected_host,
                        scopes=None,
                        client_cert_source_for_mtls=expected_client_cert_source,
                        quota_project_id=None,
                        client_info=transports.base.DEFAULT_CLIENT_INFO,
                        always_use_jwt_access=True,
                    )

    # Check the case client_cert_source and ADC client cert are not provided.
    with mock.patch.dict(
        os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": use_client_cert_env}
    ):
        with mock.patch.object(transport_class, "__init__") as patched:
            with mock.patch(
                "google.auth.transport.mtls.has_default_client_cert_source",
                return_value=False,
            ):
                patched.return_value = None
                client = client_class(transport=transport_name)
                patched.assert_called_once_with(
                    credentials=None,
                    credentials_file=None,
                    host=client.DEFAULT_ENDPOINT,
                    scopes=None,
                    client_cert_source_for_mtls=None,
                    quota_project_id=None,
                    client_info=transports.base.DEFAULT_CLIENT_INFO,
                    always_use_jwt_access=True,
                )


@pytest.mark.parametrize("client_class", [ForwardingRulesClient])
@mock.patch.object(
    ForwardingRulesClient,
    "DEFAULT_ENDPOINT",
    modify_default_endpoint(ForwardingRulesClient),
)
def test_forwarding_rules_client_get_mtls_endpoint_and_cert_source(client_class):
    mock_client_cert_source = mock.Mock()

    # Test the case GOOGLE_API_USE_CLIENT_CERTIFICATE is "true".
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": "true"}):
        mock_api_endpoint = "foo"
        options = client_options.ClientOptions(
            client_cert_source=mock_client_cert_source, api_endpoint=mock_api_endpoint
        )
        api_endpoint, cert_source = client_class.get_mtls_endpoint_and_cert_source(
            options
        )
        assert api_endpoint == mock_api_endpoint
        assert cert_source == mock_client_cert_source

    # Test the case GOOGLE_API_USE_CLIENT_CERTIFICATE is "false".
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": "false"}):
        mock_client_cert_source = mock.Mock()
        mock_api_endpoint = "foo"
        options = client_options.ClientOptions(
            client_cert_source=mock_client_cert_source, api_endpoint=mock_api_endpoint
        )
        api_endpoint, cert_source = client_class.get_mtls_endpoint_and_cert_source(
            options
        )
        assert api_endpoint == mock_api_endpoint
        assert cert_source is None

    # Test the case GOOGLE_API_USE_MTLS_ENDPOINT is "never".
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "never"}):
        api_endpoint, cert_source = client_class.get_mtls_endpoint_and_cert_source()
        assert api_endpoint == client_class.DEFAULT_ENDPOINT
        assert cert_source is None

    # Test the case GOOGLE_API_USE_MTLS_ENDPOINT is "always".
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "always"}):
        api_endpoint, cert_source = client_class.get_mtls_endpoint_and_cert_source()
        assert api_endpoint == client_class.DEFAULT_MTLS_ENDPOINT
        assert cert_source is None

    # Test the case GOOGLE_API_USE_MTLS_ENDPOINT is "auto" and default cert doesn't exist.
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": "true"}):
        with mock.patch(
            "google.auth.transport.mtls.has_default_client_cert_source",
            return_value=False,
        ):
            api_endpoint, cert_source = client_class.get_mtls_endpoint_and_cert_source()
            assert api_endpoint == client_class.DEFAULT_ENDPOINT
            assert cert_source is None

    # Test the case GOOGLE_API_USE_MTLS_ENDPOINT is "auto" and default cert exists.
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": "true"}):
        with mock.patch(
            "google.auth.transport.mtls.has_default_client_cert_source",
            return_value=True,
        ):
            with mock.patch(
                "google.auth.transport.mtls.default_client_cert_source",
                return_value=mock_client_cert_source,
            ):
                (
                    api_endpoint,
                    cert_source,
                ) = client_class.get_mtls_endpoint_and_cert_source()
                assert api_endpoint == client_class.DEFAULT_MTLS_ENDPOINT
                assert cert_source == mock_client_cert_source


@pytest.mark.parametrize(
    "client_class,transport_class,transport_name",
    [(ForwardingRulesClient, transports.ForwardingRulesRestTransport, "rest"),],
)
def test_forwarding_rules_client_client_options_scopes(
    client_class, transport_class, transport_name
):
    # Check the case scopes are provided.
    options = client_options.ClientOptions(scopes=["1", "2"],)
    with mock.patch.object(transport_class, "__init__") as patched:
        patched.return_value = None
        client = client_class(client_options=options, transport=transport_name)
        patched.assert_called_once_with(
            credentials=None,
            credentials_file=None,
            host=client.DEFAULT_ENDPOINT,
            scopes=["1", "2"],
            client_cert_source_for_mtls=None,
            quota_project_id=None,
            client_info=transports.base.DEFAULT_CLIENT_INFO,
            always_use_jwt_access=True,
        )


@pytest.mark.parametrize(
    "client_class,transport_class,transport_name,grpc_helpers",
    [(ForwardingRulesClient, transports.ForwardingRulesRestTransport, "rest", None),],
)
def test_forwarding_rules_client_client_options_credentials_file(
    client_class, transport_class, transport_name, grpc_helpers
):
    # Check the case credentials file is provided.
    options = client_options.ClientOptions(credentials_file="credentials.json")

    with mock.patch.object(transport_class, "__init__") as patched:
        patched.return_value = None
        client = client_class(client_options=options, transport=transport_name)
        patched.assert_called_once_with(
            credentials=None,
            credentials_file="credentials.json",
            host=client.DEFAULT_ENDPOINT,
            scopes=None,
            client_cert_source_for_mtls=None,
            quota_project_id=None,
            client_info=transports.base.DEFAULT_CLIENT_INFO,
            always_use_jwt_access=True,
        )


@pytest.mark.parametrize(
    "request_type", [compute.AggregatedListForwardingRulesRequest, dict,]
)
def test_aggregated_list_rest(request_type):
    client = ForwardingRulesClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest",
    )

    # send a request that will satisfy transcoding
    request_init = {"project": "sample1"}
    request = request_type(request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = compute.ForwardingRuleAggregatedList(
            id="id_value",
            kind="kind_value",
            next_page_token="next_page_token_value",
            self_link="self_link_value",
            unreachables=["unreachables_value"],
        )

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        json_return_value = compute.ForwardingRuleAggregatedList.to_json(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        response = client.aggregated_list(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.AggregatedListPager)
    assert response.id == "id_value"
    assert response.kind == "kind_value"
    assert response.next_page_token == "next_page_token_value"
    assert response.self_link == "self_link_value"
    assert response.unreachables == ["unreachables_value"]


def test_aggregated_list_rest_required_fields(
    request_type=compute.AggregatedListForwardingRulesRequest,
):
    transport_class = transports.ForwardingRulesRestTransport

    request_init = {}
    request_init["project"] = ""
    request = request_type(request_init)
    jsonified_request = json.loads(
        request_type.to_json(
            request, including_default_value_fields=False, use_integers_for_enums=False
        )
    )

    # verify fields with default values are dropped

    unset_fields = transport_class(
        credentials=ga_credentials.AnonymousCredentials()
    ).aggregated_list._get_unset_required_fields(jsonified_request)
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["project"] = "project_value"

    unset_fields = transport_class(
        credentials=ga_credentials.AnonymousCredentials()
    ).aggregated_list._get_unset_required_fields(jsonified_request)
    # Check that path parameters and body parameters are not mixing in.
    assert not set(unset_fields) - set(
        (
            "filter",
            "include_all_scopes",
            "max_results",
            "order_by",
            "page_token",
            "return_partial_success",
        )
    )
    jsonified_request.update(unset_fields)

    # verify required fields with non-default values are left alone
    assert "project" in jsonified_request
    assert jsonified_request["project"] == "project_value"

    client = ForwardingRulesClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest",
    )
    request = request_type(request_init)

    # Designate an appropriate value for the returned response.
    return_value = compute.ForwardingRuleAggregatedList()
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # We need to mock transcode() because providing default values
        # for required fields will fail the real version if the http_options
        # expect actual values for those fields.
        with mock.patch.object(path_template, "transcode") as transcode:
            # A uri without fields and an empty body will force all the
            # request fields to show up in the query_params.
            transcode_result = {
                "uri": "v1/sample_method",
                "method": "get",
                "query_params": request_init,
            }
            transcode.return_value = transcode_result

            response_value = Response()
            response_value.status_code = 200
            json_return_value = compute.ForwardingRuleAggregatedList.to_json(
                return_value
            )
            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value

            response = client.aggregated_list(request)

            expected_params = []
            actual_params = req.call_args.kwargs["params"]
            assert expected_params == actual_params


def test_aggregated_list_rest_unset_required_fields():
    transport = transports.ForwardingRulesRestTransport(
        credentials=ga_credentials.AnonymousCredentials
    )

    unset_fields = transport.aggregated_list._get_unset_required_fields({})
    assert set(unset_fields) == (
        set(
            (
                "filter",
                "includeAllScopes",
                "maxResults",
                "orderBy",
                "pageToken",
                "returnPartialSuccess",
            )
        )
        & set(("project",))
    )


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_aggregated_list_rest_interceptors(null_interceptor):
    transport = transports.ForwardingRulesRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.ForwardingRulesRestInterceptor(),
    )
    client = ForwardingRulesClient(transport=transport)
    with mock.patch.object(
        type(client.transport._session), "request"
    ) as req, mock.patch.object(
        path_template, "transcode"
    ) as transcode, mock.patch.object(
        transports.ForwardingRulesRestInterceptor, "post_aggregated_list"
    ) as post, mock.patch.object(
        transports.ForwardingRulesRestInterceptor, "pre_aggregated_list"
    ) as pre:
        pre.assert_not_called()
        post.assert_not_called()

        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": None,
            "query_params": {},
        }

        req.return_value = Response()
        req.return_value.status_code = 200
        req.return_value.request = PreparedRequest()
        req.return_value._content = compute.ForwardingRuleAggregatedList.to_json(
            compute.ForwardingRuleAggregatedList()
        )

        request = compute.AggregatedListForwardingRulesRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = compute.ForwardingRuleAggregatedList

        client.aggregated_list(
            request, metadata=[("key", "val"), ("cephalopod", "squid"),]
        )

        pre.assert_called_once()
        post.assert_called_once()


def test_aggregated_list_rest_bad_request(
    transport: str = "rest", request_type=compute.AggregatedListForwardingRulesRequest
):
    client = ForwardingRulesClient(
        credentials=ga_credentials.AnonymousCredentials(), transport=transport,
    )

    # send a request that will satisfy transcoding
    request_init = {"project": "sample1"}
    request = request_type(request_init)

    # Mock the http request call within the method and fake a BadRequest error.
    with mock.patch.object(Session, "request") as req, pytest.raises(
        core_exceptions.BadRequest
    ):
        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 400
        response_value.request = Request()
        req.return_value = response_value
        client.aggregated_list(request)


def test_aggregated_list_rest_flattened():
    client = ForwardingRulesClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = compute.ForwardingRuleAggregatedList()

        # get arguments that satisfy an http rule for this method
        sample_request = {"project": "sample1"}

        # get truthy value for each flattened field
        mock_args = dict(project="project_value",)
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        json_return_value = compute.ForwardingRuleAggregatedList.to_json(return_value)

        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value

        client.aggregated_list(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/compute/v1/projects/{project}/aggregated/forwardingRules"
            % client.transport._host,
            args[1],
        )


def test_aggregated_list_rest_flattened_error(transport: str = "rest"):
    client = ForwardingRulesClient(
        credentials=ga_credentials.AnonymousCredentials(), transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.aggregated_list(
            compute.AggregatedListForwardingRulesRequest(), project="project_value",
        )


def test_aggregated_list_rest_pager(transport: str = "rest"):
    client = ForwardingRulesClient(
        credentials=ga_credentials.AnonymousCredentials(), transport=transport,
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # TODO(kbandes): remove this mock unless there's a good reason for it.
        # with mock.patch.object(path_template, 'transcode') as transcode:
        # Set the response as a series of pages
        response = (
            compute.ForwardingRuleAggregatedList(
                items={
                    "a": compute.ForwardingRulesScopedList(),
                    "b": compute.ForwardingRulesScopedList(),
                    "c": compute.ForwardingRulesScopedList(),
                },
                next_page_token="abc",
            ),
            compute.ForwardingRuleAggregatedList(items={}, next_page_token="def",),
            compute.ForwardingRuleAggregatedList(
                items={"g": compute.ForwardingRulesScopedList(),},
                next_page_token="ghi",
            ),
            compute.ForwardingRuleAggregatedList(
                items={
                    "h": compute.ForwardingRulesScopedList(),
                    "i": compute.ForwardingRulesScopedList(),
                },
            ),
        )
        # Two responses for two calls
        response = response + response

        # Wrap the values into proper Response objs
        response = tuple(
            compute.ForwardingRuleAggregatedList.to_json(x) for x in response
        )
        return_values = tuple(Response() for i in response)
        for return_val, response_val in zip(return_values, response):
            return_val._content = response_val.encode("UTF-8")
            return_val.status_code = 200
        req.side_effect = return_values

        sample_request = {"project": "sample1"}

        pager = client.aggregated_list(request=sample_request)

        assert isinstance(pager.get("a"), compute.ForwardingRulesScopedList)
        assert pager.get("h") is None

        results = list(pager)
        assert len(results) == 6
        assert all(isinstance(i, tuple) for i in results)
        for result in results:
            assert isinstance(result, tuple)
            assert tuple(type(t) for t in result) == (
                str,
                compute.ForwardingRulesScopedList,
            )

        assert pager.get("a") is None
        assert isinstance(pager.get("h"), compute.ForwardingRulesScopedList)

        pages = list(client.aggregated_list(request=sample_request).pages)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


@pytest.mark.parametrize("request_type", [compute.DeleteForwardingRuleRequest, dict,])
def test_delete_unary_rest(request_type):
    client = ForwardingRulesClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest",
    )

    # send a request that will satisfy transcoding
    request_init = {
        "project": "sample1",
        "region": "sample2",
        "forwarding_rule": "sample3",
    }
    request = request_type(request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = compute.Operation(
            client_operation_id="client_operation_id_value",
            creation_timestamp="creation_timestamp_value",
            description="description_value",
            end_time="end_time_value",
            http_error_message="http_error_message_value",
            http_error_status_code=2374,
            id=205,
            insert_time="insert_time_value",
            kind="kind_value",
            name="name_value",
            operation_group_id="operation_group_id_value",
            operation_type="operation_type_value",
            progress=885,
            region="region_value",
            self_link="self_link_value",
            start_time="start_time_value",
            status=compute.Operation.Status.DONE,
            status_message="status_message_value",
            target_id=947,
            target_link="target_link_value",
            user="user_value",
            zone="zone_value",
        )

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        json_return_value = compute.Operation.to_json(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        response = client.delete_unary(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, compute.Operation)
    assert response.client_operation_id == "client_operation_id_value"
    assert response.creation_timestamp == "creation_timestamp_value"
    assert response.description == "description_value"
    assert response.end_time == "end_time_value"
    assert response.http_error_message == "http_error_message_value"
    assert response.http_error_status_code == 2374
    assert response.id == 205
    assert response.insert_time == "insert_time_value"
    assert response.kind == "kind_value"
    assert response.name == "name_value"
    assert response.operation_group_id == "operation_group_id_value"
    assert response.operation_type == "operation_type_value"
    assert response.progress == 885
    assert response.region == "region_value"
    assert response.self_link == "self_link_value"
    assert response.start_time == "start_time_value"
    assert response.status == compute.Operation.Status.DONE
    assert response.status_message == "status_message_value"
    assert response.target_id == 947
    assert response.target_link == "target_link_value"
    assert response.user == "user_value"
    assert response.zone == "zone_value"


def test_delete_unary_rest_required_fields(
    request_type=compute.DeleteForwardingRuleRequest,
):
    transport_class = transports.ForwardingRulesRestTransport

    request_init = {}
    request_init["forwarding_rule"] = ""
    request_init["project"] = ""
    request_init["region"] = ""
    request = request_type(request_init)
    jsonified_request = json.loads(
        request_type.to_json(
            request, including_default_value_fields=False, use_integers_for_enums=False
        )
    )

    # verify fields with default values are dropped

    unset_fields = transport_class(
        credentials=ga_credentials.AnonymousCredentials()
    ).delete._get_unset_required_fields(jsonified_request)
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["forwardingRule"] = "forwarding_rule_value"
    jsonified_request["project"] = "project_value"
    jsonified_request["region"] = "region_value"

    unset_fields = transport_class(
        credentials=ga_credentials.AnonymousCredentials()
    ).delete._get_unset_required_fields(jsonified_request)
    # Check that path parameters and body parameters are not mixing in.
    assert not set(unset_fields) - set(("request_id",))
    jsonified_request.update(unset_fields)

    # verify required fields with non-default values are left alone
    assert "forwardingRule" in jsonified_request
    assert jsonified_request["forwardingRule"] == "forwarding_rule_value"
    assert "project" in jsonified_request
    assert jsonified_request["project"] == "project_value"
    assert "region" in jsonified_request
    assert jsonified_request["region"] == "region_value"

    client = ForwardingRulesClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest",
    )
    request = request_type(request_init)

    # Designate an appropriate value for the returned response.
    return_value = compute.Operation()
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # We need to mock transcode() because providing default values
        # for required fields will fail the real version if the http_options
        # expect actual values for those fields.
        with mock.patch.object(path_template, "transcode") as transcode:
            # A uri without fields and an empty body will force all the
            # request fields to show up in the query_params.
            transcode_result = {
                "uri": "v1/sample_method",
                "method": "delete",
                "query_params": request_init,
            }
            transcode.return_value = transcode_result

            response_value = Response()
            response_value.status_code = 200
            json_return_value = compute.Operation.to_json(return_value)
            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value

            response = client.delete_unary(request)

            expected_params = []
            actual_params = req.call_args.kwargs["params"]
            assert expected_params == actual_params


def test_delete_unary_rest_unset_required_fields():
    transport = transports.ForwardingRulesRestTransport(
        credentials=ga_credentials.AnonymousCredentials
    )

    unset_fields = transport.delete._get_unset_required_fields({})
    assert set(unset_fields) == (
        set(("requestId",)) & set(("forwardingRule", "project", "region",))
    )


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_delete_unary_rest_interceptors(null_interceptor):
    transport = transports.ForwardingRulesRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.ForwardingRulesRestInterceptor(),
    )
    client = ForwardingRulesClient(transport=transport)
    with mock.patch.object(
        type(client.transport._session), "request"
    ) as req, mock.patch.object(
        path_template, "transcode"
    ) as transcode, mock.patch.object(
        transports.ForwardingRulesRestInterceptor, "post_delete"
    ) as post, mock.patch.object(
        transports.ForwardingRulesRestInterceptor, "pre_delete"
    ) as pre:
        pre.assert_not_called()
        post.assert_not_called()

        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": None,
            "query_params": {},
        }

        req.return_value = Response()
        req.return_value.status_code = 200
        req.return_value.request = PreparedRequest()
        req.return_value._content = compute.Operation.to_json(compute.Operation())

        request = compute.DeleteForwardingRuleRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = compute.Operation

        client.delete_unary(
            request, metadata=[("key", "val"), ("cephalopod", "squid"),]
        )

        pre.assert_called_once()
        post.assert_called_once()


def test_delete_unary_rest_bad_request(
    transport: str = "rest", request_type=compute.DeleteForwardingRuleRequest
):
    client = ForwardingRulesClient(
        credentials=ga_credentials.AnonymousCredentials(), transport=transport,
    )

    # send a request that will satisfy transcoding
    request_init = {
        "project": "sample1",
        "region": "sample2",
        "forwarding_rule": "sample3",
    }
    request = request_type(request_init)

    # Mock the http request call within the method and fake a BadRequest error.
    with mock.patch.object(Session, "request") as req, pytest.raises(
        core_exceptions.BadRequest
    ):
        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 400
        response_value.request = Request()
        req.return_value = response_value
        client.delete_unary(request)


def test_delete_unary_rest_flattened():
    client = ForwardingRulesClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = compute.Operation()

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "project": "sample1",
            "region": "sample2",
            "forwarding_rule": "sample3",
        }

        # get truthy value for each flattened field
        mock_args = dict(
            project="project_value",
            region="region_value",
            forwarding_rule="forwarding_rule_value",
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        json_return_value = compute.Operation.to_json(return_value)

        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value

        client.delete_unary(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/compute/v1/projects/{project}/regions/{region}/forwardingRules/{forwarding_rule}"
            % client.transport._host,
            args[1],
        )


def test_delete_unary_rest_flattened_error(transport: str = "rest"):
    client = ForwardingRulesClient(
        credentials=ga_credentials.AnonymousCredentials(), transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.delete_unary(
            compute.DeleteForwardingRuleRequest(),
            project="project_value",
            region="region_value",
            forwarding_rule="forwarding_rule_value",
        )


def test_delete_unary_rest_error():
    client = ForwardingRulesClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )


@pytest.mark.parametrize("request_type", [compute.GetForwardingRuleRequest, dict,])
def test_get_rest(request_type):
    client = ForwardingRulesClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest",
    )

    # send a request that will satisfy transcoding
    request_init = {
        "project": "sample1",
        "region": "sample2",
        "forwarding_rule": "sample3",
    }
    request = request_type(request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = compute.ForwardingRule(
            I_p_address="I_p_address_value",
            I_p_protocol="I_p_protocol_value",
            all_ports=True,
            allow_global_access=True,
            backend_service="backend_service_value",
            creation_timestamp="creation_timestamp_value",
            description="description_value",
            fingerprint="fingerprint_value",
            id=205,
            ip_version="ip_version_value",
            is_mirroring_collector=True,
            kind="kind_value",
            label_fingerprint="label_fingerprint_value",
            load_balancing_scheme="load_balancing_scheme_value",
            name="name_value",
            network="network_value",
            network_tier="network_tier_value",
            port_range="port_range_value",
            ports=["ports_value"],
            psc_connection_id=1793,
            psc_connection_status="psc_connection_status_value",
            region="region_value",
            self_link="self_link_value",
            service_label="service_label_value",
            service_name="service_name_value",
            subnetwork="subnetwork_value",
            target="target_value",
        )

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        json_return_value = compute.ForwardingRule.to_json(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        response = client.get(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, compute.ForwardingRule)
    assert response.I_p_address == "I_p_address_value"
    assert response.I_p_protocol == "I_p_protocol_value"
    assert response.all_ports is True
    assert response.allow_global_access is True
    assert response.backend_service == "backend_service_value"
    assert response.creation_timestamp == "creation_timestamp_value"
    assert response.description == "description_value"
    assert response.fingerprint == "fingerprint_value"
    assert response.id == 205
    assert response.ip_version == "ip_version_value"
    assert response.is_mirroring_collector is True
    assert response.kind == "kind_value"
    assert response.label_fingerprint == "label_fingerprint_value"
    assert response.load_balancing_scheme == "load_balancing_scheme_value"
    assert response.name == "name_value"
    assert response.network == "network_value"
    assert response.network_tier == "network_tier_value"
    assert response.port_range == "port_range_value"
    assert response.ports == ["ports_value"]
    assert response.psc_connection_id == 1793
    assert response.psc_connection_status == "psc_connection_status_value"
    assert response.region == "region_value"
    assert response.self_link == "self_link_value"
    assert response.service_label == "service_label_value"
    assert response.service_name == "service_name_value"
    assert response.subnetwork == "subnetwork_value"
    assert response.target == "target_value"


def test_get_rest_required_fields(request_type=compute.GetForwardingRuleRequest):
    transport_class = transports.ForwardingRulesRestTransport

    request_init = {}
    request_init["forwarding_rule"] = ""
    request_init["project"] = ""
    request_init["region"] = ""
    request = request_type(request_init)
    jsonified_request = json.loads(
        request_type.to_json(
            request, including_default_value_fields=False, use_integers_for_enums=False
        )
    )

    # verify fields with default values are dropped

    unset_fields = transport_class(
        credentials=ga_credentials.AnonymousCredentials()
    ).get._get_unset_required_fields(jsonified_request)
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["forwardingRule"] = "forwarding_rule_value"
    jsonified_request["project"] = "project_value"
    jsonified_request["region"] = "region_value"

    unset_fields = transport_class(
        credentials=ga_credentials.AnonymousCredentials()
    ).get._get_unset_required_fields(jsonified_request)
    jsonified_request.update(unset_fields)

    # verify required fields with non-default values are left alone
    assert "forwardingRule" in jsonified_request
    assert jsonified_request["forwardingRule"] == "forwarding_rule_value"
    assert "project" in jsonified_request
    assert jsonified_request["project"] == "project_value"
    assert "region" in jsonified_request
    assert jsonified_request["region"] == "region_value"

    client = ForwardingRulesClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest",
    )
    request = request_type(request_init)

    # Designate an appropriate value for the returned response.
    return_value = compute.ForwardingRule()
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # We need to mock transcode() because providing default values
        # for required fields will fail the real version if the http_options
        # expect actual values for those fields.
        with mock.patch.object(path_template, "transcode") as transcode:
            # A uri without fields and an empty body will force all the
            # request fields to show up in the query_params.
            transcode_result = {
                "uri": "v1/sample_method",
                "method": "get",
                "query_params": request_init,
            }
            transcode.return_value = transcode_result

            response_value = Response()
            response_value.status_code = 200
            json_return_value = compute.ForwardingRule.to_json(return_value)
            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value

            response = client.get(request)

            expected_params = []
            actual_params = req.call_args.kwargs["params"]
            assert expected_params == actual_params


def test_get_rest_unset_required_fields():
    transport = transports.ForwardingRulesRestTransport(
        credentials=ga_credentials.AnonymousCredentials
    )

    unset_fields = transport.get._get_unset_required_fields({})
    assert set(unset_fields) == (
        set(()) & set(("forwardingRule", "project", "region",))
    )


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_get_rest_interceptors(null_interceptor):
    transport = transports.ForwardingRulesRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.ForwardingRulesRestInterceptor(),
    )
    client = ForwardingRulesClient(transport=transport)
    with mock.patch.object(
        type(client.transport._session), "request"
    ) as req, mock.patch.object(
        path_template, "transcode"
    ) as transcode, mock.patch.object(
        transports.ForwardingRulesRestInterceptor, "post_get"
    ) as post, mock.patch.object(
        transports.ForwardingRulesRestInterceptor, "pre_get"
    ) as pre:
        pre.assert_not_called()
        post.assert_not_called()

        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": None,
            "query_params": {},
        }

        req.return_value = Response()
        req.return_value.status_code = 200
        req.return_value.request = PreparedRequest()
        req.return_value._content = compute.ForwardingRule.to_json(
            compute.ForwardingRule()
        )

        request = compute.GetForwardingRuleRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = compute.ForwardingRule

        client.get(request, metadata=[("key", "val"), ("cephalopod", "squid"),])

        pre.assert_called_once()
        post.assert_called_once()


def test_get_rest_bad_request(
    transport: str = "rest", request_type=compute.GetForwardingRuleRequest
):
    client = ForwardingRulesClient(
        credentials=ga_credentials.AnonymousCredentials(), transport=transport,
    )

    # send a request that will satisfy transcoding
    request_init = {
        "project": "sample1",
        "region": "sample2",
        "forwarding_rule": "sample3",
    }
    request = request_type(request_init)

    # Mock the http request call within the method and fake a BadRequest error.
    with mock.patch.object(Session, "request") as req, pytest.raises(
        core_exceptions.BadRequest
    ):
        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 400
        response_value.request = Request()
        req.return_value = response_value
        client.get(request)


def test_get_rest_flattened():
    client = ForwardingRulesClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = compute.ForwardingRule()

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "project": "sample1",
            "region": "sample2",
            "forwarding_rule": "sample3",
        }

        # get truthy value for each flattened field
        mock_args = dict(
            project="project_value",
            region="region_value",
            forwarding_rule="forwarding_rule_value",
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        json_return_value = compute.ForwardingRule.to_json(return_value)

        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value

        client.get(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/compute/v1/projects/{project}/regions/{region}/forwardingRules/{forwarding_rule}"
            % client.transport._host,
            args[1],
        )


def test_get_rest_flattened_error(transport: str = "rest"):
    client = ForwardingRulesClient(
        credentials=ga_credentials.AnonymousCredentials(), transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.get(
            compute.GetForwardingRuleRequest(),
            project="project_value",
            region="region_value",
            forwarding_rule="forwarding_rule_value",
        )


def test_get_rest_error():
    client = ForwardingRulesClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )


@pytest.mark.parametrize("request_type", [compute.InsertForwardingRuleRequest, dict,])
def test_insert_unary_rest(request_type):
    client = ForwardingRulesClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest",
    )

    # send a request that will satisfy transcoding
    request_init = {"project": "sample1", "region": "sample2"}
    request_init["forwarding_rule_resource"] = {
        "I_p_address": "I_p_address_value",
        "I_p_protocol": "I_p_protocol_value",
        "all_ports": True,
        "allow_global_access": True,
        "backend_service": "backend_service_value",
        "creation_timestamp": "creation_timestamp_value",
        "description": "description_value",
        "fingerprint": "fingerprint_value",
        "id": 205,
        "ip_version": "ip_version_value",
        "is_mirroring_collector": True,
        "kind": "kind_value",
        "label_fingerprint": "label_fingerprint_value",
        "labels": {},
        "load_balancing_scheme": "load_balancing_scheme_value",
        "metadata_filters": [
            {
                "filter_labels": [{"name": "name_value", "value": "value_value"}],
                "filter_match_criteria": "filter_match_criteria_value",
            }
        ],
        "name": "name_value",
        "network": "network_value",
        "network_tier": "network_tier_value",
        "port_range": "port_range_value",
        "ports": ["ports_value_1", "ports_value_2"],
        "psc_connection_id": 1793,
        "psc_connection_status": "psc_connection_status_value",
        "region": "region_value",
        "self_link": "self_link_value",
        "service_directory_registrations": [
            {
                "namespace": "namespace_value",
                "service": "service_value",
                "service_directory_region": "service_directory_region_value",
            }
        ],
        "service_label": "service_label_value",
        "service_name": "service_name_value",
        "subnetwork": "subnetwork_value",
        "target": "target_value",
    }
    request = request_type(request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = compute.Operation(
            client_operation_id="client_operation_id_value",
            creation_timestamp="creation_timestamp_value",
            description="description_value",
            end_time="end_time_value",
            http_error_message="http_error_message_value",
            http_error_status_code=2374,
            id=205,
            insert_time="insert_time_value",
            kind="kind_value",
            name="name_value",
            operation_group_id="operation_group_id_value",
            operation_type="operation_type_value",
            progress=885,
            region="region_value",
            self_link="self_link_value",
            start_time="start_time_value",
            status=compute.Operation.Status.DONE,
            status_message="status_message_value",
            target_id=947,
            target_link="target_link_value",
            user="user_value",
            zone="zone_value",
        )

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        json_return_value = compute.Operation.to_json(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        response = client.insert_unary(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, compute.Operation)
    assert response.client_operation_id == "client_operation_id_value"
    assert response.creation_timestamp == "creation_timestamp_value"
    assert response.description == "description_value"
    assert response.end_time == "end_time_value"
    assert response.http_error_message == "http_error_message_value"
    assert response.http_error_status_code == 2374
    assert response.id == 205
    assert response.insert_time == "insert_time_value"
    assert response.kind == "kind_value"
    assert response.name == "name_value"
    assert response.operation_group_id == "operation_group_id_value"
    assert response.operation_type == "operation_type_value"
    assert response.progress == 885
    assert response.region == "region_value"
    assert response.self_link == "self_link_value"
    assert response.start_time == "start_time_value"
    assert response.status == compute.Operation.Status.DONE
    assert response.status_message == "status_message_value"
    assert response.target_id == 947
    assert response.target_link == "target_link_value"
    assert response.user == "user_value"
    assert response.zone == "zone_value"


def test_insert_unary_rest_required_fields(
    request_type=compute.InsertForwardingRuleRequest,
):
    transport_class = transports.ForwardingRulesRestTransport

    request_init = {}
    request_init["project"] = ""
    request_init["region"] = ""
    request = request_type(request_init)
    jsonified_request = json.loads(
        request_type.to_json(
            request, including_default_value_fields=False, use_integers_for_enums=False
        )
    )

    # verify fields with default values are dropped

    unset_fields = transport_class(
        credentials=ga_credentials.AnonymousCredentials()
    ).insert._get_unset_required_fields(jsonified_request)
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["project"] = "project_value"
    jsonified_request["region"] = "region_value"

    unset_fields = transport_class(
        credentials=ga_credentials.AnonymousCredentials()
    ).insert._get_unset_required_fields(jsonified_request)
    # Check that path parameters and body parameters are not mixing in.
    assert not set(unset_fields) - set(("request_id",))
    jsonified_request.update(unset_fields)

    # verify required fields with non-default values are left alone
    assert "project" in jsonified_request
    assert jsonified_request["project"] == "project_value"
    assert "region" in jsonified_request
    assert jsonified_request["region"] == "region_value"

    client = ForwardingRulesClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest",
    )
    request = request_type(request_init)

    # Designate an appropriate value for the returned response.
    return_value = compute.Operation()
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # We need to mock transcode() because providing default values
        # for required fields will fail the real version if the http_options
        # expect actual values for those fields.
        with mock.patch.object(path_template, "transcode") as transcode:
            # A uri without fields and an empty body will force all the
            # request fields to show up in the query_params.
            transcode_result = {
                "uri": "v1/sample_method",
                "method": "post",
                "query_params": request_init,
            }
            transcode_result["body"] = {}
            transcode.return_value = transcode_result

            response_value = Response()
            response_value.status_code = 200
            json_return_value = compute.Operation.to_json(return_value)
            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value

            response = client.insert_unary(request)

            expected_params = []
            actual_params = req.call_args.kwargs["params"]
            assert expected_params == actual_params


def test_insert_unary_rest_unset_required_fields():
    transport = transports.ForwardingRulesRestTransport(
        credentials=ga_credentials.AnonymousCredentials
    )

    unset_fields = transport.insert._get_unset_required_fields({})
    assert set(unset_fields) == (
        set(("requestId",)) & set(("forwardingRuleResource", "project", "region",))
    )


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_insert_unary_rest_interceptors(null_interceptor):
    transport = transports.ForwardingRulesRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.ForwardingRulesRestInterceptor(),
    )
    client = ForwardingRulesClient(transport=transport)
    with mock.patch.object(
        type(client.transport._session), "request"
    ) as req, mock.patch.object(
        path_template, "transcode"
    ) as transcode, mock.patch.object(
        transports.ForwardingRulesRestInterceptor, "post_insert"
    ) as post, mock.patch.object(
        transports.ForwardingRulesRestInterceptor, "pre_insert"
    ) as pre:
        pre.assert_not_called()
        post.assert_not_called()

        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": None,
            "query_params": {},
        }

        req.return_value = Response()
        req.return_value.status_code = 200
        req.return_value.request = PreparedRequest()
        req.return_value._content = compute.Operation.to_json(compute.Operation())

        request = compute.InsertForwardingRuleRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = compute.Operation

        client.insert_unary(
            request, metadata=[("key", "val"), ("cephalopod", "squid"),]
        )

        pre.assert_called_once()
        post.assert_called_once()


def test_insert_unary_rest_bad_request(
    transport: str = "rest", request_type=compute.InsertForwardingRuleRequest
):
    client = ForwardingRulesClient(
        credentials=ga_credentials.AnonymousCredentials(), transport=transport,
    )

    # send a request that will satisfy transcoding
    request_init = {"project": "sample1", "region": "sample2"}
    request_init["forwarding_rule_resource"] = {
        "I_p_address": "I_p_address_value",
        "I_p_protocol": "I_p_protocol_value",
        "all_ports": True,
        "allow_global_access": True,
        "backend_service": "backend_service_value",
        "creation_timestamp": "creation_timestamp_value",
        "description": "description_value",
        "fingerprint": "fingerprint_value",
        "id": 205,
        "ip_version": "ip_version_value",
        "is_mirroring_collector": True,
        "kind": "kind_value",
        "label_fingerprint": "label_fingerprint_value",
        "labels": {},
        "load_balancing_scheme": "load_balancing_scheme_value",
        "metadata_filters": [
            {
                "filter_labels": [{"name": "name_value", "value": "value_value"}],
                "filter_match_criteria": "filter_match_criteria_value",
            }
        ],
        "name": "name_value",
        "network": "network_value",
        "network_tier": "network_tier_value",
        "port_range": "port_range_value",
        "ports": ["ports_value_1", "ports_value_2"],
        "psc_connection_id": 1793,
        "psc_connection_status": "psc_connection_status_value",
        "region": "region_value",
        "self_link": "self_link_value",
        "service_directory_registrations": [
            {
                "namespace": "namespace_value",
                "service": "service_value",
                "service_directory_region": "service_directory_region_value",
            }
        ],
        "service_label": "service_label_value",
        "service_name": "service_name_value",
        "subnetwork": "subnetwork_value",
        "target": "target_value",
    }
    request = request_type(request_init)

    # Mock the http request call within the method and fake a BadRequest error.
    with mock.patch.object(Session, "request") as req, pytest.raises(
        core_exceptions.BadRequest
    ):
        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 400
        response_value.request = Request()
        req.return_value = response_value
        client.insert_unary(request)


def test_insert_unary_rest_flattened():
    client = ForwardingRulesClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = compute.Operation()

        # get arguments that satisfy an http rule for this method
        sample_request = {"project": "sample1", "region": "sample2"}

        # get truthy value for each flattened field
        mock_args = dict(
            project="project_value",
            region="region_value",
            forwarding_rule_resource=compute.ForwardingRule(
                I_p_address="I_p_address_value"
            ),
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        json_return_value = compute.Operation.to_json(return_value)

        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value

        client.insert_unary(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/compute/v1/projects/{project}/regions/{region}/forwardingRules"
            % client.transport._host,
            args[1],
        )


def test_insert_unary_rest_flattened_error(transport: str = "rest"):
    client = ForwardingRulesClient(
        credentials=ga_credentials.AnonymousCredentials(), transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.insert_unary(
            compute.InsertForwardingRuleRequest(),
            project="project_value",
            region="region_value",
            forwarding_rule_resource=compute.ForwardingRule(
                I_p_address="I_p_address_value"
            ),
        )


def test_insert_unary_rest_error():
    client = ForwardingRulesClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )


@pytest.mark.parametrize("request_type", [compute.ListForwardingRulesRequest, dict,])
def test_list_rest(request_type):
    client = ForwardingRulesClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest",
    )

    # send a request that will satisfy transcoding
    request_init = {"project": "sample1", "region": "sample2"}
    request = request_type(request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = compute.ForwardingRuleList(
            id="id_value",
            kind="kind_value",
            next_page_token="next_page_token_value",
            self_link="self_link_value",
        )

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        json_return_value = compute.ForwardingRuleList.to_json(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        response = client.list(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListPager)
    assert response.id == "id_value"
    assert response.kind == "kind_value"
    assert response.next_page_token == "next_page_token_value"
    assert response.self_link == "self_link_value"


def test_list_rest_required_fields(request_type=compute.ListForwardingRulesRequest):
    transport_class = transports.ForwardingRulesRestTransport

    request_init = {}
    request_init["project"] = ""
    request_init["region"] = ""
    request = request_type(request_init)
    jsonified_request = json.loads(
        request_type.to_json(
            request, including_default_value_fields=False, use_integers_for_enums=False
        )
    )

    # verify fields with default values are dropped

    unset_fields = transport_class(
        credentials=ga_credentials.AnonymousCredentials()
    ).list._get_unset_required_fields(jsonified_request)
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["project"] = "project_value"
    jsonified_request["region"] = "region_value"

    unset_fields = transport_class(
        credentials=ga_credentials.AnonymousCredentials()
    ).list._get_unset_required_fields(jsonified_request)
    # Check that path parameters and body parameters are not mixing in.
    assert not set(unset_fields) - set(
        ("filter", "max_results", "order_by", "page_token", "return_partial_success",)
    )
    jsonified_request.update(unset_fields)

    # verify required fields with non-default values are left alone
    assert "project" in jsonified_request
    assert jsonified_request["project"] == "project_value"
    assert "region" in jsonified_request
    assert jsonified_request["region"] == "region_value"

    client = ForwardingRulesClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest",
    )
    request = request_type(request_init)

    # Designate an appropriate value for the returned response.
    return_value = compute.ForwardingRuleList()
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # We need to mock transcode() because providing default values
        # for required fields will fail the real version if the http_options
        # expect actual values for those fields.
        with mock.patch.object(path_template, "transcode") as transcode:
            # A uri without fields and an empty body will force all the
            # request fields to show up in the query_params.
            transcode_result = {
                "uri": "v1/sample_method",
                "method": "get",
                "query_params": request_init,
            }
            transcode.return_value = transcode_result

            response_value = Response()
            response_value.status_code = 200
            json_return_value = compute.ForwardingRuleList.to_json(return_value)
            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value

            response = client.list(request)

            expected_params = []
            actual_params = req.call_args.kwargs["params"]
            assert expected_params == actual_params


def test_list_rest_unset_required_fields():
    transport = transports.ForwardingRulesRestTransport(
        credentials=ga_credentials.AnonymousCredentials
    )

    unset_fields = transport.list._get_unset_required_fields({})
    assert set(unset_fields) == (
        set(("filter", "maxResults", "orderBy", "pageToken", "returnPartialSuccess",))
        & set(("project", "region",))
    )


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_list_rest_interceptors(null_interceptor):
    transport = transports.ForwardingRulesRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.ForwardingRulesRestInterceptor(),
    )
    client = ForwardingRulesClient(transport=transport)
    with mock.patch.object(
        type(client.transport._session), "request"
    ) as req, mock.patch.object(
        path_template, "transcode"
    ) as transcode, mock.patch.object(
        transports.ForwardingRulesRestInterceptor, "post_list"
    ) as post, mock.patch.object(
        transports.ForwardingRulesRestInterceptor, "pre_list"
    ) as pre:
        pre.assert_not_called()
        post.assert_not_called()

        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": None,
            "query_params": {},
        }

        req.return_value = Response()
        req.return_value.status_code = 200
        req.return_value.request = PreparedRequest()
        req.return_value._content = compute.ForwardingRuleList.to_json(
            compute.ForwardingRuleList()
        )

        request = compute.ListForwardingRulesRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = compute.ForwardingRuleList

        client.list(request, metadata=[("key", "val"), ("cephalopod", "squid"),])

        pre.assert_called_once()
        post.assert_called_once()


def test_list_rest_bad_request(
    transport: str = "rest", request_type=compute.ListForwardingRulesRequest
):
    client = ForwardingRulesClient(
        credentials=ga_credentials.AnonymousCredentials(), transport=transport,
    )

    # send a request that will satisfy transcoding
    request_init = {"project": "sample1", "region": "sample2"}
    request = request_type(request_init)

    # Mock the http request call within the method and fake a BadRequest error.
    with mock.patch.object(Session, "request") as req, pytest.raises(
        core_exceptions.BadRequest
    ):
        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 400
        response_value.request = Request()
        req.return_value = response_value
        client.list(request)


def test_list_rest_flattened():
    client = ForwardingRulesClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = compute.ForwardingRuleList()

        # get arguments that satisfy an http rule for this method
        sample_request = {"project": "sample1", "region": "sample2"}

        # get truthy value for each flattened field
        mock_args = dict(project="project_value", region="region_value",)
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        json_return_value = compute.ForwardingRuleList.to_json(return_value)

        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value

        client.list(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/compute/v1/projects/{project}/regions/{region}/forwardingRules"
            % client.transport._host,
            args[1],
        )


def test_list_rest_flattened_error(transport: str = "rest"):
    client = ForwardingRulesClient(
        credentials=ga_credentials.AnonymousCredentials(), transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.list(
            compute.ListForwardingRulesRequest(),
            project="project_value",
            region="region_value",
        )


def test_list_rest_pager(transport: str = "rest"):
    client = ForwardingRulesClient(
        credentials=ga_credentials.AnonymousCredentials(), transport=transport,
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # TODO(kbandes): remove this mock unless there's a good reason for it.
        # with mock.patch.object(path_template, 'transcode') as transcode:
        # Set the response as a series of pages
        response = (
            compute.ForwardingRuleList(
                items=[
                    compute.ForwardingRule(),
                    compute.ForwardingRule(),
                    compute.ForwardingRule(),
                ],
                next_page_token="abc",
            ),
            compute.ForwardingRuleList(items=[], next_page_token="def",),
            compute.ForwardingRuleList(
                items=[compute.ForwardingRule(),], next_page_token="ghi",
            ),
            compute.ForwardingRuleList(
                items=[compute.ForwardingRule(), compute.ForwardingRule(),],
            ),
        )
        # Two responses for two calls
        response = response + response

        # Wrap the values into proper Response objs
        response = tuple(compute.ForwardingRuleList.to_json(x) for x in response)
        return_values = tuple(Response() for i in response)
        for return_val, response_val in zip(return_values, response):
            return_val._content = response_val.encode("UTF-8")
            return_val.status_code = 200
        req.side_effect = return_values

        sample_request = {"project": "sample1", "region": "sample2"}

        pager = client.list(request=sample_request)

        results = list(pager)
        assert len(results) == 6
        assert all(isinstance(i, compute.ForwardingRule) for i in results)

        pages = list(client.list(request=sample_request).pages)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


@pytest.mark.parametrize("request_type", [compute.PatchForwardingRuleRequest, dict,])
def test_patch_unary_rest(request_type):
    client = ForwardingRulesClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest",
    )

    # send a request that will satisfy transcoding
    request_init = {
        "project": "sample1",
        "region": "sample2",
        "forwarding_rule": "sample3",
    }
    request_init["forwarding_rule_resource"] = {
        "I_p_address": "I_p_address_value",
        "I_p_protocol": "I_p_protocol_value",
        "all_ports": True,
        "allow_global_access": True,
        "backend_service": "backend_service_value",
        "creation_timestamp": "creation_timestamp_value",
        "description": "description_value",
        "fingerprint": "fingerprint_value",
        "id": 205,
        "ip_version": "ip_version_value",
        "is_mirroring_collector": True,
        "kind": "kind_value",
        "label_fingerprint": "label_fingerprint_value",
        "labels": {},
        "load_balancing_scheme": "load_balancing_scheme_value",
        "metadata_filters": [
            {
                "filter_labels": [{"name": "name_value", "value": "value_value"}],
                "filter_match_criteria": "filter_match_criteria_value",
            }
        ],
        "name": "name_value",
        "network": "network_value",
        "network_tier": "network_tier_value",
        "port_range": "port_range_value",
        "ports": ["ports_value_1", "ports_value_2"],
        "psc_connection_id": 1793,
        "psc_connection_status": "psc_connection_status_value",
        "region": "region_value",
        "self_link": "self_link_value",
        "service_directory_registrations": [
            {
                "namespace": "namespace_value",
                "service": "service_value",
                "service_directory_region": "service_directory_region_value",
            }
        ],
        "service_label": "service_label_value",
        "service_name": "service_name_value",
        "subnetwork": "subnetwork_value",
        "target": "target_value",
    }
    request = request_type(request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = compute.Operation(
            client_operation_id="client_operation_id_value",
            creation_timestamp="creation_timestamp_value",
            description="description_value",
            end_time="end_time_value",
            http_error_message="http_error_message_value",
            http_error_status_code=2374,
            id=205,
            insert_time="insert_time_value",
            kind="kind_value",
            name="name_value",
            operation_group_id="operation_group_id_value",
            operation_type="operation_type_value",
            progress=885,
            region="region_value",
            self_link="self_link_value",
            start_time="start_time_value",
            status=compute.Operation.Status.DONE,
            status_message="status_message_value",
            target_id=947,
            target_link="target_link_value",
            user="user_value",
            zone="zone_value",
        )

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        json_return_value = compute.Operation.to_json(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        response = client.patch_unary(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, compute.Operation)
    assert response.client_operation_id == "client_operation_id_value"
    assert response.creation_timestamp == "creation_timestamp_value"
    assert response.description == "description_value"
    assert response.end_time == "end_time_value"
    assert response.http_error_message == "http_error_message_value"
    assert response.http_error_status_code == 2374
    assert response.id == 205
    assert response.insert_time == "insert_time_value"
    assert response.kind == "kind_value"
    assert response.name == "name_value"
    assert response.operation_group_id == "operation_group_id_value"
    assert response.operation_type == "operation_type_value"
    assert response.progress == 885
    assert response.region == "region_value"
    assert response.self_link == "self_link_value"
    assert response.start_time == "start_time_value"
    assert response.status == compute.Operation.Status.DONE
    assert response.status_message == "status_message_value"
    assert response.target_id == 947
    assert response.target_link == "target_link_value"
    assert response.user == "user_value"
    assert response.zone == "zone_value"


def test_patch_unary_rest_required_fields(
    request_type=compute.PatchForwardingRuleRequest,
):
    transport_class = transports.ForwardingRulesRestTransport

    request_init = {}
    request_init["forwarding_rule"] = ""
    request_init["project"] = ""
    request_init["region"] = ""
    request = request_type(request_init)
    jsonified_request = json.loads(
        request_type.to_json(
            request, including_default_value_fields=False, use_integers_for_enums=False
        )
    )

    # verify fields with default values are dropped

    unset_fields = transport_class(
        credentials=ga_credentials.AnonymousCredentials()
    ).patch._get_unset_required_fields(jsonified_request)
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["forwardingRule"] = "forwarding_rule_value"
    jsonified_request["project"] = "project_value"
    jsonified_request["region"] = "region_value"

    unset_fields = transport_class(
        credentials=ga_credentials.AnonymousCredentials()
    ).patch._get_unset_required_fields(jsonified_request)
    # Check that path parameters and body parameters are not mixing in.
    assert not set(unset_fields) - set(("request_id",))
    jsonified_request.update(unset_fields)

    # verify required fields with non-default values are left alone
    assert "forwardingRule" in jsonified_request
    assert jsonified_request["forwardingRule"] == "forwarding_rule_value"
    assert "project" in jsonified_request
    assert jsonified_request["project"] == "project_value"
    assert "region" in jsonified_request
    assert jsonified_request["region"] == "region_value"

    client = ForwardingRulesClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest",
    )
    request = request_type(request_init)

    # Designate an appropriate value for the returned response.
    return_value = compute.Operation()
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # We need to mock transcode() because providing default values
        # for required fields will fail the real version if the http_options
        # expect actual values for those fields.
        with mock.patch.object(path_template, "transcode") as transcode:
            # A uri without fields and an empty body will force all the
            # request fields to show up in the query_params.
            transcode_result = {
                "uri": "v1/sample_method",
                "method": "patch",
                "query_params": request_init,
            }
            transcode_result["body"] = {}
            transcode.return_value = transcode_result

            response_value = Response()
            response_value.status_code = 200
            json_return_value = compute.Operation.to_json(return_value)
            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value

            response = client.patch_unary(request)

            expected_params = []
            actual_params = req.call_args.kwargs["params"]
            assert expected_params == actual_params


def test_patch_unary_rest_unset_required_fields():
    transport = transports.ForwardingRulesRestTransport(
        credentials=ga_credentials.AnonymousCredentials
    )

    unset_fields = transport.patch._get_unset_required_fields({})
    assert set(unset_fields) == (
        set(("requestId",))
        & set(("forwardingRule", "forwardingRuleResource", "project", "region",))
    )


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_patch_unary_rest_interceptors(null_interceptor):
    transport = transports.ForwardingRulesRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.ForwardingRulesRestInterceptor(),
    )
    client = ForwardingRulesClient(transport=transport)
    with mock.patch.object(
        type(client.transport._session), "request"
    ) as req, mock.patch.object(
        path_template, "transcode"
    ) as transcode, mock.patch.object(
        transports.ForwardingRulesRestInterceptor, "post_patch"
    ) as post, mock.patch.object(
        transports.ForwardingRulesRestInterceptor, "pre_patch"
    ) as pre:
        pre.assert_not_called()
        post.assert_not_called()

        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": None,
            "query_params": {},
        }

        req.return_value = Response()
        req.return_value.status_code = 200
        req.return_value.request = PreparedRequest()
        req.return_value._content = compute.Operation.to_json(compute.Operation())

        request = compute.PatchForwardingRuleRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = compute.Operation

        client.patch_unary(request, metadata=[("key", "val"), ("cephalopod", "squid"),])

        pre.assert_called_once()
        post.assert_called_once()


def test_patch_unary_rest_bad_request(
    transport: str = "rest", request_type=compute.PatchForwardingRuleRequest
):
    client = ForwardingRulesClient(
        credentials=ga_credentials.AnonymousCredentials(), transport=transport,
    )

    # send a request that will satisfy transcoding
    request_init = {
        "project": "sample1",
        "region": "sample2",
        "forwarding_rule": "sample3",
    }
    request_init["forwarding_rule_resource"] = {
        "I_p_address": "I_p_address_value",
        "I_p_protocol": "I_p_protocol_value",
        "all_ports": True,
        "allow_global_access": True,
        "backend_service": "backend_service_value",
        "creation_timestamp": "creation_timestamp_value",
        "description": "description_value",
        "fingerprint": "fingerprint_value",
        "id": 205,
        "ip_version": "ip_version_value",
        "is_mirroring_collector": True,
        "kind": "kind_value",
        "label_fingerprint": "label_fingerprint_value",
        "labels": {},
        "load_balancing_scheme": "load_balancing_scheme_value",
        "metadata_filters": [
            {
                "filter_labels": [{"name": "name_value", "value": "value_value"}],
                "filter_match_criteria": "filter_match_criteria_value",
            }
        ],
        "name": "name_value",
        "network": "network_value",
        "network_tier": "network_tier_value",
        "port_range": "port_range_value",
        "ports": ["ports_value_1", "ports_value_2"],
        "psc_connection_id": 1793,
        "psc_connection_status": "psc_connection_status_value",
        "region": "region_value",
        "self_link": "self_link_value",
        "service_directory_registrations": [
            {
                "namespace": "namespace_value",
                "service": "service_value",
                "service_directory_region": "service_directory_region_value",
            }
        ],
        "service_label": "service_label_value",
        "service_name": "service_name_value",
        "subnetwork": "subnetwork_value",
        "target": "target_value",
    }
    request = request_type(request_init)

    # Mock the http request call within the method and fake a BadRequest error.
    with mock.patch.object(Session, "request") as req, pytest.raises(
        core_exceptions.BadRequest
    ):
        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 400
        response_value.request = Request()
        req.return_value = response_value
        client.patch_unary(request)


def test_patch_unary_rest_flattened():
    client = ForwardingRulesClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = compute.Operation()

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "project": "sample1",
            "region": "sample2",
            "forwarding_rule": "sample3",
        }

        # get truthy value for each flattened field
        mock_args = dict(
            project="project_value",
            region="region_value",
            forwarding_rule="forwarding_rule_value",
            forwarding_rule_resource=compute.ForwardingRule(
                I_p_address="I_p_address_value"
            ),
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        json_return_value = compute.Operation.to_json(return_value)

        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value

        client.patch_unary(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/compute/v1/projects/{project}/regions/{region}/forwardingRules/{forwarding_rule}"
            % client.transport._host,
            args[1],
        )


def test_patch_unary_rest_flattened_error(transport: str = "rest"):
    client = ForwardingRulesClient(
        credentials=ga_credentials.AnonymousCredentials(), transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.patch_unary(
            compute.PatchForwardingRuleRequest(),
            project="project_value",
            region="region_value",
            forwarding_rule="forwarding_rule_value",
            forwarding_rule_resource=compute.ForwardingRule(
                I_p_address="I_p_address_value"
            ),
        )


def test_patch_unary_rest_error():
    client = ForwardingRulesClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )


@pytest.mark.parametrize(
    "request_type", [compute.SetLabelsForwardingRuleRequest, dict,]
)
def test_set_labels_unary_rest(request_type):
    client = ForwardingRulesClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest",
    )

    # send a request that will satisfy transcoding
    request_init = {"project": "sample1", "region": "sample2", "resource": "sample3"}
    request_init["region_set_labels_request_resource"] = {
        "label_fingerprint": "label_fingerprint_value",
        "labels": {},
    }
    request = request_type(request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = compute.Operation(
            client_operation_id="client_operation_id_value",
            creation_timestamp="creation_timestamp_value",
            description="description_value",
            end_time="end_time_value",
            http_error_message="http_error_message_value",
            http_error_status_code=2374,
            id=205,
            insert_time="insert_time_value",
            kind="kind_value",
            name="name_value",
            operation_group_id="operation_group_id_value",
            operation_type="operation_type_value",
            progress=885,
            region="region_value",
            self_link="self_link_value",
            start_time="start_time_value",
            status=compute.Operation.Status.DONE,
            status_message="status_message_value",
            target_id=947,
            target_link="target_link_value",
            user="user_value",
            zone="zone_value",
        )

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        json_return_value = compute.Operation.to_json(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        response = client.set_labels_unary(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, compute.Operation)
    assert response.client_operation_id == "client_operation_id_value"
    assert response.creation_timestamp == "creation_timestamp_value"
    assert response.description == "description_value"
    assert response.end_time == "end_time_value"
    assert response.http_error_message == "http_error_message_value"
    assert response.http_error_status_code == 2374
    assert response.id == 205
    assert response.insert_time == "insert_time_value"
    assert response.kind == "kind_value"
    assert response.name == "name_value"
    assert response.operation_group_id == "operation_group_id_value"
    assert response.operation_type == "operation_type_value"
    assert response.progress == 885
    assert response.region == "region_value"
    assert response.self_link == "self_link_value"
    assert response.start_time == "start_time_value"
    assert response.status == compute.Operation.Status.DONE
    assert response.status_message == "status_message_value"
    assert response.target_id == 947
    assert response.target_link == "target_link_value"
    assert response.user == "user_value"
    assert response.zone == "zone_value"


def test_set_labels_unary_rest_required_fields(
    request_type=compute.SetLabelsForwardingRuleRequest,
):
    transport_class = transports.ForwardingRulesRestTransport

    request_init = {}
    request_init["project"] = ""
    request_init["region"] = ""
    request_init["resource"] = ""
    request = request_type(request_init)
    jsonified_request = json.loads(
        request_type.to_json(
            request, including_default_value_fields=False, use_integers_for_enums=False
        )
    )

    # verify fields with default values are dropped

    unset_fields = transport_class(
        credentials=ga_credentials.AnonymousCredentials()
    ).set_labels._get_unset_required_fields(jsonified_request)
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["project"] = "project_value"
    jsonified_request["region"] = "region_value"
    jsonified_request["resource"] = "resource_value"

    unset_fields = transport_class(
        credentials=ga_credentials.AnonymousCredentials()
    ).set_labels._get_unset_required_fields(jsonified_request)
    # Check that path parameters and body parameters are not mixing in.
    assert not set(unset_fields) - set(("request_id",))
    jsonified_request.update(unset_fields)

    # verify required fields with non-default values are left alone
    assert "project" in jsonified_request
    assert jsonified_request["project"] == "project_value"
    assert "region" in jsonified_request
    assert jsonified_request["region"] == "region_value"
    assert "resource" in jsonified_request
    assert jsonified_request["resource"] == "resource_value"

    client = ForwardingRulesClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest",
    )
    request = request_type(request_init)

    # Designate an appropriate value for the returned response.
    return_value = compute.Operation()
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # We need to mock transcode() because providing default values
        # for required fields will fail the real version if the http_options
        # expect actual values for those fields.
        with mock.patch.object(path_template, "transcode") as transcode:
            # A uri without fields and an empty body will force all the
            # request fields to show up in the query_params.
            transcode_result = {
                "uri": "v1/sample_method",
                "method": "post",
                "query_params": request_init,
            }
            transcode_result["body"] = {}
            transcode.return_value = transcode_result

            response_value = Response()
            response_value.status_code = 200
            json_return_value = compute.Operation.to_json(return_value)
            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value

            response = client.set_labels_unary(request)

            expected_params = []
            actual_params = req.call_args.kwargs["params"]
            assert expected_params == actual_params


def test_set_labels_unary_rest_unset_required_fields():
    transport = transports.ForwardingRulesRestTransport(
        credentials=ga_credentials.AnonymousCredentials
    )

    unset_fields = transport.set_labels._get_unset_required_fields({})
    assert set(unset_fields) == (
        set(("requestId",))
        & set(("project", "region", "regionSetLabelsRequestResource", "resource",))
    )


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_set_labels_unary_rest_interceptors(null_interceptor):
    transport = transports.ForwardingRulesRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.ForwardingRulesRestInterceptor(),
    )
    client = ForwardingRulesClient(transport=transport)
    with mock.patch.object(
        type(client.transport._session), "request"
    ) as req, mock.patch.object(
        path_template, "transcode"
    ) as transcode, mock.patch.object(
        transports.ForwardingRulesRestInterceptor, "post_set_labels"
    ) as post, mock.patch.object(
        transports.ForwardingRulesRestInterceptor, "pre_set_labels"
    ) as pre:
        pre.assert_not_called()
        post.assert_not_called()

        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": None,
            "query_params": {},
        }

        req.return_value = Response()
        req.return_value.status_code = 200
        req.return_value.request = PreparedRequest()
        req.return_value._content = compute.Operation.to_json(compute.Operation())

        request = compute.SetLabelsForwardingRuleRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = compute.Operation

        client.set_labels_unary(
            request, metadata=[("key", "val"), ("cephalopod", "squid"),]
        )

        pre.assert_called_once()
        post.assert_called_once()


def test_set_labels_unary_rest_bad_request(
    transport: str = "rest", request_type=compute.SetLabelsForwardingRuleRequest
):
    client = ForwardingRulesClient(
        credentials=ga_credentials.AnonymousCredentials(), transport=transport,
    )

    # send a request that will satisfy transcoding
    request_init = {"project": "sample1", "region": "sample2", "resource": "sample3"}
    request_init["region_set_labels_request_resource"] = {
        "label_fingerprint": "label_fingerprint_value",
        "labels": {},
    }
    request = request_type(request_init)

    # Mock the http request call within the method and fake a BadRequest error.
    with mock.patch.object(Session, "request") as req, pytest.raises(
        core_exceptions.BadRequest
    ):
        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 400
        response_value.request = Request()
        req.return_value = response_value
        client.set_labels_unary(request)


def test_set_labels_unary_rest_flattened():
    client = ForwardingRulesClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = compute.Operation()

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "project": "sample1",
            "region": "sample2",
            "resource": "sample3",
        }

        # get truthy value for each flattened field
        mock_args = dict(
            project="project_value",
            region="region_value",
            resource="resource_value",
            region_set_labels_request_resource=compute.RegionSetLabelsRequest(
                label_fingerprint="label_fingerprint_value"
            ),
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        json_return_value = compute.Operation.to_json(return_value)

        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value

        client.set_labels_unary(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/compute/v1/projects/{project}/regions/{region}/forwardingRules/{resource}/setLabels"
            % client.transport._host,
            args[1],
        )


def test_set_labels_unary_rest_flattened_error(transport: str = "rest"):
    client = ForwardingRulesClient(
        credentials=ga_credentials.AnonymousCredentials(), transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.set_labels_unary(
            compute.SetLabelsForwardingRuleRequest(),
            project="project_value",
            region="region_value",
            resource="resource_value",
            region_set_labels_request_resource=compute.RegionSetLabelsRequest(
                label_fingerprint="label_fingerprint_value"
            ),
        )


def test_set_labels_unary_rest_error():
    client = ForwardingRulesClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )


@pytest.mark.parametrize(
    "request_type", [compute.SetTargetForwardingRuleRequest, dict,]
)
def test_set_target_unary_rest(request_type):
    client = ForwardingRulesClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest",
    )

    # send a request that will satisfy transcoding
    request_init = {
        "project": "sample1",
        "region": "sample2",
        "forwarding_rule": "sample3",
    }
    request_init["target_reference_resource"] = {"target": "target_value"}
    request = request_type(request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = compute.Operation(
            client_operation_id="client_operation_id_value",
            creation_timestamp="creation_timestamp_value",
            description="description_value",
            end_time="end_time_value",
            http_error_message="http_error_message_value",
            http_error_status_code=2374,
            id=205,
            insert_time="insert_time_value",
            kind="kind_value",
            name="name_value",
            operation_group_id="operation_group_id_value",
            operation_type="operation_type_value",
            progress=885,
            region="region_value",
            self_link="self_link_value",
            start_time="start_time_value",
            status=compute.Operation.Status.DONE,
            status_message="status_message_value",
            target_id=947,
            target_link="target_link_value",
            user="user_value",
            zone="zone_value",
        )

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        json_return_value = compute.Operation.to_json(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        response = client.set_target_unary(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, compute.Operation)
    assert response.client_operation_id == "client_operation_id_value"
    assert response.creation_timestamp == "creation_timestamp_value"
    assert response.description == "description_value"
    assert response.end_time == "end_time_value"
    assert response.http_error_message == "http_error_message_value"
    assert response.http_error_status_code == 2374
    assert response.id == 205
    assert response.insert_time == "insert_time_value"
    assert response.kind == "kind_value"
    assert response.name == "name_value"
    assert response.operation_group_id == "operation_group_id_value"
    assert response.operation_type == "operation_type_value"
    assert response.progress == 885
    assert response.region == "region_value"
    assert response.self_link == "self_link_value"
    assert response.start_time == "start_time_value"
    assert response.status == compute.Operation.Status.DONE
    assert response.status_message == "status_message_value"
    assert response.target_id == 947
    assert response.target_link == "target_link_value"
    assert response.user == "user_value"
    assert response.zone == "zone_value"


def test_set_target_unary_rest_required_fields(
    request_type=compute.SetTargetForwardingRuleRequest,
):
    transport_class = transports.ForwardingRulesRestTransport

    request_init = {}
    request_init["forwarding_rule"] = ""
    request_init["project"] = ""
    request_init["region"] = ""
    request = request_type(request_init)
    jsonified_request = json.loads(
        request_type.to_json(
            request, including_default_value_fields=False, use_integers_for_enums=False
        )
    )

    # verify fields with default values are dropped

    unset_fields = transport_class(
        credentials=ga_credentials.AnonymousCredentials()
    ).set_target._get_unset_required_fields(jsonified_request)
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["forwardingRule"] = "forwarding_rule_value"
    jsonified_request["project"] = "project_value"
    jsonified_request["region"] = "region_value"

    unset_fields = transport_class(
        credentials=ga_credentials.AnonymousCredentials()
    ).set_target._get_unset_required_fields(jsonified_request)
    # Check that path parameters and body parameters are not mixing in.
    assert not set(unset_fields) - set(("request_id",))
    jsonified_request.update(unset_fields)

    # verify required fields with non-default values are left alone
    assert "forwardingRule" in jsonified_request
    assert jsonified_request["forwardingRule"] == "forwarding_rule_value"
    assert "project" in jsonified_request
    assert jsonified_request["project"] == "project_value"
    assert "region" in jsonified_request
    assert jsonified_request["region"] == "region_value"

    client = ForwardingRulesClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest",
    )
    request = request_type(request_init)

    # Designate an appropriate value for the returned response.
    return_value = compute.Operation()
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # We need to mock transcode() because providing default values
        # for required fields will fail the real version if the http_options
        # expect actual values for those fields.
        with mock.patch.object(path_template, "transcode") as transcode:
            # A uri without fields and an empty body will force all the
            # request fields to show up in the query_params.
            transcode_result = {
                "uri": "v1/sample_method",
                "method": "post",
                "query_params": request_init,
            }
            transcode_result["body"] = {}
            transcode.return_value = transcode_result

            response_value = Response()
            response_value.status_code = 200
            json_return_value = compute.Operation.to_json(return_value)
            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value

            response = client.set_target_unary(request)

            expected_params = []
            actual_params = req.call_args.kwargs["params"]
            assert expected_params == actual_params


def test_set_target_unary_rest_unset_required_fields():
    transport = transports.ForwardingRulesRestTransport(
        credentials=ga_credentials.AnonymousCredentials
    )

    unset_fields = transport.set_target._get_unset_required_fields({})
    assert set(unset_fields) == (
        set(("requestId",))
        & set(("forwardingRule", "project", "region", "targetReferenceResource",))
    )


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_set_target_unary_rest_interceptors(null_interceptor):
    transport = transports.ForwardingRulesRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.ForwardingRulesRestInterceptor(),
    )
    client = ForwardingRulesClient(transport=transport)
    with mock.patch.object(
        type(client.transport._session), "request"
    ) as req, mock.patch.object(
        path_template, "transcode"
    ) as transcode, mock.patch.object(
        transports.ForwardingRulesRestInterceptor, "post_set_target"
    ) as post, mock.patch.object(
        transports.ForwardingRulesRestInterceptor, "pre_set_target"
    ) as pre:
        pre.assert_not_called()
        post.assert_not_called()

        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": None,
            "query_params": {},
        }

        req.return_value = Response()
        req.return_value.status_code = 200
        req.return_value.request = PreparedRequest()
        req.return_value._content = compute.Operation.to_json(compute.Operation())

        request = compute.SetTargetForwardingRuleRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = compute.Operation

        client.set_target_unary(
            request, metadata=[("key", "val"), ("cephalopod", "squid"),]
        )

        pre.assert_called_once()
        post.assert_called_once()


def test_set_target_unary_rest_bad_request(
    transport: str = "rest", request_type=compute.SetTargetForwardingRuleRequest
):
    client = ForwardingRulesClient(
        credentials=ga_credentials.AnonymousCredentials(), transport=transport,
    )

    # send a request that will satisfy transcoding
    request_init = {
        "project": "sample1",
        "region": "sample2",
        "forwarding_rule": "sample3",
    }
    request_init["target_reference_resource"] = {"target": "target_value"}
    request = request_type(request_init)

    # Mock the http request call within the method and fake a BadRequest error.
    with mock.patch.object(Session, "request") as req, pytest.raises(
        core_exceptions.BadRequest
    ):
        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 400
        response_value.request = Request()
        req.return_value = response_value
        client.set_target_unary(request)


def test_set_target_unary_rest_flattened():
    client = ForwardingRulesClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = compute.Operation()

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "project": "sample1",
            "region": "sample2",
            "forwarding_rule": "sample3",
        }

        # get truthy value for each flattened field
        mock_args = dict(
            project="project_value",
            region="region_value",
            forwarding_rule="forwarding_rule_value",
            target_reference_resource=compute.TargetReference(target="target_value"),
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        json_return_value = compute.Operation.to_json(return_value)

        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value

        client.set_target_unary(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/compute/v1/projects/{project}/regions/{region}/forwardingRules/{forwarding_rule}/setTarget"
            % client.transport._host,
            args[1],
        )


def test_set_target_unary_rest_flattened_error(transport: str = "rest"):
    client = ForwardingRulesClient(
        credentials=ga_credentials.AnonymousCredentials(), transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.set_target_unary(
            compute.SetTargetForwardingRuleRequest(),
            project="project_value",
            region="region_value",
            forwarding_rule="forwarding_rule_value",
            target_reference_resource=compute.TargetReference(target="target_value"),
        )


def test_set_target_unary_rest_error():
    client = ForwardingRulesClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )


def test_credentials_transport_error():
    # It is an error to provide credentials and a transport instance.
    transport = transports.ForwardingRulesRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = ForwardingRulesClient(
            credentials=ga_credentials.AnonymousCredentials(), transport=transport,
        )

    # It is an error to provide a credentials file and a transport instance.
    transport = transports.ForwardingRulesRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = ForwardingRulesClient(
            client_options={"credentials_file": "credentials.json"},
            transport=transport,
        )

    # It is an error to provide an api_key and a transport instance.
    transport = transports.ForwardingRulesRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    options = client_options.ClientOptions()
    options.api_key = "api_key"
    with pytest.raises(ValueError):
        client = ForwardingRulesClient(client_options=options, transport=transport,)

    # It is an error to provide an api_key and a credential.
    options = mock.Mock()
    options.api_key = "api_key"
    with pytest.raises(ValueError):
        client = ForwardingRulesClient(
            client_options=options, credentials=ga_credentials.AnonymousCredentials()
        )

    # It is an error to provide scopes and a transport instance.
    transport = transports.ForwardingRulesRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = ForwardingRulesClient(
            client_options={"scopes": ["1", "2"]}, transport=transport,
        )


def test_transport_instance():
    # A client may be instantiated with a custom transport instance.
    transport = transports.ForwardingRulesRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    client = ForwardingRulesClient(transport=transport)
    assert client.transport is transport


@pytest.mark.parametrize("transport_class", [transports.ForwardingRulesRestTransport,])
def test_transport_adc(transport_class):
    # Test default credentials are used if not provided.
    with mock.patch.object(google.auth, "default") as adc:
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport_class()
        adc.assert_called_once()


def test_forwarding_rules_base_transport_error():
    # Passing both a credentials object and credentials_file should raise an error
    with pytest.raises(core_exceptions.DuplicateCredentialArgs):
        transport = transports.ForwardingRulesTransport(
            credentials=ga_credentials.AnonymousCredentials(),
            credentials_file="credentials.json",
        )


def test_forwarding_rules_base_transport():
    # Instantiate the base transport.
    with mock.patch(
        "google.cloud.compute_v1.services.forwarding_rules.transports.ForwardingRulesTransport.__init__"
    ) as Transport:
        Transport.return_value = None
        transport = transports.ForwardingRulesTransport(
            credentials=ga_credentials.AnonymousCredentials(),
        )

    # Every method on the transport should just blindly
    # raise NotImplementedError.
    methods = (
        "aggregated_list",
        "delete",
        "get",
        "insert",
        "list",
        "patch",
        "set_labels",
        "set_target",
    )
    for method in methods:
        with pytest.raises(NotImplementedError):
            getattr(transport, method)(request=object())

    with pytest.raises(NotImplementedError):
        transport.close()


def test_forwarding_rules_base_transport_with_credentials_file():
    # Instantiate the base transport with a credentials file
    with mock.patch.object(
        google.auth, "load_credentials_from_file", autospec=True
    ) as load_creds, mock.patch(
        "google.cloud.compute_v1.services.forwarding_rules.transports.ForwardingRulesTransport._prep_wrapped_messages"
    ) as Transport:
        Transport.return_value = None
        load_creds.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport = transports.ForwardingRulesTransport(
            credentials_file="credentials.json", quota_project_id="octopus",
        )
        load_creds.assert_called_once_with(
            "credentials.json",
            scopes=None,
            default_scopes=(
                "https://www.googleapis.com/auth/compute",
                "https://www.googleapis.com/auth/cloud-platform",
            ),
            quota_project_id="octopus",
        )


def test_forwarding_rules_base_transport_with_adc():
    # Test the default credentials are used if credentials and credentials_file are None.
    with mock.patch.object(google.auth, "default", autospec=True) as adc, mock.patch(
        "google.cloud.compute_v1.services.forwarding_rules.transports.ForwardingRulesTransport._prep_wrapped_messages"
    ) as Transport:
        Transport.return_value = None
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport = transports.ForwardingRulesTransport()
        adc.assert_called_once()


def test_forwarding_rules_auth_adc():
    # If no credentials are provided, we should use ADC credentials.
    with mock.patch.object(google.auth, "default", autospec=True) as adc:
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        ForwardingRulesClient()
        adc.assert_called_once_with(
            scopes=None,
            default_scopes=(
                "https://www.googleapis.com/auth/compute",
                "https://www.googleapis.com/auth/cloud-platform",
            ),
            quota_project_id=None,
        )


def test_forwarding_rules_http_transport_client_cert_source_for_mtls():
    cred = ga_credentials.AnonymousCredentials()
    with mock.patch(
        "google.auth.transport.requests.AuthorizedSession.configure_mtls_channel"
    ) as mock_configure_mtls_channel:
        transports.ForwardingRulesRestTransport(
            credentials=cred, client_cert_source_for_mtls=client_cert_source_callback
        )
        mock_configure_mtls_channel.assert_called_once_with(client_cert_source_callback)


@pytest.mark.parametrize("transport_name", ["rest",])
def test_forwarding_rules_host_no_port(transport_name):
    client = ForwardingRulesClient(
        credentials=ga_credentials.AnonymousCredentials(),
        client_options=client_options.ClientOptions(
            api_endpoint="compute.googleapis.com"
        ),
        transport=transport_name,
    )
    assert client.transport._host == (
        "compute.googleapis.com:443"
        if transport_name in ["grpc", "grpc_asyncio"]
        else "https://compute.googleapis.com"
    )


@pytest.mark.parametrize("transport_name", ["rest",])
def test_forwarding_rules_host_with_port(transport_name):
    client = ForwardingRulesClient(
        credentials=ga_credentials.AnonymousCredentials(),
        client_options=client_options.ClientOptions(
            api_endpoint="compute.googleapis.com:8000"
        ),
        transport=transport_name,
    )
    assert client.transport._host == (
        "compute.googleapis.com:8000"
        if transport_name in ["grpc", "grpc_asyncio"]
        else "https://compute.googleapis.com:8000"
    )


def test_common_billing_account_path():
    billing_account = "squid"
    expected = "billingAccounts/{billing_account}".format(
        billing_account=billing_account,
    )
    actual = ForwardingRulesClient.common_billing_account_path(billing_account)
    assert expected == actual


def test_parse_common_billing_account_path():
    expected = {
        "billing_account": "clam",
    }
    path = ForwardingRulesClient.common_billing_account_path(**expected)

    # Check that the path construction is reversible.
    actual = ForwardingRulesClient.parse_common_billing_account_path(path)
    assert expected == actual


def test_common_folder_path():
    folder = "whelk"
    expected = "folders/{folder}".format(folder=folder,)
    actual = ForwardingRulesClient.common_folder_path(folder)
    assert expected == actual


def test_parse_common_folder_path():
    expected = {
        "folder": "octopus",
    }
    path = ForwardingRulesClient.common_folder_path(**expected)

    # Check that the path construction is reversible.
    actual = ForwardingRulesClient.parse_common_folder_path(path)
    assert expected == actual


def test_common_organization_path():
    organization = "oyster"
    expected = "organizations/{organization}".format(organization=organization,)
    actual = ForwardingRulesClient.common_organization_path(organization)
    assert expected == actual


def test_parse_common_organization_path():
    expected = {
        "organization": "nudibranch",
    }
    path = ForwardingRulesClient.common_organization_path(**expected)

    # Check that the path construction is reversible.
    actual = ForwardingRulesClient.parse_common_organization_path(path)
    assert expected == actual


def test_common_project_path():
    project = "cuttlefish"
    expected = "projects/{project}".format(project=project,)
    actual = ForwardingRulesClient.common_project_path(project)
    assert expected == actual


def test_parse_common_project_path():
    expected = {
        "project": "mussel",
    }
    path = ForwardingRulesClient.common_project_path(**expected)

    # Check that the path construction is reversible.
    actual = ForwardingRulesClient.parse_common_project_path(path)
    assert expected == actual


def test_common_location_path():
    project = "winkle"
    location = "nautilus"
    expected = "projects/{project}/locations/{location}".format(
        project=project, location=location,
    )
    actual = ForwardingRulesClient.common_location_path(project, location)
    assert expected == actual


def test_parse_common_location_path():
    expected = {
        "project": "scallop",
        "location": "abalone",
    }
    path = ForwardingRulesClient.common_location_path(**expected)

    # Check that the path construction is reversible.
    actual = ForwardingRulesClient.parse_common_location_path(path)
    assert expected == actual


def test_client_with_default_client_info():
    client_info = gapic_v1.client_info.ClientInfo()

    with mock.patch.object(
        transports.ForwardingRulesTransport, "_prep_wrapped_messages"
    ) as prep:
        client = ForwardingRulesClient(
            credentials=ga_credentials.AnonymousCredentials(), client_info=client_info,
        )
        prep.assert_called_once_with(client_info)

    with mock.patch.object(
        transports.ForwardingRulesTransport, "_prep_wrapped_messages"
    ) as prep:
        transport_class = ForwardingRulesClient.get_transport_class()
        transport = transport_class(
            credentials=ga_credentials.AnonymousCredentials(), client_info=client_info,
        )
        prep.assert_called_once_with(client_info)


def test_transport_close():
    transports = {
        "rest": "_session",
    }

    for transport, close_name in transports.items():
        client = ForwardingRulesClient(
            credentials=ga_credentials.AnonymousCredentials(), transport=transport
        )
        with mock.patch.object(
            type(getattr(client.transport, close_name)), "close"
        ) as close:
            with client:
                close.assert_not_called()
            close.assert_called_once()


def test_client_ctx():
    transports = [
        "rest",
    ]
    for transport in transports:
        client = ForwardingRulesClient(
            credentials=ga_credentials.AnonymousCredentials(), transport=transport
        )
        # Test client calls underlying transport.
        with mock.patch.object(type(client.transport), "close") as close:
            close.assert_not_called()
            with client:
                pass
            close.assert_called()


@pytest.mark.parametrize(
    "client_class,transport_class",
    [(ForwardingRulesClient, transports.ForwardingRulesRestTransport),],
)
def test_api_key_credentials(client_class, transport_class):
    with mock.patch.object(
        google.auth._default, "get_api_key_credentials", create=True
    ) as get_api_key_credentials:
        mock_cred = mock.Mock()
        get_api_key_credentials.return_value = mock_cred
        options = client_options.ClientOptions()
        options.api_key = "api_key"
        with mock.patch.object(transport_class, "__init__") as patched:
            patched.return_value = None
            client = client_class(client_options=options)
            patched.assert_called_once_with(
                credentials=mock_cred,
                credentials_file=None,
                host=client.DEFAULT_ENDPOINT,
                scopes=None,
                client_cert_source_for_mtls=None,
                quota_project_id=None,
                client_info=transports.base.DEFAULT_CLIENT_INFO,
                always_use_jwt_access=True,
            )
