# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ResponseCacheRespServer(object):
    """
    Details of a RESP based cache store server
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ResponseCacheRespServer object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param host:
            The value to assign to the host property of this ResponseCacheRespServer.
        :type host: str

        :param port:
            The value to assign to the port property of this ResponseCacheRespServer.
        :type port: int

        """
        self.swagger_types = {
            'host': 'str',
            'port': 'int'
        }

        self.attribute_map = {
            'host': 'host',
            'port': 'port'
        }

        self._host = None
        self._port = None

    @property
    def host(self):
        """
        **[Required]** Gets the host of this ResponseCacheRespServer.
        Hostname or IP address (IPv4 only) where the cache store is running.


        :return: The host of this ResponseCacheRespServer.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """
        Sets the host of this ResponseCacheRespServer.
        Hostname or IP address (IPv4 only) where the cache store is running.


        :param host: The host of this ResponseCacheRespServer.
        :type: str
        """
        self._host = host

    @property
    def port(self):
        """
        **[Required]** Gets the port of this ResponseCacheRespServer.
        The port the cache store is exposed on.


        :return: The port of this ResponseCacheRespServer.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """
        Sets the port of this ResponseCacheRespServer.
        The port the cache store is exposed on.


        :param port: The port of this ResponseCacheRespServer.
        :type: int
        """
        self._port = port

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
