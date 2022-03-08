# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class VanityUrlDetails(object):
    """
    Vanity url configuration details.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new VanityUrlDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this VanityUrlDetails.
        :type key: str

        :param description:
            The value to assign to the description property of this VanityUrlDetails.
        :type description: str

        :param urls:
            The value to assign to the urls property of this VanityUrlDetails.
        :type urls: list[str]

        :param hosts:
            The value to assign to the hosts property of this VanityUrlDetails.
        :type hosts: list[str]

        :param public_certificate:
            The value to assign to the public_certificate property of this VanityUrlDetails.
        :type public_certificate: str

        """
        self.swagger_types = {
            'key': 'str',
            'description': 'str',
            'urls': 'list[str]',
            'hosts': 'list[str]',
            'public_certificate': 'str'
        }

        self.attribute_map = {
            'key': 'key',
            'description': 'description',
            'urls': 'urls',
            'hosts': 'hosts',
            'public_certificate': 'publicCertificate'
        }

        self._key = None
        self._description = None
        self._urls = None
        self._hosts = None
        self._public_certificate = None

    @property
    def key(self):
        """
        Gets the key of this VanityUrlDetails.
        The vanity url unique identifier key.


        :return: The key of this VanityUrlDetails.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this VanityUrlDetails.
        The vanity url unique identifier key.


        :param key: The key of this VanityUrlDetails.
        :type: str
        """
        self._key = key

    @property
    def description(self):
        """
        Gets the description of this VanityUrlDetails.
        Description of the vanity url.


        :return: The description of this VanityUrlDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this VanityUrlDetails.
        Description of the vanity url.


        :param description: The description of this VanityUrlDetails.
        :type: str
        """
        self._description = description

    @property
    def urls(self):
        """
        Gets the urls of this VanityUrlDetails.
        List of urls supported by this vanity URL definition (max of 3).


        :return: The urls of this VanityUrlDetails.
        :rtype: list[str]
        """
        return self._urls

    @urls.setter
    def urls(self, urls):
        """
        Sets the urls of this VanityUrlDetails.
        List of urls supported by this vanity URL definition (max of 3).


        :param urls: The urls of this VanityUrlDetails.
        :type: list[str]
        """
        self._urls = urls

    @property
    def hosts(self):
        """
        Gets the hosts of this VanityUrlDetails.
        List of fully qualified hostnames supported by this vanity URL definition (max of 3).


        :return: The hosts of this VanityUrlDetails.
        :rtype: list[str]
        """
        return self._hosts

    @hosts.setter
    def hosts(self, hosts):
        """
        Sets the hosts of this VanityUrlDetails.
        List of fully qualified hostnames supported by this vanity URL definition (max of 3).


        :param hosts: The hosts of this VanityUrlDetails.
        :type: list[str]
        """
        self._hosts = hosts

    @property
    def public_certificate(self):
        """
        Gets the public_certificate of this VanityUrlDetails.
        PEM certificate for HTTPS connections.


        :return: The public_certificate of this VanityUrlDetails.
        :rtype: str
        """
        return self._public_certificate

    @public_certificate.setter
    def public_certificate(self, public_certificate):
        """
        Sets the public_certificate of this VanityUrlDetails.
        PEM certificate for HTTPS connections.


        :param public_certificate: The public_certificate of this VanityUrlDetails.
        :type: str
        """
        self._public_certificate = public_certificate

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
