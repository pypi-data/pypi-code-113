# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Source(object):
    """
    The properties that define a source. Source refers to the source environment from which you migrate an application to Oracle Cloud
    Infrastructure. For more information, see `Manage Sources`__.

    To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're
    an administrator who needs to write policies to give users access, see `Getting Started with
    Policies`__.

    __ https://docs.cloud.oracle.com/iaas/application-migration/manage_sources.htm
    __ https://docs.cloud.oracle.com/Content/Identity/Concepts/policygetstarted.htm
    """

    #: A constant which can be used with the lifecycle_state property of a Source.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a Source.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a Source.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a Source.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a Source.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a Source.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    def __init__(self, **kwargs):
        """
        Initializes a new Source object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this Source.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this Source.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this Source.
        :type display_name: str

        :param description:
            The value to assign to the description property of this Source.
        :type description: str

        :param time_created:
            The value to assign to the time_created property of this Source.
        :type time_created: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this Source.
            Allowed values for this property are: "CREATING", "DELETING", "UPDATING", "ACTIVE", "INACTIVE", "DELETED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this Source.
        :type lifecycle_details: str

        :param source_details:
            The value to assign to the source_details property of this Source.
        :type source_details: oci.application_migration.models.SourceDetails

        :param freeform_tags:
            The value to assign to the freeform_tags property of this Source.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this Source.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'description': 'str',
            'time_created': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'source_details': 'SourceDetails',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'description': 'description',
            'time_created': 'timeCreated',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'source_details': 'sourceDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._id = None
        self._compartment_id = None
        self._display_name = None
        self._description = None
        self._time_created = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._source_details = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def id(self):
        """
        Gets the id of this Source.
        The `OCID`__ of the source.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The id of this Source.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Source.
        The `OCID`__ of the source.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param id: The id of this Source.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this Source.
        The `OCID`__ of the compartment that contains the source.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this Source.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this Source.
        The `OCID`__ of the compartment that contains the source.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this Source.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        Gets the display_name of this Source.
        Name of the source. This helps you to identify the appropriate source environment when you have multiple sources defined.


        :return: The display_name of this Source.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this Source.
        Name of the source. This helps you to identify the appropriate source environment when you have multiple sources defined.


        :param display_name: The display_name of this Source.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this Source.
        Description of the source. This helps you to identify the appropriate source environment when you have multiple sources defined.


        :return: The description of this Source.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Source.
        Description of the source. This helps you to identify the appropriate source environment when you have multiple sources defined.


        :param description: The description of this Source.
        :type: str
        """
        self._description = description

    @property
    def time_created(self):
        """
        Gets the time_created of this Source.
        The date and time at which the source was created, in the format defined by RFC3339.


        :return: The time_created of this Source.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this Source.
        The date and time at which the source was created, in the format defined by RFC3339.


        :param time_created: The time_created of this Source.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this Source.
        The current state of the source.

        Allowed values for this property are: "CREATING", "DELETING", "UPDATING", "ACTIVE", "INACTIVE", "DELETED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this Source.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this Source.
        The current state of the source.


        :param lifecycle_state: The lifecycle_state of this Source.
        :type: str
        """
        allowed_values = ["CREATING", "DELETING", "UPDATING", "ACTIVE", "INACTIVE", "DELETED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this Source.
        Details about the current lifecycle state of the source.


        :return: The lifecycle_details of this Source.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this Source.
        Details about the current lifecycle state of the source.


        :param lifecycle_details: The lifecycle_details of this Source.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def source_details(self):
        """
        Gets the source_details of this Source.

        :return: The source_details of this Source.
        :rtype: oci.application_migration.models.SourceDetails
        """
        return self._source_details

    @source_details.setter
    def source_details(self, source_details):
        """
        Sets the source_details of this Source.

        :param source_details: The source_details of this Source.
        :type: oci.application_migration.models.SourceDetails
        """
        self._source_details = source_details

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this Source.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__. Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this Source.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this Source.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__. Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this Source.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this Source.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this Source.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this Source.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this Source.
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
