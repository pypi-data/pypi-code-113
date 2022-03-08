# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Deployment(object):
    """
    A container for your OCI GoldenGate resources, such as the OCI GoldenGate deployment console.
    """

    #: A constant which can be used with the lifecycle_state property of a Deployment.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a Deployment.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a Deployment.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a Deployment.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a Deployment.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a Deployment.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a Deployment.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a Deployment.
    #: This constant has a value of "NEEDS_ATTENTION"
    LIFECYCLE_STATE_NEEDS_ATTENTION = "NEEDS_ATTENTION"

    #: A constant which can be used with the lifecycle_state property of a Deployment.
    #: This constant has a value of "IN_PROGRESS"
    LIFECYCLE_STATE_IN_PROGRESS = "IN_PROGRESS"

    #: A constant which can be used with the lifecycle_state property of a Deployment.
    #: This constant has a value of "CANCELING"
    LIFECYCLE_STATE_CANCELING = "CANCELING"

    #: A constant which can be used with the lifecycle_state property of a Deployment.
    #: This constant has a value of "CANCELED"
    LIFECYCLE_STATE_CANCELED = "CANCELED"

    #: A constant which can be used with the lifecycle_state property of a Deployment.
    #: This constant has a value of "SUCCEEDED"
    LIFECYCLE_STATE_SUCCEEDED = "SUCCEEDED"

    #: A constant which can be used with the lifecycle_sub_state property of a Deployment.
    #: This constant has a value of "RECOVERING"
    LIFECYCLE_SUB_STATE_RECOVERING = "RECOVERING"

    #: A constant which can be used with the lifecycle_sub_state property of a Deployment.
    #: This constant has a value of "STARTING"
    LIFECYCLE_SUB_STATE_STARTING = "STARTING"

    #: A constant which can be used with the lifecycle_sub_state property of a Deployment.
    #: This constant has a value of "STOPPING"
    LIFECYCLE_SUB_STATE_STOPPING = "STOPPING"

    #: A constant which can be used with the lifecycle_sub_state property of a Deployment.
    #: This constant has a value of "MOVING"
    LIFECYCLE_SUB_STATE_MOVING = "MOVING"

    #: A constant which can be used with the lifecycle_sub_state property of a Deployment.
    #: This constant has a value of "UPGRADING"
    LIFECYCLE_SUB_STATE_UPGRADING = "UPGRADING"

    #: A constant which can be used with the lifecycle_sub_state property of a Deployment.
    #: This constant has a value of "RESTORING"
    LIFECYCLE_SUB_STATE_RESTORING = "RESTORING"

    #: A constant which can be used with the lifecycle_sub_state property of a Deployment.
    #: This constant has a value of "BACKUP_IN_PROGRESS"
    LIFECYCLE_SUB_STATE_BACKUP_IN_PROGRESS = "BACKUP_IN_PROGRESS"

    #: A constant which can be used with the license_model property of a Deployment.
    #: This constant has a value of "LICENSE_INCLUDED"
    LICENSE_MODEL_LICENSE_INCLUDED = "LICENSE_INCLUDED"

    #: A constant which can be used with the license_model property of a Deployment.
    #: This constant has a value of "BRING_YOUR_OWN_LICENSE"
    LICENSE_MODEL_BRING_YOUR_OWN_LICENSE = "BRING_YOUR_OWN_LICENSE"

    #: A constant which can be used with the deployment_type property of a Deployment.
    #: This constant has a value of "OGG"
    DEPLOYMENT_TYPE_OGG = "OGG"

    def __init__(self, **kwargs):
        """
        Initializes a new Deployment object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this Deployment.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this Deployment.
        :type display_name: str

        :param description:
            The value to assign to the description property of this Deployment.
        :type description: str

        :param compartment_id:
            The value to assign to the compartment_id property of this Deployment.
        :type compartment_id: str

        :param deployment_backup_id:
            The value to assign to the deployment_backup_id property of this Deployment.
        :type deployment_backup_id: str

        :param time_created:
            The value to assign to the time_created property of this Deployment.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this Deployment.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this Deployment.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED", "NEEDS_ATTENTION", "IN_PROGRESS", "CANCELING", "CANCELED", "SUCCEEDED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_sub_state:
            The value to assign to the lifecycle_sub_state property of this Deployment.
            Allowed values for this property are: "RECOVERING", "STARTING", "STOPPING", "MOVING", "UPGRADING", "RESTORING", "BACKUP_IN_PROGRESS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_sub_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this Deployment.
        :type lifecycle_details: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this Deployment.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this Deployment.
        :type defined_tags: dict(str, dict(str, object))

        :param is_healthy:
            The value to assign to the is_healthy property of this Deployment.
        :type is_healthy: bool

        :param subnet_id:
            The value to assign to the subnet_id property of this Deployment.
        :type subnet_id: str

        :param fqdn:
            The value to assign to the fqdn property of this Deployment.
        :type fqdn: str

        :param license_model:
            The value to assign to the license_model property of this Deployment.
            Allowed values for this property are: "LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type license_model: str

        :param cpu_core_count:
            The value to assign to the cpu_core_count property of this Deployment.
        :type cpu_core_count: int

        :param is_auto_scaling_enabled:
            The value to assign to the is_auto_scaling_enabled property of this Deployment.
        :type is_auto_scaling_enabled: bool

        :param nsg_ids:
            The value to assign to the nsg_ids property of this Deployment.
        :type nsg_ids: list[str]

        :param is_public:
            The value to assign to the is_public property of this Deployment.
        :type is_public: bool

        :param public_ip_address:
            The value to assign to the public_ip_address property of this Deployment.
        :type public_ip_address: str

        :param private_ip_address:
            The value to assign to the private_ip_address property of this Deployment.
        :type private_ip_address: str

        :param deployment_url:
            The value to assign to the deployment_url property of this Deployment.
        :type deployment_url: str

        :param system_tags:
            The value to assign to the system_tags property of this Deployment.
        :type system_tags: dict(str, dict(str, object))

        :param is_latest_version:
            The value to assign to the is_latest_version property of this Deployment.
        :type is_latest_version: bool

        :param time_upgrade_required:
            The value to assign to the time_upgrade_required property of this Deployment.
        :type time_upgrade_required: datetime

        :param deployment_type:
            The value to assign to the deployment_type property of this Deployment.
            Allowed values for this property are: "OGG", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type deployment_type: str

        :param ogg_data:
            The value to assign to the ogg_data property of this Deployment.
        :type ogg_data: oci.golden_gate.models.OggDeployment

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'description': 'str',
            'compartment_id': 'str',
            'deployment_backup_id': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_sub_state': 'str',
            'lifecycle_details': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'is_healthy': 'bool',
            'subnet_id': 'str',
            'fqdn': 'str',
            'license_model': 'str',
            'cpu_core_count': 'int',
            'is_auto_scaling_enabled': 'bool',
            'nsg_ids': 'list[str]',
            'is_public': 'bool',
            'public_ip_address': 'str',
            'private_ip_address': 'str',
            'deployment_url': 'str',
            'system_tags': 'dict(str, dict(str, object))',
            'is_latest_version': 'bool',
            'time_upgrade_required': 'datetime',
            'deployment_type': 'str',
            'ogg_data': 'OggDeployment'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'description': 'description',
            'compartment_id': 'compartmentId',
            'deployment_backup_id': 'deploymentBackupId',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_sub_state': 'lifecycleSubState',
            'lifecycle_details': 'lifecycleDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'is_healthy': 'isHealthy',
            'subnet_id': 'subnetId',
            'fqdn': 'fqdn',
            'license_model': 'licenseModel',
            'cpu_core_count': 'cpuCoreCount',
            'is_auto_scaling_enabled': 'isAutoScalingEnabled',
            'nsg_ids': 'nsgIds',
            'is_public': 'isPublic',
            'public_ip_address': 'publicIpAddress',
            'private_ip_address': 'privateIpAddress',
            'deployment_url': 'deploymentUrl',
            'system_tags': 'systemTags',
            'is_latest_version': 'isLatestVersion',
            'time_upgrade_required': 'timeUpgradeRequired',
            'deployment_type': 'deploymentType',
            'ogg_data': 'oggData'
        }

        self._id = None
        self._display_name = None
        self._description = None
        self._compartment_id = None
        self._deployment_backup_id = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._lifecycle_sub_state = None
        self._lifecycle_details = None
        self._freeform_tags = None
        self._defined_tags = None
        self._is_healthy = None
        self._subnet_id = None
        self._fqdn = None
        self._license_model = None
        self._cpu_core_count = None
        self._is_auto_scaling_enabled = None
        self._nsg_ids = None
        self._is_public = None
        self._public_ip_address = None
        self._private_ip_address = None
        self._deployment_url = None
        self._system_tags = None
        self._is_latest_version = None
        self._time_upgrade_required = None
        self._deployment_type = None
        self._ogg_data = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this Deployment.
        The `OCID`__ of the deployment being referenced.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this Deployment.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Deployment.
        The `OCID`__ of the deployment being referenced.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this Deployment.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        Gets the display_name of this Deployment.
        An object's Display Name.


        :return: The display_name of this Deployment.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this Deployment.
        An object's Display Name.


        :param display_name: The display_name of this Deployment.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this Deployment.
        Metadata about this specific object.


        :return: The description of this Deployment.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Deployment.
        Metadata about this specific object.


        :param description: The description of this Deployment.
        :type: str
        """
        self._description = description

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this Deployment.
        The `OCID`__ of the compartment being referenced.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this Deployment.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this Deployment.
        The `OCID`__ of the compartment being referenced.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this Deployment.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def deployment_backup_id(self):
        """
        Gets the deployment_backup_id of this Deployment.
        The `OCID`__ of the backup being referenced.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The deployment_backup_id of this Deployment.
        :rtype: str
        """
        return self._deployment_backup_id

    @deployment_backup_id.setter
    def deployment_backup_id(self, deployment_backup_id):
        """
        Sets the deployment_backup_id of this Deployment.
        The `OCID`__ of the backup being referenced.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param deployment_backup_id: The deployment_backup_id of this Deployment.
        :type: str
        """
        self._deployment_backup_id = deployment_backup_id

    @property
    def time_created(self):
        """
        Gets the time_created of this Deployment.
        The time the resource was created. The format is defined by `RFC3339`__, such as `2016-08-25T21:10:29.600Z`.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this Deployment.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this Deployment.
        The time the resource was created. The format is defined by `RFC3339`__, such as `2016-08-25T21:10:29.600Z`.

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this Deployment.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this Deployment.
        The time the resource was last updated. The format is defined by `RFC3339`__, such as `2016-08-25T21:10:29.600Z`.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_updated of this Deployment.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this Deployment.
        The time the resource was last updated. The format is defined by `RFC3339`__, such as `2016-08-25T21:10:29.600Z`.

        __ https://tools.ietf.org/html/rfc3339


        :param time_updated: The time_updated of this Deployment.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this Deployment.
        Possible lifecycle states.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED", "NEEDS_ATTENTION", "IN_PROGRESS", "CANCELING", "CANCELED", "SUCCEEDED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this Deployment.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this Deployment.
        Possible lifecycle states.


        :param lifecycle_state: The lifecycle_state of this Deployment.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED", "NEEDS_ATTENTION", "IN_PROGRESS", "CANCELING", "CANCELED", "SUCCEEDED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_sub_state(self):
        """
        Gets the lifecycle_sub_state of this Deployment.
        Possible GGS lifecycle sub-states.

        Allowed values for this property are: "RECOVERING", "STARTING", "STOPPING", "MOVING", "UPGRADING", "RESTORING", "BACKUP_IN_PROGRESS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_sub_state of this Deployment.
        :rtype: str
        """
        return self._lifecycle_sub_state

    @lifecycle_sub_state.setter
    def lifecycle_sub_state(self, lifecycle_sub_state):
        """
        Sets the lifecycle_sub_state of this Deployment.
        Possible GGS lifecycle sub-states.


        :param lifecycle_sub_state: The lifecycle_sub_state of this Deployment.
        :type: str
        """
        allowed_values = ["RECOVERING", "STARTING", "STOPPING", "MOVING", "UPGRADING", "RESTORING", "BACKUP_IN_PROGRESS"]
        if not value_allowed_none_or_none_sentinel(lifecycle_sub_state, allowed_values):
            lifecycle_sub_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_sub_state = lifecycle_sub_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this Deployment.
        Describes the object's current state in detail. For example, it can be used to provide actionable information for a resource in a Failed state.


        :return: The lifecycle_details of this Deployment.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this Deployment.
        Describes the object's current state in detail. For example, it can be used to provide actionable information for a resource in a Failed state.


        :param lifecycle_details: The lifecycle_details of this Deployment.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this Deployment.
        A simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this Deployment.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this Deployment.
        A simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this Deployment.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this Deployment.
        Tags defined for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this Deployment.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this Deployment.
        Tags defined for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this Deployment.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def is_healthy(self):
        """
        Gets the is_healthy of this Deployment.
        True if all of the aggregate resources are working correctly.


        :return: The is_healthy of this Deployment.
        :rtype: bool
        """
        return self._is_healthy

    @is_healthy.setter
    def is_healthy(self, is_healthy):
        """
        Sets the is_healthy of this Deployment.
        True if all of the aggregate resources are working correctly.


        :param is_healthy: The is_healthy of this Deployment.
        :type: bool
        """
        self._is_healthy = is_healthy

    @property
    def subnet_id(self):
        """
        **[Required]** Gets the subnet_id of this Deployment.
        The `OCID`__ of the subnet being referenced.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The subnet_id of this Deployment.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """
        Sets the subnet_id of this Deployment.
        The `OCID`__ of the subnet being referenced.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param subnet_id: The subnet_id of this Deployment.
        :type: str
        """
        self._subnet_id = subnet_id

    @property
    def fqdn(self):
        """
        Gets the fqdn of this Deployment.
        A three-label Fully Qualified Domain Name (FQDN) for a resource.


        :return: The fqdn of this Deployment.
        :rtype: str
        """
        return self._fqdn

    @fqdn.setter
    def fqdn(self, fqdn):
        """
        Sets the fqdn of this Deployment.
        A three-label Fully Qualified Domain Name (FQDN) for a resource.


        :param fqdn: The fqdn of this Deployment.
        :type: str
        """
        self._fqdn = fqdn

    @property
    def license_model(self):
        """
        **[Required]** Gets the license_model of this Deployment.
        The Oracle license model that applies to a Deployment.

        Allowed values for this property are: "LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The license_model of this Deployment.
        :rtype: str
        """
        return self._license_model

    @license_model.setter
    def license_model(self, license_model):
        """
        Sets the license_model of this Deployment.
        The Oracle license model that applies to a Deployment.


        :param license_model: The license_model of this Deployment.
        :type: str
        """
        allowed_values = ["LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"]
        if not value_allowed_none_or_none_sentinel(license_model, allowed_values):
            license_model = 'UNKNOWN_ENUM_VALUE'
        self._license_model = license_model

    @property
    def cpu_core_count(self):
        """
        **[Required]** Gets the cpu_core_count of this Deployment.
        The Minimum number of OCPUs to be made available for this Deployment.


        :return: The cpu_core_count of this Deployment.
        :rtype: int
        """
        return self._cpu_core_count

    @cpu_core_count.setter
    def cpu_core_count(self, cpu_core_count):
        """
        Sets the cpu_core_count of this Deployment.
        The Minimum number of OCPUs to be made available for this Deployment.


        :param cpu_core_count: The cpu_core_count of this Deployment.
        :type: int
        """
        self._cpu_core_count = cpu_core_count

    @property
    def is_auto_scaling_enabled(self):
        """
        **[Required]** Gets the is_auto_scaling_enabled of this Deployment.
        Indicates if auto scaling is enabled for the Deployment's CPU core count.


        :return: The is_auto_scaling_enabled of this Deployment.
        :rtype: bool
        """
        return self._is_auto_scaling_enabled

    @is_auto_scaling_enabled.setter
    def is_auto_scaling_enabled(self, is_auto_scaling_enabled):
        """
        Sets the is_auto_scaling_enabled of this Deployment.
        Indicates if auto scaling is enabled for the Deployment's CPU core count.


        :param is_auto_scaling_enabled: The is_auto_scaling_enabled of this Deployment.
        :type: bool
        """
        self._is_auto_scaling_enabled = is_auto_scaling_enabled

    @property
    def nsg_ids(self):
        """
        Gets the nsg_ids of this Deployment.
        An array of `Network Security Group`__ OCIDs used to define network access for a deployment.

        __ https://docs.cloud.oracle.com/Content/Network/Concepts/networksecuritygroups.htm


        :return: The nsg_ids of this Deployment.
        :rtype: list[str]
        """
        return self._nsg_ids

    @nsg_ids.setter
    def nsg_ids(self, nsg_ids):
        """
        Sets the nsg_ids of this Deployment.
        An array of `Network Security Group`__ OCIDs used to define network access for a deployment.

        __ https://docs.cloud.oracle.com/Content/Network/Concepts/networksecuritygroups.htm


        :param nsg_ids: The nsg_ids of this Deployment.
        :type: list[str]
        """
        self._nsg_ids = nsg_ids

    @property
    def is_public(self):
        """
        Gets the is_public of this Deployment.
        True if this object is publicly available.


        :return: The is_public of this Deployment.
        :rtype: bool
        """
        return self._is_public

    @is_public.setter
    def is_public(self, is_public):
        """
        Sets the is_public of this Deployment.
        True if this object is publicly available.


        :param is_public: The is_public of this Deployment.
        :type: bool
        """
        self._is_public = is_public

    @property
    def public_ip_address(self):
        """
        Gets the public_ip_address of this Deployment.
        The public IP address representing the access point for the Deployment.


        :return: The public_ip_address of this Deployment.
        :rtype: str
        """
        return self._public_ip_address

    @public_ip_address.setter
    def public_ip_address(self, public_ip_address):
        """
        Sets the public_ip_address of this Deployment.
        The public IP address representing the access point for the Deployment.


        :param public_ip_address: The public_ip_address of this Deployment.
        :type: str
        """
        self._public_ip_address = public_ip_address

    @property
    def private_ip_address(self):
        """
        Gets the private_ip_address of this Deployment.
        The private IP address in the customer's VCN representing the access point for the associated endpoint service in the GoldenGate service VCN.


        :return: The private_ip_address of this Deployment.
        :rtype: str
        """
        return self._private_ip_address

    @private_ip_address.setter
    def private_ip_address(self, private_ip_address):
        """
        Sets the private_ip_address of this Deployment.
        The private IP address in the customer's VCN representing the access point for the associated endpoint service in the GoldenGate service VCN.


        :param private_ip_address: The private_ip_address of this Deployment.
        :type: str
        """
        self._private_ip_address = private_ip_address

    @property
    def deployment_url(self):
        """
        Gets the deployment_url of this Deployment.
        The URL of a resource.


        :return: The deployment_url of this Deployment.
        :rtype: str
        """
        return self._deployment_url

    @deployment_url.setter
    def deployment_url(self, deployment_url):
        """
        Sets the deployment_url of this Deployment.
        The URL of a resource.


        :param deployment_url: The deployment_url of this Deployment.
        :type: str
        """
        self._deployment_url = deployment_url

    @property
    def system_tags(self):
        """
        Gets the system_tags of this Deployment.
        The system tags associated with this resource, if any. The system tags are set by Oracle Cloud Infrastructure services. Each key is predefined and scoped to namespaces.  For more information, see `Resource Tags`__.
        Example: `{orcl-cloud: {free-tier-retain: true}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The system_tags of this Deployment.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this Deployment.
        The system tags associated with this resource, if any. The system tags are set by Oracle Cloud Infrastructure services. Each key is predefined and scoped to namespaces.  For more information, see `Resource Tags`__.
        Example: `{orcl-cloud: {free-tier-retain: true}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param system_tags: The system_tags of this Deployment.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    @property
    def is_latest_version(self):
        """
        Gets the is_latest_version of this Deployment.
        Indicates if the resource is the the latest available version.


        :return: The is_latest_version of this Deployment.
        :rtype: bool
        """
        return self._is_latest_version

    @is_latest_version.setter
    def is_latest_version(self, is_latest_version):
        """
        Sets the is_latest_version of this Deployment.
        Indicates if the resource is the the latest available version.


        :param is_latest_version: The is_latest_version of this Deployment.
        :type: bool
        """
        self._is_latest_version = is_latest_version

    @property
    def time_upgrade_required(self):
        """
        Gets the time_upgrade_required of this Deployment.
        The date the existing version in use will no longer be considered as usable and an upgrade will be required.  This date is typically 6 months after the version was released for use by GGS.  The format is defined by `RFC3339`__, such as `2016-08-25T21:10:29.600Z`.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_upgrade_required of this Deployment.
        :rtype: datetime
        """
        return self._time_upgrade_required

    @time_upgrade_required.setter
    def time_upgrade_required(self, time_upgrade_required):
        """
        Sets the time_upgrade_required of this Deployment.
        The date the existing version in use will no longer be considered as usable and an upgrade will be required.  This date is typically 6 months after the version was released for use by GGS.  The format is defined by `RFC3339`__, such as `2016-08-25T21:10:29.600Z`.

        __ https://tools.ietf.org/html/rfc3339


        :param time_upgrade_required: The time_upgrade_required of this Deployment.
        :type: datetime
        """
        self._time_upgrade_required = time_upgrade_required

    @property
    def deployment_type(self):
        """
        **[Required]** Gets the deployment_type of this Deployment.
        The type of deployment, the value determines the exact 'type' of service executed in the Deployment. NOTE: Use of the value OGG is maintained for backward compatibility purposes.  Its use is discouraged
              in favor of the equivalent DATABASE_ORACLE value.

        Allowed values for this property are: "OGG", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The deployment_type of this Deployment.
        :rtype: str
        """
        return self._deployment_type

    @deployment_type.setter
    def deployment_type(self, deployment_type):
        """
        Sets the deployment_type of this Deployment.
        The type of deployment, the value determines the exact 'type' of service executed in the Deployment. NOTE: Use of the value OGG is maintained for backward compatibility purposes.  Its use is discouraged
              in favor of the equivalent DATABASE_ORACLE value.


        :param deployment_type: The deployment_type of this Deployment.
        :type: str
        """
        allowed_values = ["OGG"]
        if not value_allowed_none_or_none_sentinel(deployment_type, allowed_values):
            deployment_type = 'UNKNOWN_ENUM_VALUE'
        self._deployment_type = deployment_type

    @property
    def ogg_data(self):
        """
        Gets the ogg_data of this Deployment.

        :return: The ogg_data of this Deployment.
        :rtype: oci.golden_gate.models.OggDeployment
        """
        return self._ogg_data

    @ogg_data.setter
    def ogg_data(self, ogg_data):
        """
        Sets the ogg_data of this Deployment.

        :param ogg_data: The ogg_data of this Deployment.
        :type: oci.golden_gate.models.OggDeployment
        """
        self._ogg_data = ogg_data

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
