#!/usr/bin/python
#
# Copyright 2018-2021 Polyaxon, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# coding: utf-8

"""
    Polyaxon SDKs and REST API specification.

    Polyaxon SDKs and REST API specification.  # noqa: E501

    The version of the OpenAPI document: 1.16.0
    Contact: contact@polyaxon.com
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from polyaxon_sdk.configuration import Configuration


class V1User(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'username': 'str',
        'email': 'str',
        'name': 'str',
        'kind': 'str',
        'theme': 'int',
        'organization': 'str'
    }

    attribute_map = {
        'username': 'username',
        'email': 'email',
        'name': 'name',
        'kind': 'kind',
        'theme': 'theme',
        'organization': 'organization'
    }

    def __init__(self, username=None, email=None, name=None, kind=None, theme=None, organization=None, local_vars_configuration=None):  # noqa: E501
        """V1User - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._username = None
        self._email = None
        self._name = None
        self._kind = None
        self._theme = None
        self._organization = None
        self.discriminator = None

        if username is not None:
            self.username = username
        if email is not None:
            self.email = email
        if name is not None:
            self.name = name
        if kind is not None:
            self.kind = kind
        if theme is not None:
            self.theme = theme
        if organization is not None:
            self.organization = organization

    @property
    def username(self):
        """Gets the username of this V1User.  # noqa: E501


        :return: The username of this V1User.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this V1User.


        :param username: The username of this V1User.  # noqa: E501
        :type username: str
        """

        self._username = username

    @property
    def email(self):
        """Gets the email of this V1User.  # noqa: E501


        :return: The email of this V1User.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this V1User.


        :param email: The email of this V1User.  # noqa: E501
        :type email: str
        """

        self._email = email

    @property
    def name(self):
        """Gets the name of this V1User.  # noqa: E501


        :return: The name of this V1User.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V1User.


        :param name: The name of this V1User.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def kind(self):
        """Gets the kind of this V1User.  # noqa: E501


        :return: The kind of this V1User.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this V1User.


        :param kind: The kind of this V1User.  # noqa: E501
        :type kind: str
        """

        self._kind = kind

    @property
    def theme(self):
        """Gets the theme of this V1User.  # noqa: E501


        :return: The theme of this V1User.  # noqa: E501
        :rtype: int
        """
        return self._theme

    @theme.setter
    def theme(self, theme):
        """Sets the theme of this V1User.


        :param theme: The theme of this V1User.  # noqa: E501
        :type theme: int
        """

        self._theme = theme

    @property
    def organization(self):
        """Gets the organization of this V1User.  # noqa: E501


        :return: The organization of this V1User.  # noqa: E501
        :rtype: str
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this V1User.


        :param organization: The organization of this V1User.  # noqa: E501
        :type organization: str
        """

        self._organization = organization

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1User):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1User):
            return True

        return self.to_dict() != other.to_dict()
