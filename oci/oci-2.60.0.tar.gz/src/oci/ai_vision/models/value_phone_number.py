# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .field_value import FieldValue
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ValuePhoneNumber(FieldValue):
    """
    Phone number field value.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ValuePhoneNumber object with values from keyword arguments. The default value of the :py:attr:`~oci.ai_vision.models.ValuePhoneNumber.value_type` attribute
        of this class is ``PHONE_NUMBER`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param value_type:
            The value to assign to the value_type property of this ValuePhoneNumber.
            Allowed values for this property are: "STRING", "DATE", "TIME", "PHONE_NUMBER", "NUMBER", "INTEGER", "ARRAY"
        :type value_type: str

        :param text:
            The value to assign to the text property of this ValuePhoneNumber.
        :type text: str

        :param confidence:
            The value to assign to the confidence property of this ValuePhoneNumber.
        :type confidence: float

        :param bounding_polygon:
            The value to assign to the bounding_polygon property of this ValuePhoneNumber.
        :type bounding_polygon: oci.ai_vision.models.BoundingPolygon

        :param word_indexes:
            The value to assign to the word_indexes property of this ValuePhoneNumber.
        :type word_indexes: list[int]

        :param value:
            The value to assign to the value property of this ValuePhoneNumber.
        :type value: str

        """
        self.swagger_types = {
            'value_type': 'str',
            'text': 'str',
            'confidence': 'float',
            'bounding_polygon': 'BoundingPolygon',
            'word_indexes': 'list[int]',
            'value': 'str'
        }

        self.attribute_map = {
            'value_type': 'valueType',
            'text': 'text',
            'confidence': 'confidence',
            'bounding_polygon': 'boundingPolygon',
            'word_indexes': 'wordIndexes',
            'value': 'value'
        }

        self._value_type = None
        self._text = None
        self._confidence = None
        self._bounding_polygon = None
        self._word_indexes = None
        self._value = None
        self._value_type = 'PHONE_NUMBER'

    @property
    def value(self):
        """
        **[Required]** Gets the value of this ValuePhoneNumber.
        Phone number field value.


        :return: The value of this ValuePhoneNumber.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this ValuePhoneNumber.
        Phone number field value.


        :param value: The value of this ValuePhoneNumber.
        :type: str
        """
        self._value = value

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
