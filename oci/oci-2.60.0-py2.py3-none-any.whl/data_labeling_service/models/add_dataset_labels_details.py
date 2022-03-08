# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AddDatasetLabelsDetails(object):
    """
    Adds a subset of Labels to the Dataset's LabelSet.  This LabelSet will be merged with the current Dataset's LabelSet. Requests with duplicate Labels will be rejected.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AddDatasetLabelsDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param label_set:
            The value to assign to the label_set property of this AddDatasetLabelsDetails.
        :type label_set: oci.data_labeling_service.models.LabelSet

        """
        self.swagger_types = {
            'label_set': 'LabelSet'
        }

        self.attribute_map = {
            'label_set': 'labelSet'
        }

        self._label_set = None

    @property
    def label_set(self):
        """
        Gets the label_set of this AddDatasetLabelsDetails.

        :return: The label_set of this AddDatasetLabelsDetails.
        :rtype: oci.data_labeling_service.models.LabelSet
        """
        return self._label_set

    @label_set.setter
    def label_set(self, label_set):
        """
        Sets the label_set of this AddDatasetLabelsDetails.

        :param label_set: The label_set of this AddDatasetLabelsDetails.
        :type: oci.data_labeling_service.models.LabelSet
        """
        self._label_set = label_set

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
