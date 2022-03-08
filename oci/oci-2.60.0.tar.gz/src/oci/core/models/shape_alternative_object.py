# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ShapeAlternativeObject(object):
    """
    The shape that Oracle recommends you to use an alternative to the current shape.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ShapeAlternativeObject object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param shape_name:
            The value to assign to the shape_name property of this ShapeAlternativeObject.
        :type shape_name: str

        """
        self.swagger_types = {
            'shape_name': 'str'
        }

        self.attribute_map = {
            'shape_name': 'shapeName'
        }

        self._shape_name = None

    @property
    def shape_name(self):
        """
        **[Required]** Gets the shape_name of this ShapeAlternativeObject.
        The name of the shape.


        :return: The shape_name of this ShapeAlternativeObject.
        :rtype: str
        """
        return self._shape_name

    @shape_name.setter
    def shape_name(self, shape_name):
        """
        Sets the shape_name of this ShapeAlternativeObject.
        The name of the shape.


        :param shape_name: The shape_name of this ShapeAlternativeObject.
        :type: str
        """
        self._shape_name = shape_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
