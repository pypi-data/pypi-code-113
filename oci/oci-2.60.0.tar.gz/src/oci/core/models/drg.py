# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Drg(object):
    """
    A dynamic routing gateway (DRG) is a virtual router that provides a path for private
    network traffic between networks. You use it with other Networking
    Service components to create a connection to your on-premises network using `Site-to-Site VPN`__ or a connection that uses
    `FastConnect`__. For more information, see
    `Overview of the Networking Service`__.

    To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized,
    talk to an administrator. If you're an administrator who needs to write policies to give users access, see
    `Getting Started with Policies`__.

    __ https://docs.cloud.oracle.com/Content/Network/Tasks/managingIPsec.htm
    __ https://docs.cloud.oracle.com/Content/Network/Concepts/fastconnect.htm
    __ https://docs.cloud.oracle.com/iaas/Content/Network/Concepts/overview.htm
    __ https://docs.cloud.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm
    """

    #: A constant which can be used with the lifecycle_state property of a Drg.
    #: This constant has a value of "PROVISIONING"
    LIFECYCLE_STATE_PROVISIONING = "PROVISIONING"

    #: A constant which can be used with the lifecycle_state property of a Drg.
    #: This constant has a value of "AVAILABLE"
    LIFECYCLE_STATE_AVAILABLE = "AVAILABLE"

    #: A constant which can be used with the lifecycle_state property of a Drg.
    #: This constant has a value of "TERMINATING"
    LIFECYCLE_STATE_TERMINATING = "TERMINATING"

    #: A constant which can be used with the lifecycle_state property of a Drg.
    #: This constant has a value of "TERMINATED"
    LIFECYCLE_STATE_TERMINATED = "TERMINATED"

    def __init__(self, **kwargs):
        """
        Initializes a new Drg object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this Drg.
        :type compartment_id: str

        :param defined_tags:
            The value to assign to the defined_tags property of this Drg.
        :type defined_tags: dict(str, dict(str, object))

        :param display_name:
            The value to assign to the display_name property of this Drg.
        :type display_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this Drg.
        :type freeform_tags: dict(str, str)

        :param id:
            The value to assign to the id property of this Drg.
        :type id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this Drg.
            Allowed values for this property are: "PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param time_created:
            The value to assign to the time_created property of this Drg.
        :type time_created: datetime

        :param default_drg_route_tables:
            The value to assign to the default_drg_route_tables property of this Drg.
        :type default_drg_route_tables: oci.core.models.DefaultDrgRouteTables

        :param default_export_drg_route_distribution_id:
            The value to assign to the default_export_drg_route_distribution_id property of this Drg.
        :type default_export_drg_route_distribution_id: str

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'defined_tags': 'dict(str, dict(str, object))',
            'display_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'id': 'str',
            'lifecycle_state': 'str',
            'time_created': 'datetime',
            'default_drg_route_tables': 'DefaultDrgRouteTables',
            'default_export_drg_route_distribution_id': 'str'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'defined_tags': 'definedTags',
            'display_name': 'displayName',
            'freeform_tags': 'freeformTags',
            'id': 'id',
            'lifecycle_state': 'lifecycleState',
            'time_created': 'timeCreated',
            'default_drg_route_tables': 'defaultDrgRouteTables',
            'default_export_drg_route_distribution_id': 'defaultExportDrgRouteDistributionId'
        }

        self._compartment_id = None
        self._defined_tags = None
        self._display_name = None
        self._freeform_tags = None
        self._id = None
        self._lifecycle_state = None
        self._time_created = None
        self._default_drg_route_tables = None
        self._default_export_drg_route_distribution_id = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this Drg.
        The `OCID`__ of the compartment containing the DRG.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this Drg.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this Drg.
        The `OCID`__ of the compartment containing the DRG.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this Drg.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this Drg.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this Drg.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this Drg.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this Drg.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def display_name(self):
        """
        Gets the display_name of this Drg.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this Drg.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this Drg.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this Drg.
        :type: str
        """
        self._display_name = display_name

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this Drg.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this Drg.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this Drg.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this Drg.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def id(self):
        """
        **[Required]** Gets the id of this Drg.
        The DRG's Oracle ID (`OCID`__).

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this Drg.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Drg.
        The DRG's Oracle ID (`OCID`__).

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this Drg.
        :type: str
        """
        self._id = id

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this Drg.
        The DRG's current state.

        Allowed values for this property are: "PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this Drg.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this Drg.
        The DRG's current state.


        :param lifecycle_state: The lifecycle_state of this Drg.
        :type: str
        """
        allowed_values = ["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def time_created(self):
        """
        Gets the time_created of this Drg.
        The date and time the DRG was created, in the format defined by `RFC3339`__.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this Drg.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this Drg.
        The date and time the DRG was created, in the format defined by `RFC3339`__.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this Drg.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def default_drg_route_tables(self):
        """
        Gets the default_drg_route_tables of this Drg.

        :return: The default_drg_route_tables of this Drg.
        :rtype: oci.core.models.DefaultDrgRouteTables
        """
        return self._default_drg_route_tables

    @default_drg_route_tables.setter
    def default_drg_route_tables(self, default_drg_route_tables):
        """
        Sets the default_drg_route_tables of this Drg.

        :param default_drg_route_tables: The default_drg_route_tables of this Drg.
        :type: oci.core.models.DefaultDrgRouteTables
        """
        self._default_drg_route_tables = default_drg_route_tables

    @property
    def default_export_drg_route_distribution_id(self):
        """
        Gets the default_export_drg_route_distribution_id of this Drg.
        The `OCID`__ of this DRG's default export route distribution for the DRG attachments.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The default_export_drg_route_distribution_id of this Drg.
        :rtype: str
        """
        return self._default_export_drg_route_distribution_id

    @default_export_drg_route_distribution_id.setter
    def default_export_drg_route_distribution_id(self, default_export_drg_route_distribution_id):
        """
        Sets the default_export_drg_route_distribution_id of this Drg.
        The `OCID`__ of this DRG's default export route distribution for the DRG attachments.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param default_export_drg_route_distribution_id: The default_export_drg_route_distribution_id of this Drg.
        :type: str
        """
        self._default_export_drg_route_distribution_id = default_export_drg_route_distribution_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
