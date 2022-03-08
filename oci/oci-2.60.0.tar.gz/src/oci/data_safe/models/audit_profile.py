# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AuditProfile(object):
    """
    The resource represents audit profile settings and audit configurations for the database target, and helps evaluate the initial audit data volume for configuring collection in Data Safe. The resource is also responsible for auto-discovery of audit trails in the database target during target's registration.
    """

    #: A constant which can be used with the lifecycle_state property of a AuditProfile.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a AuditProfile.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a AuditProfile.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a AuditProfile.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a AuditProfile.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a AuditProfile.
    #: This constant has a value of "NEEDS_ATTENTION"
    LIFECYCLE_STATE_NEEDS_ATTENTION = "NEEDS_ATTENTION"

    #: A constant which can be used with the lifecycle_state property of a AuditProfile.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    def __init__(self, **kwargs):
        """
        Initializes a new AuditProfile object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this AuditProfile.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this AuditProfile.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this AuditProfile.
        :type display_name: str

        :param time_created:
            The value to assign to the time_created property of this AuditProfile.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this AuditProfile.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this AuditProfile.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "FAILED", "NEEDS_ATTENTION", "DELETED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this AuditProfile.
        :type lifecycle_details: str

        :param target_id:
            The value to assign to the target_id property of this AuditProfile.
        :type target_id: str

        :param description:
            The value to assign to the description property of this AuditProfile.
        :type description: str

        :param audit_trails:
            The value to assign to the audit_trails property of this AuditProfile.
        :type audit_trails: list[oci.data_safe.models.AuditTrail]

        :param is_paid_usage_enabled:
            The value to assign to the is_paid_usage_enabled property of this AuditProfile.
        :type is_paid_usage_enabled: bool

        :param online_months:
            The value to assign to the online_months property of this AuditProfile.
        :type online_months: int

        :param offline_months:
            The value to assign to the offline_months property of this AuditProfile.
        :type offline_months: int

        :param audit_collected_volume:
            The value to assign to the audit_collected_volume property of this AuditProfile.
        :type audit_collected_volume: int

        :param is_override_global_retention_setting:
            The value to assign to the is_override_global_retention_setting property of this AuditProfile.
        :type is_override_global_retention_setting: bool

        :param freeform_tags:
            The value to assign to the freeform_tags property of this AuditProfile.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this AuditProfile.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this AuditProfile.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'target_id': 'str',
            'description': 'str',
            'audit_trails': 'list[AuditTrail]',
            'is_paid_usage_enabled': 'bool',
            'online_months': 'int',
            'offline_months': 'int',
            'audit_collected_volume': 'int',
            'is_override_global_retention_setting': 'bool',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'target_id': 'targetId',
            'description': 'description',
            'audit_trails': 'auditTrails',
            'is_paid_usage_enabled': 'isPaidUsageEnabled',
            'online_months': 'onlineMonths',
            'offline_months': 'offlineMonths',
            'audit_collected_volume': 'auditCollectedVolume',
            'is_override_global_retention_setting': 'isOverrideGlobalRetentionSetting',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._id = None
        self._compartment_id = None
        self._display_name = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._target_id = None
        self._description = None
        self._audit_trails = None
        self._is_paid_usage_enabled = None
        self._online_months = None
        self._offline_months = None
        self._audit_collected_volume = None
        self._is_override_global_retention_setting = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this AuditProfile.
        The OCID of the audit profile.


        :return: The id of this AuditProfile.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this AuditProfile.
        The OCID of the audit profile.


        :param id: The id of this AuditProfile.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this AuditProfile.
        The OCID of the compartment that contains the audit.


        :return: The compartment_id of this AuditProfile.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this AuditProfile.
        The OCID of the compartment that contains the audit.


        :param compartment_id: The compartment_id of this AuditProfile.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this AuditProfile.
        The display name of the audit profile.


        :return: The display_name of this AuditProfile.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this AuditProfile.
        The display name of the audit profile.


        :param display_name: The display_name of this AuditProfile.
        :type: str
        """
        self._display_name = display_name

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this AuditProfile.
        The date and time the audit profile was created, in the format defined by RFC3339.


        :return: The time_created of this AuditProfile.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this AuditProfile.
        The date and time the audit profile was created, in the format defined by RFC3339.


        :param time_created: The time_created of this AuditProfile.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this AuditProfile.
        The date and time the audit profile was updated, in the format defined by RFC3339.


        :return: The time_updated of this AuditProfile.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this AuditProfile.
        The date and time the audit profile was updated, in the format defined by RFC3339.


        :param time_updated: The time_updated of this AuditProfile.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this AuditProfile.
        The current state of the audit profile.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "FAILED", "NEEDS_ATTENTION", "DELETED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this AuditProfile.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this AuditProfile.
        The current state of the audit profile.


        :param lifecycle_state: The lifecycle_state of this AuditProfile.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "DELETING", "FAILED", "NEEDS_ATTENTION", "DELETED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this AuditProfile.
        Details about the current state of the audit profile in Data Safe.


        :return: The lifecycle_details of this AuditProfile.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this AuditProfile.
        Details about the current state of the audit profile in Data Safe.


        :param lifecycle_details: The lifecycle_details of this AuditProfile.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def target_id(self):
        """
        **[Required]** Gets the target_id of this AuditProfile.
        The OCID of the Data Safe target for which the audit profile is created.


        :return: The target_id of this AuditProfile.
        :rtype: str
        """
        return self._target_id

    @target_id.setter
    def target_id(self, target_id):
        """
        Sets the target_id of this AuditProfile.
        The OCID of the Data Safe target for which the audit profile is created.


        :param target_id: The target_id of this AuditProfile.
        :type: str
        """
        self._target_id = target_id

    @property
    def description(self):
        """
        Gets the description of this AuditProfile.
        The description of the audit profile.


        :return: The description of this AuditProfile.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this AuditProfile.
        The description of the audit profile.


        :param description: The description of this AuditProfile.
        :type: str
        """
        self._description = description

    @property
    def audit_trails(self):
        """
        Gets the audit_trails of this AuditProfile.
        Indicates the list of available audit trails on the target.


        :return: The audit_trails of this AuditProfile.
        :rtype: list[oci.data_safe.models.AuditTrail]
        """
        return self._audit_trails

    @audit_trails.setter
    def audit_trails(self, audit_trails):
        """
        Sets the audit_trails of this AuditProfile.
        Indicates the list of available audit trails on the target.


        :param audit_trails: The audit_trails of this AuditProfile.
        :type: list[oci.data_safe.models.AuditTrail]
        """
        self._audit_trails = audit_trails

    @property
    def is_paid_usage_enabled(self):
        """
        **[Required]** Gets the is_paid_usage_enabled of this AuditProfile.
        Indicates if you want to continue collecting audit records beyond the free limit of one million audit records per month per target database,
        potentially incurring additional charges. The default value is inherited from the global settings.
        You can change at the global level or at the target level.


        :return: The is_paid_usage_enabled of this AuditProfile.
        :rtype: bool
        """
        return self._is_paid_usage_enabled

    @is_paid_usage_enabled.setter
    def is_paid_usage_enabled(self, is_paid_usage_enabled):
        """
        Sets the is_paid_usage_enabled of this AuditProfile.
        Indicates if you want to continue collecting audit records beyond the free limit of one million audit records per month per target database,
        potentially incurring additional charges. The default value is inherited from the global settings.
        You can change at the global level or at the target level.


        :param is_paid_usage_enabled: The is_paid_usage_enabled of this AuditProfile.
        :type: bool
        """
        self._is_paid_usage_enabled = is_paid_usage_enabled

    @property
    def online_months(self):
        """
        **[Required]** Gets the online_months of this AuditProfile.
        Indicates the number of months the audit records will be stored online in Oracle Data Safe audit repository for immediate reporting and analysis.
        Minimum: 1; Maximum:12 months


        :return: The online_months of this AuditProfile.
        :rtype: int
        """
        return self._online_months

    @online_months.setter
    def online_months(self, online_months):
        """
        Sets the online_months of this AuditProfile.
        Indicates the number of months the audit records will be stored online in Oracle Data Safe audit repository for immediate reporting and analysis.
        Minimum: 1; Maximum:12 months


        :param online_months: The online_months of this AuditProfile.
        :type: int
        """
        self._online_months = online_months

    @property
    def offline_months(self):
        """
        **[Required]** Gets the offline_months of this AuditProfile.
        Indicates the number of months the audit records will be stored offline in the Data Safe audit archive.
        Minimum: 0; Maximum: 72 months.
        If you have a requirement to store the audit data even longer in archive, please contact the Oracle Support.


        :return: The offline_months of this AuditProfile.
        :rtype: int
        """
        return self._offline_months

    @offline_months.setter
    def offline_months(self, offline_months):
        """
        Sets the offline_months of this AuditProfile.
        Indicates the number of months the audit records will be stored offline in the Data Safe audit archive.
        Minimum: 0; Maximum: 72 months.
        If you have a requirement to store the audit data even longer in archive, please contact the Oracle Support.


        :param offline_months: The offline_months of this AuditProfile.
        :type: int
        """
        self._offline_months = offline_months

    @property
    def audit_collected_volume(self):
        """
        Gets the audit_collected_volume of this AuditProfile.
        Indicates number of audit records collected by Data Safe in the current calendar month.
        Audit records for the Data Safe service account are excluded and are not counted towards your monthly free limit.


        :return: The audit_collected_volume of this AuditProfile.
        :rtype: int
        """
        return self._audit_collected_volume

    @audit_collected_volume.setter
    def audit_collected_volume(self, audit_collected_volume):
        """
        Sets the audit_collected_volume of this AuditProfile.
        Indicates number of audit records collected by Data Safe in the current calendar month.
        Audit records for the Data Safe service account are excluded and are not counted towards your monthly free limit.


        :param audit_collected_volume: The audit_collected_volume of this AuditProfile.
        :type: int
        """
        self._audit_collected_volume = audit_collected_volume

    @property
    def is_override_global_retention_setting(self):
        """
        **[Required]** Gets the is_override_global_retention_setting of this AuditProfile.
        Indicates whether audit retention settings like online and offline months is set at the
        target level overriding the global audit retention settings.


        :return: The is_override_global_retention_setting of this AuditProfile.
        :rtype: bool
        """
        return self._is_override_global_retention_setting

    @is_override_global_retention_setting.setter
    def is_override_global_retention_setting(self, is_override_global_retention_setting):
        """
        Sets the is_override_global_retention_setting of this AuditProfile.
        Indicates whether audit retention settings like online and offline months is set at the
        target level overriding the global audit retention settings.


        :param is_override_global_retention_setting: The is_override_global_retention_setting of this AuditProfile.
        :type: bool
        """
        self._is_override_global_retention_setting = is_override_global_retention_setting

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this AuditProfile.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see `Resource Tags`__

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this AuditProfile.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this AuditProfile.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see `Resource Tags`__

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this AuditProfile.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this AuditProfile.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this AuditProfile.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this AuditProfile.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this AuditProfile.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this AuditProfile.
        System tags for this resource. Each key is predefined and scoped to a namespace. For more information, see Resource Tags.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this AuditProfile.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this AuditProfile.
        System tags for this resource. Each key is predefined and scoped to a namespace. For more information, see Resource Tags.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this AuditProfile.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
