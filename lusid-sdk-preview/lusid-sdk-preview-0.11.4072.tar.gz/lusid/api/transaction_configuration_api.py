# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.4072
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from lusid.api_client import ApiClient
from lusid.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)
from lusid.models.lusid_problem_details import LusidProblemDetails
from lusid.models.lusid_validation_problem_details import LusidValidationProblemDetails
from lusid.models.transaction_type import TransactionType


class TransactionConfigurationApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_transaction_type(self, source, type, **kwargs):  # noqa: E501
        """[EXPERIMENTAL] GetTransactionType: Get a single transaction configuration type  # noqa: E501

        Get a single transaction type. Returns failure if not found  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_transaction_type(source, type, async_req=True)
        >>> result = thread.get()

        :param source: The source that the type is in (required)
        :type source: str
        :param type: One of the type's aliases (required)
        :type type: str
        :param as_at: The asAt datetime at which to retrieve the transaction configuration.              Defaults to returning the latest version of the transaction configuration type if not specified
        :type as_at: datetime
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: TransactionType
        """
        kwargs['_return_http_data_only'] = True
        return self.get_transaction_type_with_http_info(source, type, **kwargs)  # noqa: E501

    def get_transaction_type_with_http_info(self, source, type, **kwargs):  # noqa: E501
        """[EXPERIMENTAL] GetTransactionType: Get a single transaction configuration type  # noqa: E501

        Get a single transaction type. Returns failure if not found  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_transaction_type_with_http_info(source, type, async_req=True)
        >>> result = thread.get()

        :param source: The source that the type is in (required)
        :type source: str
        :param type: One of the type's aliases (required)
        :type type: str
        :param as_at: The asAt datetime at which to retrieve the transaction configuration.              Defaults to returning the latest version of the transaction configuration type if not specified
        :type as_at: datetime
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object, the HTTP status code, and the headers.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: (TransactionType, int, HTTPHeaderDict)
        """

        local_var_params = locals()

        all_params = [
            'source',
            'type',
            'as_at'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_headers'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_transaction_type" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        if self.api_client.client_side_validation and ('source' in local_var_params and  # noqa: E501
                                                        len(local_var_params['source']) > 64):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `source` when calling `get_transaction_type`, length must be less than or equal to `64`")  # noqa: E501
        if self.api_client.client_side_validation and ('source' in local_var_params and  # noqa: E501
                                                        len(local_var_params['source']) < 1):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `source` when calling `get_transaction_type`, length must be greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and 'source' in local_var_params and not re.search(r'^[a-zA-Z0-9\-_]+$', local_var_params['source']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `source` when calling `get_transaction_type`, must conform to the pattern `/^[a-zA-Z0-9\-_]+$/`")  # noqa: E501
        if self.api_client.client_side_validation and ('type' in local_var_params and  # noqa: E501
                                                        len(local_var_params['type']) > 64):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `type` when calling `get_transaction_type`, length must be less than or equal to `64`")  # noqa: E501
        if self.api_client.client_side_validation and ('type' in local_var_params and  # noqa: E501
                                                        len(local_var_params['type']) < 1):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `type` when calling `get_transaction_type`, length must be greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and 'type' in local_var_params and not re.search(r'^[a-zA-Z0-9\-_]+$', local_var_params['type']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `type` when calling `get_transaction_type`, must conform to the pattern `/^[a-zA-Z0-9\-_]+$/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'source' in local_var_params:
            path_params['source'] = local_var_params['source']  # noqa: E501
        if 'type' in local_var_params:
            path_params['type'] = local_var_params['type']  # noqa: E501

        query_params = []
        if 'as_at' in local_var_params and local_var_params['as_at'] is not None:  # noqa: E501
            query_params.append(('asAt', local_var_params['as_at']))  # noqa: E501

        header_params = dict(local_var_params.get('_headers', {}))

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        header_params['Accept-Encoding'] = "gzip, deflate, br"


        # set the LUSID header
        header_params['X-LUSID-SDK-Language'] = 'Python'
        header_params['X-LUSID-SDK-Version'] = '0.11.4072'

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        response_types_map = {
            200: "TransactionType",
            400: "LusidValidationProblemDetails",
        }

        return self.api_client.call_api(
            '/api/transactionconfiguration/types/{source}/{type}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))
