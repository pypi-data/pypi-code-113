# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.4072
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from lusid.configuration import Configuration


class FieldDefinition(object):
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
      required_map (dict): The key is attribute name
                           and the value is whether it is 'required' or 'optional'.
    """
    openapi_types = {
        'key': 'str',
        'is_required': 'bool',
        'is_unique': 'bool'
    }

    attribute_map = {
        'key': 'key',
        'is_required': 'isRequired',
        'is_unique': 'isUnique'
    }

    required_map = {
        'key': 'required',
        'is_required': 'required',
        'is_unique': 'required'
    }

    def __init__(self, key=None, is_required=None, is_unique=None, local_vars_configuration=None):  # noqa: E501
        """FieldDefinition - a model defined in OpenAPI"
        
        :param key:  (required)
        :type key: str
        :param is_required:  (required)
        :type is_required: bool
        :param is_unique:  (required)
        :type is_unique: bool

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._key = None
        self._is_required = None
        self._is_unique = None
        self.discriminator = None

        self.key = key
        self.is_required = is_required
        self.is_unique = is_unique

    @property
    def key(self):
        """Gets the key of this FieldDefinition.  # noqa: E501


        :return: The key of this FieldDefinition.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this FieldDefinition.


        :param key: The key of this FieldDefinition.  # noqa: E501
        :type key: str
        """
        if self.local_vars_configuration.client_side_validation and key is None:  # noqa: E501
            raise ValueError("Invalid value for `key`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                key is not None and len(key) > 512):
            raise ValueError("Invalid value for `key`, length must be less than or equal to `512`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                key is not None and len(key) < 1):
            raise ValueError("Invalid value for `key`, length must be greater than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                key is not None and not re.search(r'^[\s\S]*$', key)):  # noqa: E501
            raise ValueError(r"Invalid value for `key`, must be a follow pattern or equal to `/^[\s\S]*$/`")  # noqa: E501

        self._key = key

    @property
    def is_required(self):
        """Gets the is_required of this FieldDefinition.  # noqa: E501


        :return: The is_required of this FieldDefinition.  # noqa: E501
        :rtype: bool
        """
        return self._is_required

    @is_required.setter
    def is_required(self, is_required):
        """Sets the is_required of this FieldDefinition.


        :param is_required: The is_required of this FieldDefinition.  # noqa: E501
        :type is_required: bool
        """
        if self.local_vars_configuration.client_side_validation and is_required is None:  # noqa: E501
            raise ValueError("Invalid value for `is_required`, must not be `None`")  # noqa: E501

        self._is_required = is_required

    @property
    def is_unique(self):
        """Gets the is_unique of this FieldDefinition.  # noqa: E501


        :return: The is_unique of this FieldDefinition.  # noqa: E501
        :rtype: bool
        """
        return self._is_unique

    @is_unique.setter
    def is_unique(self, is_unique):
        """Sets the is_unique of this FieldDefinition.


        :param is_unique: The is_unique of this FieldDefinition.  # noqa: E501
        :type is_unique: bool
        """
        if self.local_vars_configuration.client_side_validation and is_unique is None:  # noqa: E501
            raise ValueError("Invalid value for `is_unique`, must not be `None`")  # noqa: E501

        self._is_unique = is_unique

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
        if not isinstance(other, FieldDefinition):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FieldDefinition):
            return True

        return self.to_dict() != other.to_dict()
