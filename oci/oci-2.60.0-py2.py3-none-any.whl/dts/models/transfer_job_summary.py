# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TransferJobSummary(object):
    """
    TransferJobSummary model.
    """

    #: A constant which can be used with the device_type property of a TransferJobSummary.
    #: This constant has a value of "DISK"
    DEVICE_TYPE_DISK = "DISK"

    #: A constant which can be used with the device_type property of a TransferJobSummary.
    #: This constant has a value of "APPLIANCE"
    DEVICE_TYPE_APPLIANCE = "APPLIANCE"

    #: A constant which can be used with the lifecycle_state property of a TransferJobSummary.
    #: This constant has a value of "INITIATED"
    LIFECYCLE_STATE_INITIATED = "INITIATED"

    #: A constant which can be used with the lifecycle_state property of a TransferJobSummary.
    #: This constant has a value of "PREPARING"
    LIFECYCLE_STATE_PREPARING = "PREPARING"

    #: A constant which can be used with the lifecycle_state property of a TransferJobSummary.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a TransferJobSummary.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a TransferJobSummary.
    #: This constant has a value of "CLOSED"
    LIFECYCLE_STATE_CLOSED = "CLOSED"

    def __init__(self, **kwargs):
        """
        Initializes a new TransferJobSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this TransferJobSummary.
        :type id: str

        :param upload_bucket_name:
            The value to assign to the upload_bucket_name property of this TransferJobSummary.
        :type upload_bucket_name: str

        :param display_name:
            The value to assign to the display_name property of this TransferJobSummary.
        :type display_name: str

        :param label:
            The value to assign to the label property of this TransferJobSummary.
        :type label: str

        :param device_type:
            The value to assign to the device_type property of this TransferJobSummary.
            Allowed values for this property are: "DISK", "APPLIANCE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type device_type: str

        :param creation_time:
            The value to assign to the creation_time property of this TransferJobSummary.
        :type creation_time: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this TransferJobSummary.
            Allowed values for this property are: "INITIATED", "PREPARING", "ACTIVE", "DELETED", "CLOSED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this TransferJobSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this TransferJobSummary.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'upload_bucket_name': 'str',
            'display_name': 'str',
            'label': 'str',
            'device_type': 'str',
            'creation_time': 'datetime',
            'lifecycle_state': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'upload_bucket_name': 'uploadBucketName',
            'display_name': 'displayName',
            'label': 'label',
            'device_type': 'deviceType',
            'creation_time': 'creationTime',
            'lifecycle_state': 'lifecycleState',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._id = None
        self._upload_bucket_name = None
        self._display_name = None
        self._label = None
        self._device_type = None
        self._creation_time = None
        self._lifecycle_state = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def id(self):
        """
        Gets the id of this TransferJobSummary.

        :return: The id of this TransferJobSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this TransferJobSummary.

        :param id: The id of this TransferJobSummary.
        :type: str
        """
        self._id = id

    @property
    def upload_bucket_name(self):
        """
        Gets the upload_bucket_name of this TransferJobSummary.

        :return: The upload_bucket_name of this TransferJobSummary.
        :rtype: str
        """
        return self._upload_bucket_name

    @upload_bucket_name.setter
    def upload_bucket_name(self, upload_bucket_name):
        """
        Sets the upload_bucket_name of this TransferJobSummary.

        :param upload_bucket_name: The upload_bucket_name of this TransferJobSummary.
        :type: str
        """
        self._upload_bucket_name = upload_bucket_name

    @property
    def display_name(self):
        """
        Gets the display_name of this TransferJobSummary.

        :return: The display_name of this TransferJobSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this TransferJobSummary.

        :param display_name: The display_name of this TransferJobSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def label(self):
        """
        Gets the label of this TransferJobSummary.

        :return: The label of this TransferJobSummary.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """
        Sets the label of this TransferJobSummary.

        :param label: The label of this TransferJobSummary.
        :type: str
        """
        self._label = label

    @property
    def device_type(self):
        """
        Gets the device_type of this TransferJobSummary.
        Allowed values for this property are: "DISK", "APPLIANCE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The device_type of this TransferJobSummary.
        :rtype: str
        """
        return self._device_type

    @device_type.setter
    def device_type(self, device_type):
        """
        Sets the device_type of this TransferJobSummary.

        :param device_type: The device_type of this TransferJobSummary.
        :type: str
        """
        allowed_values = ["DISK", "APPLIANCE"]
        if not value_allowed_none_or_none_sentinel(device_type, allowed_values):
            device_type = 'UNKNOWN_ENUM_VALUE'
        self._device_type = device_type

    @property
    def creation_time(self):
        """
        Gets the creation_time of this TransferJobSummary.

        :return: The creation_time of this TransferJobSummary.
        :rtype: datetime
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """
        Sets the creation_time of this TransferJobSummary.

        :param creation_time: The creation_time of this TransferJobSummary.
        :type: datetime
        """
        self._creation_time = creation_time

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this TransferJobSummary.
        Allowed values for this property are: "INITIATED", "PREPARING", "ACTIVE", "DELETED", "CLOSED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this TransferJobSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this TransferJobSummary.

        :param lifecycle_state: The lifecycle_state of this TransferJobSummary.
        :type: str
        """
        allowed_values = ["INITIATED", "PREPARING", "ACTIVE", "DELETED", "CLOSED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this TransferJobSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this TransferJobSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this TransferJobSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this TransferJobSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this TransferJobSummary.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this TransferJobSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this TransferJobSummary.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this TransferJobSummary.
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
