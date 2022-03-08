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


class Warning(object):
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
        'entity_id': 'str',
        'message': 'str'
    }

    attribute_map = {
        'entity_id': 'entityId',
        'message': 'message'
    }

    required_map = {
        'entity_id': 'required',
        'message': 'required'
    }

    def __init__(self, entity_id=None, message=None, local_vars_configuration=None):  # noqa: E501
        """Warning - a model defined in OpenAPI"
        
        :param entity_id:  (required)
        :type entity_id: str
        :param message:  (required)
        :type message: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._entity_id = None
        self._message = None
        self.discriminator = None

        self.entity_id = entity_id
        self.message = message

    @property
    def entity_id(self):
        """Gets the entity_id of this Warning.  # noqa: E501


        :return: The entity_id of this Warning.  # noqa: E501
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """Sets the entity_id of this Warning.


        :param entity_id: The entity_id of this Warning.  # noqa: E501
        :type entity_id: str
        """
        if self.local_vars_configuration.client_side_validation and entity_id is None:  # noqa: E501
            raise ValueError("Invalid value for `entity_id`, must not be `None`")  # noqa: E501

        self._entity_id = entity_id

    @property
    def message(self):
        """Gets the message of this Warning.  # noqa: E501


        :return: The message of this Warning.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this Warning.


        :param message: The message of this Warning.  # noqa: E501
        :type message: str
        """
        if self.local_vars_configuration.client_side_validation and message is None:  # noqa: E501
            raise ValueError("Invalid value for `message`, must not be `None`")  # noqa: E501

        self._message = message

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
        if not isinstance(other, Warning):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Warning):
            return True

        return self.to_dict() != other.to_dict()
