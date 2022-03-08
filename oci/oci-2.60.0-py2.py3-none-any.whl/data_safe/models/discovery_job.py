# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DiscoveryJob(object):
    """
    A data discovery job. It helps track job's metadata as well as result statistics.
    """

    #: A constant which can be used with the discovery_type property of a DiscoveryJob.
    #: This constant has a value of "ALL"
    DISCOVERY_TYPE_ALL = "ALL"

    #: A constant which can be used with the discovery_type property of a DiscoveryJob.
    #: This constant has a value of "NEW"
    DISCOVERY_TYPE_NEW = "NEW"

    #: A constant which can be used with the discovery_type property of a DiscoveryJob.
    #: This constant has a value of "MODIFIED"
    DISCOVERY_TYPE_MODIFIED = "MODIFIED"

    #: A constant which can be used with the discovery_type property of a DiscoveryJob.
    #: This constant has a value of "DELETED"
    DISCOVERY_TYPE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a DiscoveryJob.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a DiscoveryJob.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a DiscoveryJob.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a DiscoveryJob.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a DiscoveryJob.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a DiscoveryJob.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new DiscoveryJob object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this DiscoveryJob.
        :type id: str

        :param discovery_type:
            The value to assign to the discovery_type property of this DiscoveryJob.
            Allowed values for this property are: "ALL", "NEW", "MODIFIED", "DELETED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type discovery_type: str

        :param display_name:
            The value to assign to the display_name property of this DiscoveryJob.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this DiscoveryJob.
        :type compartment_id: str

        :param time_started:
            The value to assign to the time_started property of this DiscoveryJob.
        :type time_started: datetime

        :param time_finished:
            The value to assign to the time_finished property of this DiscoveryJob.
        :type time_finished: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this DiscoveryJob.
            Allowed values for this property are: "CREATING", "ACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param sensitive_data_model_id:
            The value to assign to the sensitive_data_model_id property of this DiscoveryJob.
        :type sensitive_data_model_id: str

        :param target_id:
            The value to assign to the target_id property of this DiscoveryJob.
        :type target_id: str

        :param schemas_for_discovery:
            The value to assign to the schemas_for_discovery property of this DiscoveryJob.
        :type schemas_for_discovery: list[str]

        :param sensitive_type_ids_for_discovery:
            The value to assign to the sensitive_type_ids_for_discovery property of this DiscoveryJob.
        :type sensitive_type_ids_for_discovery: list[str]

        :param is_sample_data_collection_enabled:
            The value to assign to the is_sample_data_collection_enabled property of this DiscoveryJob.
        :type is_sample_data_collection_enabled: bool

        :param is_app_defined_relation_discovery_enabled:
            The value to assign to the is_app_defined_relation_discovery_enabled property of this DiscoveryJob.
        :type is_app_defined_relation_discovery_enabled: bool

        :param is_include_all_schemas:
            The value to assign to the is_include_all_schemas property of this DiscoveryJob.
        :type is_include_all_schemas: bool

        :param is_include_all_sensitive_types:
            The value to assign to the is_include_all_sensitive_types property of this DiscoveryJob.
        :type is_include_all_sensitive_types: bool

        :param total_schemas_scanned:
            The value to assign to the total_schemas_scanned property of this DiscoveryJob.
        :type total_schemas_scanned: int

        :param total_objects_scanned:
            The value to assign to the total_objects_scanned property of this DiscoveryJob.
        :type total_objects_scanned: int

        :param total_columns_scanned:
            The value to assign to the total_columns_scanned property of this DiscoveryJob.
        :type total_columns_scanned: int

        :param total_new_sensitive_columns:
            The value to assign to the total_new_sensitive_columns property of this DiscoveryJob.
        :type total_new_sensitive_columns: int

        :param total_modified_sensitive_columns:
            The value to assign to the total_modified_sensitive_columns property of this DiscoveryJob.
        :type total_modified_sensitive_columns: int

        :param total_deleted_sensitive_columns:
            The value to assign to the total_deleted_sensitive_columns property of this DiscoveryJob.
        :type total_deleted_sensitive_columns: int

        :param freeform_tags:
            The value to assign to the freeform_tags property of this DiscoveryJob.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this DiscoveryJob.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this DiscoveryJob.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'discovery_type': 'str',
            'display_name': 'str',
            'compartment_id': 'str',
            'time_started': 'datetime',
            'time_finished': 'datetime',
            'lifecycle_state': 'str',
            'sensitive_data_model_id': 'str',
            'target_id': 'str',
            'schemas_for_discovery': 'list[str]',
            'sensitive_type_ids_for_discovery': 'list[str]',
            'is_sample_data_collection_enabled': 'bool',
            'is_app_defined_relation_discovery_enabled': 'bool',
            'is_include_all_schemas': 'bool',
            'is_include_all_sensitive_types': 'bool',
            'total_schemas_scanned': 'int',
            'total_objects_scanned': 'int',
            'total_columns_scanned': 'int',
            'total_new_sensitive_columns': 'int',
            'total_modified_sensitive_columns': 'int',
            'total_deleted_sensitive_columns': 'int',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'discovery_type': 'discoveryType',
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'time_started': 'timeStarted',
            'time_finished': 'timeFinished',
            'lifecycle_state': 'lifecycleState',
            'sensitive_data_model_id': 'sensitiveDataModelId',
            'target_id': 'targetId',
            'schemas_for_discovery': 'schemasForDiscovery',
            'sensitive_type_ids_for_discovery': 'sensitiveTypeIdsForDiscovery',
            'is_sample_data_collection_enabled': 'isSampleDataCollectionEnabled',
            'is_app_defined_relation_discovery_enabled': 'isAppDefinedRelationDiscoveryEnabled',
            'is_include_all_schemas': 'isIncludeAllSchemas',
            'is_include_all_sensitive_types': 'isIncludeAllSensitiveTypes',
            'total_schemas_scanned': 'totalSchemasScanned',
            'total_objects_scanned': 'totalObjectsScanned',
            'total_columns_scanned': 'totalColumnsScanned',
            'total_new_sensitive_columns': 'totalNewSensitiveColumns',
            'total_modified_sensitive_columns': 'totalModifiedSensitiveColumns',
            'total_deleted_sensitive_columns': 'totalDeletedSensitiveColumns',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._id = None
        self._discovery_type = None
        self._display_name = None
        self._compartment_id = None
        self._time_started = None
        self._time_finished = None
        self._lifecycle_state = None
        self._sensitive_data_model_id = None
        self._target_id = None
        self._schemas_for_discovery = None
        self._sensitive_type_ids_for_discovery = None
        self._is_sample_data_collection_enabled = None
        self._is_app_defined_relation_discovery_enabled = None
        self._is_include_all_schemas = None
        self._is_include_all_sensitive_types = None
        self._total_schemas_scanned = None
        self._total_objects_scanned = None
        self._total_columns_scanned = None
        self._total_new_sensitive_columns = None
        self._total_modified_sensitive_columns = None
        self._total_deleted_sensitive_columns = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this DiscoveryJob.
        The OCID of the discovery job.


        :return: The id of this DiscoveryJob.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DiscoveryJob.
        The OCID of the discovery job.


        :param id: The id of this DiscoveryJob.
        :type: str
        """
        self._id = id

    @property
    def discovery_type(self):
        """
        **[Required]** Gets the discovery_type of this DiscoveryJob.
        The type of the discovery job. It defines the job's scope.
        NEW identifies new sensitive columns in the target database that are not in the sensitive data model.
        DELETED identifies columns that are present in the sensitive data model but have been deleted from the target database.
        MODIFIED identifies columns that are present in the target database as well as the sensitive data model but some of their attributes have been modified.
        ALL covers all the above three scenarios and reports new, deleted and modified columns.

        Allowed values for this property are: "ALL", "NEW", "MODIFIED", "DELETED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The discovery_type of this DiscoveryJob.
        :rtype: str
        """
        return self._discovery_type

    @discovery_type.setter
    def discovery_type(self, discovery_type):
        """
        Sets the discovery_type of this DiscoveryJob.
        The type of the discovery job. It defines the job's scope.
        NEW identifies new sensitive columns in the target database that are not in the sensitive data model.
        DELETED identifies columns that are present in the sensitive data model but have been deleted from the target database.
        MODIFIED identifies columns that are present in the target database as well as the sensitive data model but some of their attributes have been modified.
        ALL covers all the above three scenarios and reports new, deleted and modified columns.


        :param discovery_type: The discovery_type of this DiscoveryJob.
        :type: str
        """
        allowed_values = ["ALL", "NEW", "MODIFIED", "DELETED"]
        if not value_allowed_none_or_none_sentinel(discovery_type, allowed_values):
            discovery_type = 'UNKNOWN_ENUM_VALUE'
        self._discovery_type = discovery_type

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this DiscoveryJob.
        The display name of the discovery job.


        :return: The display_name of this DiscoveryJob.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this DiscoveryJob.
        The display name of the discovery job.


        :param display_name: The display_name of this DiscoveryJob.
        :type: str
        """
        self._display_name = display_name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this DiscoveryJob.
        The OCID of the compartment that contains the discovery job.


        :return: The compartment_id of this DiscoveryJob.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this DiscoveryJob.
        The OCID of the compartment that contains the discovery job.


        :param compartment_id: The compartment_id of this DiscoveryJob.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def time_started(self):
        """
        **[Required]** Gets the time_started of this DiscoveryJob.
        The date and time the discovery job started, in the format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_started of this DiscoveryJob.
        :rtype: datetime
        """
        return self._time_started

    @time_started.setter
    def time_started(self, time_started):
        """
        Sets the time_started of this DiscoveryJob.
        The date and time the discovery job started, in the format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :param time_started: The time_started of this DiscoveryJob.
        :type: datetime
        """
        self._time_started = time_started

    @property
    def time_finished(self):
        """
        **[Required]** Gets the time_finished of this DiscoveryJob.
        The date and time the discovery job finished, in the format defined by `RFC3339`__..

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_finished of this DiscoveryJob.
        :rtype: datetime
        """
        return self._time_finished

    @time_finished.setter
    def time_finished(self, time_finished):
        """
        Sets the time_finished of this DiscoveryJob.
        The date and time the discovery job finished, in the format defined by `RFC3339`__..

        __ https://tools.ietf.org/html/rfc3339


        :param time_finished: The time_finished of this DiscoveryJob.
        :type: datetime
        """
        self._time_finished = time_finished

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this DiscoveryJob.
        The current state of the discovery job.

        Allowed values for this property are: "CREATING", "ACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this DiscoveryJob.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this DiscoveryJob.
        The current state of the discovery job.


        :param lifecycle_state: The lifecycle_state of this DiscoveryJob.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def sensitive_data_model_id(self):
        """
        **[Required]** Gets the sensitive_data_model_id of this DiscoveryJob.
        The OCID of the sensitive data model associated with the discovery job.


        :return: The sensitive_data_model_id of this DiscoveryJob.
        :rtype: str
        """
        return self._sensitive_data_model_id

    @sensitive_data_model_id.setter
    def sensitive_data_model_id(self, sensitive_data_model_id):
        """
        Sets the sensitive_data_model_id of this DiscoveryJob.
        The OCID of the sensitive data model associated with the discovery job.


        :param sensitive_data_model_id: The sensitive_data_model_id of this DiscoveryJob.
        :type: str
        """
        self._sensitive_data_model_id = sensitive_data_model_id

    @property
    def target_id(self):
        """
        **[Required]** Gets the target_id of this DiscoveryJob.
        The OCID of the target database associated with the discovery job.


        :return: The target_id of this DiscoveryJob.
        :rtype: str
        """
        return self._target_id

    @target_id.setter
    def target_id(self, target_id):
        """
        Sets the target_id of this DiscoveryJob.
        The OCID of the target database associated with the discovery job.


        :param target_id: The target_id of this DiscoveryJob.
        :type: str
        """
        self._target_id = target_id

    @property
    def schemas_for_discovery(self):
        """
        Gets the schemas_for_discovery of this DiscoveryJob.
        The schemas used for data discovery.


        :return: The schemas_for_discovery of this DiscoveryJob.
        :rtype: list[str]
        """
        return self._schemas_for_discovery

    @schemas_for_discovery.setter
    def schemas_for_discovery(self, schemas_for_discovery):
        """
        Sets the schemas_for_discovery of this DiscoveryJob.
        The schemas used for data discovery.


        :param schemas_for_discovery: The schemas_for_discovery of this DiscoveryJob.
        :type: list[str]
        """
        self._schemas_for_discovery = schemas_for_discovery

    @property
    def sensitive_type_ids_for_discovery(self):
        """
        Gets the sensitive_type_ids_for_discovery of this DiscoveryJob.
        The OCIDs of the sensitive types used for data discovery.


        :return: The sensitive_type_ids_for_discovery of this DiscoveryJob.
        :rtype: list[str]
        """
        return self._sensitive_type_ids_for_discovery

    @sensitive_type_ids_for_discovery.setter
    def sensitive_type_ids_for_discovery(self, sensitive_type_ids_for_discovery):
        """
        Sets the sensitive_type_ids_for_discovery of this DiscoveryJob.
        The OCIDs of the sensitive types used for data discovery.


        :param sensitive_type_ids_for_discovery: The sensitive_type_ids_for_discovery of this DiscoveryJob.
        :type: list[str]
        """
        self._sensitive_type_ids_for_discovery = sensitive_type_ids_for_discovery

    @property
    def is_sample_data_collection_enabled(self):
        """
        **[Required]** Gets the is_sample_data_collection_enabled of this DiscoveryJob.
        Indicates if the discovery job should collect and store sample data values for the discovered columns.
        Sample data helps review the discovered columns and ensure that they actually contain sensitive data.
        As it collects original data from the target database, it's disabled by default and should be used only
        if it's acceptable to store sample data in Data Safe's repository in Oracle Cloud. Note that sample data
        values are not collected for columns with the following data types: LONG, LOB, RAW, XMLTYPE and BFILE.


        :return: The is_sample_data_collection_enabled of this DiscoveryJob.
        :rtype: bool
        """
        return self._is_sample_data_collection_enabled

    @is_sample_data_collection_enabled.setter
    def is_sample_data_collection_enabled(self, is_sample_data_collection_enabled):
        """
        Sets the is_sample_data_collection_enabled of this DiscoveryJob.
        Indicates if the discovery job should collect and store sample data values for the discovered columns.
        Sample data helps review the discovered columns and ensure that they actually contain sensitive data.
        As it collects original data from the target database, it's disabled by default and should be used only
        if it's acceptable to store sample data in Data Safe's repository in Oracle Cloud. Note that sample data
        values are not collected for columns with the following data types: LONG, LOB, RAW, XMLTYPE and BFILE.


        :param is_sample_data_collection_enabled: The is_sample_data_collection_enabled of this DiscoveryJob.
        :type: bool
        """
        self._is_sample_data_collection_enabled = is_sample_data_collection_enabled

    @property
    def is_app_defined_relation_discovery_enabled(self):
        """
        **[Required]** Gets the is_app_defined_relation_discovery_enabled of this DiscoveryJob.
        Indicates if the discovery job should identify potential application-level (non-dictionary) referential
        relationships between columns. Note that data discovery automatically identifies and adds database-level (dictionary-defined)
        relationships. This option helps identify application-level relationships that are not defined in the database dictionary,
        which in turn, helps identify additional sensitive columns and preserve referential integrity during data masking.
        It's disabled by default and should be used only if there is a need to identify application-level relationships.


        :return: The is_app_defined_relation_discovery_enabled of this DiscoveryJob.
        :rtype: bool
        """
        return self._is_app_defined_relation_discovery_enabled

    @is_app_defined_relation_discovery_enabled.setter
    def is_app_defined_relation_discovery_enabled(self, is_app_defined_relation_discovery_enabled):
        """
        Sets the is_app_defined_relation_discovery_enabled of this DiscoveryJob.
        Indicates if the discovery job should identify potential application-level (non-dictionary) referential
        relationships between columns. Note that data discovery automatically identifies and adds database-level (dictionary-defined)
        relationships. This option helps identify application-level relationships that are not defined in the database dictionary,
        which in turn, helps identify additional sensitive columns and preserve referential integrity during data masking.
        It's disabled by default and should be used only if there is a need to identify application-level relationships.


        :param is_app_defined_relation_discovery_enabled: The is_app_defined_relation_discovery_enabled of this DiscoveryJob.
        :type: bool
        """
        self._is_app_defined_relation_discovery_enabled = is_app_defined_relation_discovery_enabled

    @property
    def is_include_all_schemas(self):
        """
        **[Required]** Gets the is_include_all_schemas of this DiscoveryJob.
        Indicates if all the schemas in the associated target database are used for data discovery.
        If it's set to true, the schemasForDiscovery attribute is ignored and all schemas are used.


        :return: The is_include_all_schemas of this DiscoveryJob.
        :rtype: bool
        """
        return self._is_include_all_schemas

    @is_include_all_schemas.setter
    def is_include_all_schemas(self, is_include_all_schemas):
        """
        Sets the is_include_all_schemas of this DiscoveryJob.
        Indicates if all the schemas in the associated target database are used for data discovery.
        If it's set to true, the schemasForDiscovery attribute is ignored and all schemas are used.


        :param is_include_all_schemas: The is_include_all_schemas of this DiscoveryJob.
        :type: bool
        """
        self._is_include_all_schemas = is_include_all_schemas

    @property
    def is_include_all_sensitive_types(self):
        """
        **[Required]** Gets the is_include_all_sensitive_types of this DiscoveryJob.
        Indicates if all the existing sensitive types are used for data discovery. If it's set to true, the
        sensitiveTypeIdsForDiscovery attribute is ignored and all sensitive types are used.


        :return: The is_include_all_sensitive_types of this DiscoveryJob.
        :rtype: bool
        """
        return self._is_include_all_sensitive_types

    @is_include_all_sensitive_types.setter
    def is_include_all_sensitive_types(self, is_include_all_sensitive_types):
        """
        Sets the is_include_all_sensitive_types of this DiscoveryJob.
        Indicates if all the existing sensitive types are used for data discovery. If it's set to true, the
        sensitiveTypeIdsForDiscovery attribute is ignored and all sensitive types are used.


        :param is_include_all_sensitive_types: The is_include_all_sensitive_types of this DiscoveryJob.
        :type: bool
        """
        self._is_include_all_sensitive_types = is_include_all_sensitive_types

    @property
    def total_schemas_scanned(self):
        """
        **[Required]** Gets the total_schemas_scanned of this DiscoveryJob.
        The total number of schemas scanned by the discovery job.


        :return: The total_schemas_scanned of this DiscoveryJob.
        :rtype: int
        """
        return self._total_schemas_scanned

    @total_schemas_scanned.setter
    def total_schemas_scanned(self, total_schemas_scanned):
        """
        Sets the total_schemas_scanned of this DiscoveryJob.
        The total number of schemas scanned by the discovery job.


        :param total_schemas_scanned: The total_schemas_scanned of this DiscoveryJob.
        :type: int
        """
        self._total_schemas_scanned = total_schemas_scanned

    @property
    def total_objects_scanned(self):
        """
        **[Required]** Gets the total_objects_scanned of this DiscoveryJob.
        The total number of objects (tables and editioning views) scanned by the discovery job.


        :return: The total_objects_scanned of this DiscoveryJob.
        :rtype: int
        """
        return self._total_objects_scanned

    @total_objects_scanned.setter
    def total_objects_scanned(self, total_objects_scanned):
        """
        Sets the total_objects_scanned of this DiscoveryJob.
        The total number of objects (tables and editioning views) scanned by the discovery job.


        :param total_objects_scanned: The total_objects_scanned of this DiscoveryJob.
        :type: int
        """
        self._total_objects_scanned = total_objects_scanned

    @property
    def total_columns_scanned(self):
        """
        **[Required]** Gets the total_columns_scanned of this DiscoveryJob.
        The total number of columns scanned by the discovery job.


        :return: The total_columns_scanned of this DiscoveryJob.
        :rtype: int
        """
        return self._total_columns_scanned

    @total_columns_scanned.setter
    def total_columns_scanned(self, total_columns_scanned):
        """
        Sets the total_columns_scanned of this DiscoveryJob.
        The total number of columns scanned by the discovery job.


        :param total_columns_scanned: The total_columns_scanned of this DiscoveryJob.
        :type: int
        """
        self._total_columns_scanned = total_columns_scanned

    @property
    def total_new_sensitive_columns(self):
        """
        **[Required]** Gets the total_new_sensitive_columns of this DiscoveryJob.
        The total number of new sensitive columns identified by the discovery job.


        :return: The total_new_sensitive_columns of this DiscoveryJob.
        :rtype: int
        """
        return self._total_new_sensitive_columns

    @total_new_sensitive_columns.setter
    def total_new_sensitive_columns(self, total_new_sensitive_columns):
        """
        Sets the total_new_sensitive_columns of this DiscoveryJob.
        The total number of new sensitive columns identified by the discovery job.


        :param total_new_sensitive_columns: The total_new_sensitive_columns of this DiscoveryJob.
        :type: int
        """
        self._total_new_sensitive_columns = total_new_sensitive_columns

    @property
    def total_modified_sensitive_columns(self):
        """
        **[Required]** Gets the total_modified_sensitive_columns of this DiscoveryJob.
        The total number of modified sensitive columns identified by the discovery job.


        :return: The total_modified_sensitive_columns of this DiscoveryJob.
        :rtype: int
        """
        return self._total_modified_sensitive_columns

    @total_modified_sensitive_columns.setter
    def total_modified_sensitive_columns(self, total_modified_sensitive_columns):
        """
        Sets the total_modified_sensitive_columns of this DiscoveryJob.
        The total number of modified sensitive columns identified by the discovery job.


        :param total_modified_sensitive_columns: The total_modified_sensitive_columns of this DiscoveryJob.
        :type: int
        """
        self._total_modified_sensitive_columns = total_modified_sensitive_columns

    @property
    def total_deleted_sensitive_columns(self):
        """
        **[Required]** Gets the total_deleted_sensitive_columns of this DiscoveryJob.
        The total number of deleted sensitive columns identified by the discovery job.


        :return: The total_deleted_sensitive_columns of this DiscoveryJob.
        :rtype: int
        """
        return self._total_deleted_sensitive_columns

    @total_deleted_sensitive_columns.setter
    def total_deleted_sensitive_columns(self, total_deleted_sensitive_columns):
        """
        Sets the total_deleted_sensitive_columns of this DiscoveryJob.
        The total number of deleted sensitive columns identified by the discovery job.


        :param total_deleted_sensitive_columns: The total_deleted_sensitive_columns of this DiscoveryJob.
        :type: int
        """
        self._total_deleted_sensitive_columns = total_deleted_sensitive_columns

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this DiscoveryJob.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see `Resource Tags`__

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this DiscoveryJob.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this DiscoveryJob.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see `Resource Tags`__

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this DiscoveryJob.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this DiscoveryJob.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this DiscoveryJob.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this DiscoveryJob.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this DiscoveryJob.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this DiscoveryJob.
        System tags for this resource. Each key is predefined and scoped to a namespace. For more information, see Resource Tags.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this DiscoveryJob.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this DiscoveryJob.
        System tags for this resource. Each key is predefined and scoped to a namespace. For more information, see Resource Tags.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this DiscoveryJob.
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
