# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ZoneTransferServer(object):
    """
    An OCI nameserver that transfers zone data with external nameservers.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ZoneTransferServer object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param address:
            The value to assign to the address property of this ZoneTransferServer.
        :type address: str

        :param port:
            The value to assign to the port property of this ZoneTransferServer.
        :type port: int

        :param is_transfer_source:
            The value to assign to the is_transfer_source property of this ZoneTransferServer.
        :type is_transfer_source: bool

        :param is_transfer_destination:
            The value to assign to the is_transfer_destination property of this ZoneTransferServer.
        :type is_transfer_destination: bool

        """
        self.swagger_types = {
            'address': 'str',
            'port': 'int',
            'is_transfer_source': 'bool',
            'is_transfer_destination': 'bool'
        }

        self.attribute_map = {
            'address': 'address',
            'port': 'port',
            'is_transfer_source': 'isTransferSource',
            'is_transfer_destination': 'isTransferDestination'
        }

        self._address = None
        self._port = None
        self._is_transfer_source = None
        self._is_transfer_destination = None

    @property
    def address(self):
        """
        **[Required]** Gets the address of this ZoneTransferServer.
        The server's IP address (IPv4 or IPv6).


        :return: The address of this ZoneTransferServer.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """
        Sets the address of this ZoneTransferServer.
        The server's IP address (IPv4 or IPv6).


        :param address: The address of this ZoneTransferServer.
        :type: str
        """
        self._address = address

    @property
    def port(self):
        """
        Gets the port of this ZoneTransferServer.
        The server's port.


        :return: The port of this ZoneTransferServer.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """
        Sets the port of this ZoneTransferServer.
        The server's port.


        :param port: The port of this ZoneTransferServer.
        :type: int
        """
        self._port = port

    @property
    def is_transfer_source(self):
        """
        Gets the is_transfer_source of this ZoneTransferServer.
        A Boolean flag indicating whether or not the server is a zone data transfer source.


        :return: The is_transfer_source of this ZoneTransferServer.
        :rtype: bool
        """
        return self._is_transfer_source

    @is_transfer_source.setter
    def is_transfer_source(self, is_transfer_source):
        """
        Sets the is_transfer_source of this ZoneTransferServer.
        A Boolean flag indicating whether or not the server is a zone data transfer source.


        :param is_transfer_source: The is_transfer_source of this ZoneTransferServer.
        :type: bool
        """
        self._is_transfer_source = is_transfer_source

    @property
    def is_transfer_destination(self):
        """
        Gets the is_transfer_destination of this ZoneTransferServer.
        A Boolean flag indicating whether or not the server is a zone data transfer destination.


        :return: The is_transfer_destination of this ZoneTransferServer.
        :rtype: bool
        """
        return self._is_transfer_destination

    @is_transfer_destination.setter
    def is_transfer_destination(self, is_transfer_destination):
        """
        Sets the is_transfer_destination of this ZoneTransferServer.
        A Boolean flag indicating whether or not the server is a zone data transfer destination.


        :param is_transfer_destination: The is_transfer_destination of this ZoneTransferServer.
        :type: bool
        """
        self._is_transfer_destination = is_transfer_destination

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
