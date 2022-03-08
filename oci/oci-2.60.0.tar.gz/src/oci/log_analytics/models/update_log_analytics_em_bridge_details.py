# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateLogAnalyticsEmBridgeDetails(object):
    """
    Log analytics entity type definition to be updated.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateLogAnalyticsEmBridgeDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this UpdateLogAnalyticsEmBridgeDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this UpdateLogAnalyticsEmBridgeDetails.
        :type description: str

        :param bucket_name:
            The value to assign to the bucket_name property of this UpdateLogAnalyticsEmBridgeDetails.
        :type bucket_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateLogAnalyticsEmBridgeDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateLogAnalyticsEmBridgeDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'description': 'str',
            'bucket_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'description': 'description',
            'bucket_name': 'bucketName',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._display_name = None
        self._description = None
        self._bucket_name = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateLogAnalyticsEmBridgeDetails.
        Log analytics enterprise manager bridge display name.


        :return: The display_name of this UpdateLogAnalyticsEmBridgeDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateLogAnalyticsEmBridgeDetails.
        Log analytics enterprise manager bridge display name.


        :param display_name: The display_name of this UpdateLogAnalyticsEmBridgeDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this UpdateLogAnalyticsEmBridgeDetails.
        A description for log analytics enterprise manager bridge.


        :return: The description of this UpdateLogAnalyticsEmBridgeDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this UpdateLogAnalyticsEmBridgeDetails.
        A description for log analytics enterprise manager bridge.


        :param description: The description of this UpdateLogAnalyticsEmBridgeDetails.
        :type: str
        """
        self._description = description

    @property
    def bucket_name(self):
        """
        Gets the bucket_name of this UpdateLogAnalyticsEmBridgeDetails.
        Object store bucket name where enterprise manager harvested entities will be uploaded.


        :return: The bucket_name of this UpdateLogAnalyticsEmBridgeDetails.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        """
        Sets the bucket_name of this UpdateLogAnalyticsEmBridgeDetails.
        Object store bucket name where enterprise manager harvested entities will be uploaded.


        :param bucket_name: The bucket_name of this UpdateLogAnalyticsEmBridgeDetails.
        :type: str
        """
        self._bucket_name = bucket_name

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateLogAnalyticsEmBridgeDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this UpdateLogAnalyticsEmBridgeDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateLogAnalyticsEmBridgeDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this UpdateLogAnalyticsEmBridgeDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateLogAnalyticsEmBridgeDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this UpdateLogAnalyticsEmBridgeDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateLogAnalyticsEmBridgeDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this UpdateLogAnalyticsEmBridgeDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
