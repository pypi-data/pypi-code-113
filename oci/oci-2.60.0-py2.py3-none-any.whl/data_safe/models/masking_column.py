# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MaskingColumn(object):
    """
    A masking column is a resource corresponding to a database column that you want to
    mask. It's a subresource of masking policy resource and is always associated with
    a masking policy. Note that only parent columns are managed as masking columns.
    The child columns are automatically managed using the childColumns attribute.
    """

    #: A constant which can be used with the lifecycle_state property of a MaskingColumn.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a MaskingColumn.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a MaskingColumn.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a MaskingColumn.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a MaskingColumn.
    #: This constant has a value of "NEEDS_ATTENTION"
    LIFECYCLE_STATE_NEEDS_ATTENTION = "NEEDS_ATTENTION"

    #: A constant which can be used with the lifecycle_state property of a MaskingColumn.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the object_type property of a MaskingColumn.
    #: This constant has a value of "TABLE"
    OBJECT_TYPE_TABLE = "TABLE"

    #: A constant which can be used with the object_type property of a MaskingColumn.
    #: This constant has a value of "EDITIONING_VIEW"
    OBJECT_TYPE_EDITIONING_VIEW = "EDITIONING_VIEW"

    def __init__(self, **kwargs):
        """
        Initializes a new MaskingColumn object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this MaskingColumn.
        :type key: str

        :param masking_policy_id:
            The value to assign to the masking_policy_id property of this MaskingColumn.
        :type masking_policy_id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this MaskingColumn.
            Allowed values for this property are: "CREATING", "ACTIVE", "UPDATING", "DELETING", "NEEDS_ATTENTION", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this MaskingColumn.
        :type lifecycle_details: str

        :param time_created:
            The value to assign to the time_created property of this MaskingColumn.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this MaskingColumn.
        :type time_updated: datetime

        :param schema_name:
            The value to assign to the schema_name property of this MaskingColumn.
        :type schema_name: str

        :param object_name:
            The value to assign to the object_name property of this MaskingColumn.
        :type object_name: str

        :param object_type:
            The value to assign to the object_type property of this MaskingColumn.
            Allowed values for this property are: "TABLE", "EDITIONING_VIEW", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type object_type: str

        :param column_name:
            The value to assign to the column_name property of this MaskingColumn.
        :type column_name: str

        :param child_columns:
            The value to assign to the child_columns property of this MaskingColumn.
        :type child_columns: list[str]

        :param masking_column_group:
            The value to assign to the masking_column_group property of this MaskingColumn.
        :type masking_column_group: str

        :param sensitive_type_id:
            The value to assign to the sensitive_type_id property of this MaskingColumn.
        :type sensitive_type_id: str

        :param is_masking_enabled:
            The value to assign to the is_masking_enabled property of this MaskingColumn.
        :type is_masking_enabled: bool

        :param data_type:
            The value to assign to the data_type property of this MaskingColumn.
        :type data_type: str

        :param masking_formats:
            The value to assign to the masking_formats property of this MaskingColumn.
        :type masking_formats: list[oci.data_safe.models.MaskingFormat]

        """
        self.swagger_types = {
            'key': 'str',
            'masking_policy_id': 'str',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'schema_name': 'str',
            'object_name': 'str',
            'object_type': 'str',
            'column_name': 'str',
            'child_columns': 'list[str]',
            'masking_column_group': 'str',
            'sensitive_type_id': 'str',
            'is_masking_enabled': 'bool',
            'data_type': 'str',
            'masking_formats': 'list[MaskingFormat]'
        }

        self.attribute_map = {
            'key': 'key',
            'masking_policy_id': 'maskingPolicyId',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'schema_name': 'schemaName',
            'object_name': 'objectName',
            'object_type': 'objectType',
            'column_name': 'columnName',
            'child_columns': 'childColumns',
            'masking_column_group': 'maskingColumnGroup',
            'sensitive_type_id': 'sensitiveTypeId',
            'is_masking_enabled': 'isMaskingEnabled',
            'data_type': 'dataType',
            'masking_formats': 'maskingFormats'
        }

        self._key = None
        self._masking_policy_id = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._time_created = None
        self._time_updated = None
        self._schema_name = None
        self._object_name = None
        self._object_type = None
        self._column_name = None
        self._child_columns = None
        self._masking_column_group = None
        self._sensitive_type_id = None
        self._is_masking_enabled = None
        self._data_type = None
        self._masking_formats = None

    @property
    def key(self):
        """
        **[Required]** Gets the key of this MaskingColumn.
        The unique key that identifies the masking column. It's numeric and unique within a masking policy.


        :return: The key of this MaskingColumn.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this MaskingColumn.
        The unique key that identifies the masking column. It's numeric and unique within a masking policy.


        :param key: The key of this MaskingColumn.
        :type: str
        """
        self._key = key

    @property
    def masking_policy_id(self):
        """
        **[Required]** Gets the masking_policy_id of this MaskingColumn.
        The OCID of the masking policy that contains the masking column.


        :return: The masking_policy_id of this MaskingColumn.
        :rtype: str
        """
        return self._masking_policy_id

    @masking_policy_id.setter
    def masking_policy_id(self, masking_policy_id):
        """
        Sets the masking_policy_id of this MaskingColumn.
        The OCID of the masking policy that contains the masking column.


        :param masking_policy_id: The masking_policy_id of this MaskingColumn.
        :type: str
        """
        self._masking_policy_id = masking_policy_id

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this MaskingColumn.
        The current state of the masking column.

        Allowed values for this property are: "CREATING", "ACTIVE", "UPDATING", "DELETING", "NEEDS_ATTENTION", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this MaskingColumn.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this MaskingColumn.
        The current state of the masking column.


        :param lifecycle_state: The lifecycle_state of this MaskingColumn.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "UPDATING", "DELETING", "NEEDS_ATTENTION", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this MaskingColumn.
        Details about the current state of the masking column.


        :return: The lifecycle_details of this MaskingColumn.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this MaskingColumn.
        Details about the current state of the masking column.


        :param lifecycle_details: The lifecycle_details of this MaskingColumn.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this MaskingColumn.
        The date and time the masking column was created, in the format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this MaskingColumn.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this MaskingColumn.
        The date and time the masking column was created, in the format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this MaskingColumn.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this MaskingColumn.
        The date and time the masking column was last updated, in the format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_updated of this MaskingColumn.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this MaskingColumn.
        The date and time the masking column was last updated, in the format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :param time_updated: The time_updated of this MaskingColumn.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def schema_name(self):
        """
        **[Required]** Gets the schema_name of this MaskingColumn.
        The name of the schema that contains the database column.


        :return: The schema_name of this MaskingColumn.
        :rtype: str
        """
        return self._schema_name

    @schema_name.setter
    def schema_name(self, schema_name):
        """
        Sets the schema_name of this MaskingColumn.
        The name of the schema that contains the database column.


        :param schema_name: The schema_name of this MaskingColumn.
        :type: str
        """
        self._schema_name = schema_name

    @property
    def object_name(self):
        """
        **[Required]** Gets the object_name of this MaskingColumn.
        The name of the object (table or editioning view) that contains the database column.


        :return: The object_name of this MaskingColumn.
        :rtype: str
        """
        return self._object_name

    @object_name.setter
    def object_name(self, object_name):
        """
        Sets the object_name of this MaskingColumn.
        The name of the object (table or editioning view) that contains the database column.


        :param object_name: The object_name of this MaskingColumn.
        :type: str
        """
        self._object_name = object_name

    @property
    def object_type(self):
        """
        Gets the object_type of this MaskingColumn.
        The type of the object that contains the database column.

        Allowed values for this property are: "TABLE", "EDITIONING_VIEW", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The object_type of this MaskingColumn.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this MaskingColumn.
        The type of the object that contains the database column.


        :param object_type: The object_type of this MaskingColumn.
        :type: str
        """
        allowed_values = ["TABLE", "EDITIONING_VIEW"]
        if not value_allowed_none_or_none_sentinel(object_type, allowed_values):
            object_type = 'UNKNOWN_ENUM_VALUE'
        self._object_type = object_type

    @property
    def column_name(self):
        """
        **[Required]** Gets the column_name of this MaskingColumn.
        The name of the database column. Note that the same name is used for the masking column.
        There is no separate displayName attribute for the masking column.


        :return: The column_name of this MaskingColumn.
        :rtype: str
        """
        return self._column_name

    @column_name.setter
    def column_name(self, column_name):
        """
        Sets the column_name of this MaskingColumn.
        The name of the database column. Note that the same name is used for the masking column.
        There is no separate displayName attribute for the masking column.


        :param column_name: The column_name of this MaskingColumn.
        :type: str
        """
        self._column_name = column_name

    @property
    def child_columns(self):
        """
        Gets the child_columns of this MaskingColumn.
        An array of child columns that are in referential relationship with the masking column.


        :return: The child_columns of this MaskingColumn.
        :rtype: list[str]
        """
        return self._child_columns

    @child_columns.setter
    def child_columns(self, child_columns):
        """
        Sets the child_columns of this MaskingColumn.
        An array of child columns that are in referential relationship with the masking column.


        :param child_columns: The child_columns of this MaskingColumn.
        :type: list[str]
        """
        self._child_columns = child_columns

    @property
    def masking_column_group(self):
        """
        Gets the masking_column_group of this MaskingColumn.
        The group of the masking column. All the columns in a group are masked together to ensure
        that the masked data across these columns continue to retain the same logical relationship.
        For more details, check <a href=https://docs.oracle.com/en/cloud/paas/data-safe/udscs/group-masking1.html#GUID-755056B9-9540-48C0-9491-262A44A85037>Group Masking in the Data Safe documentation.</a>


        :return: The masking_column_group of this MaskingColumn.
        :rtype: str
        """
        return self._masking_column_group

    @masking_column_group.setter
    def masking_column_group(self, masking_column_group):
        """
        Sets the masking_column_group of this MaskingColumn.
        The group of the masking column. All the columns in a group are masked together to ensure
        that the masked data across these columns continue to retain the same logical relationship.
        For more details, check <a href=https://docs.oracle.com/en/cloud/paas/data-safe/udscs/group-masking1.html#GUID-755056B9-9540-48C0-9491-262A44A85037>Group Masking in the Data Safe documentation.</a>


        :param masking_column_group: The masking_column_group of this MaskingColumn.
        :type: str
        """
        self._masking_column_group = masking_column_group

    @property
    def sensitive_type_id(self):
        """
        Gets the sensitive_type_id of this MaskingColumn.
        The OCID of the sensitive type associated with the masking column.


        :return: The sensitive_type_id of this MaskingColumn.
        :rtype: str
        """
        return self._sensitive_type_id

    @sensitive_type_id.setter
    def sensitive_type_id(self, sensitive_type_id):
        """
        Sets the sensitive_type_id of this MaskingColumn.
        The OCID of the sensitive type associated with the masking column.


        :param sensitive_type_id: The sensitive_type_id of this MaskingColumn.
        :type: str
        """
        self._sensitive_type_id = sensitive_type_id

    @property
    def is_masking_enabled(self):
        """
        **[Required]** Gets the is_masking_enabled of this MaskingColumn.
        Indicates if data masking is enabled for the masking column.


        :return: The is_masking_enabled of this MaskingColumn.
        :rtype: bool
        """
        return self._is_masking_enabled

    @is_masking_enabled.setter
    def is_masking_enabled(self, is_masking_enabled):
        """
        Sets the is_masking_enabled of this MaskingColumn.
        Indicates if data masking is enabled for the masking column.


        :param is_masking_enabled: The is_masking_enabled of this MaskingColumn.
        :type: bool
        """
        self._is_masking_enabled = is_masking_enabled

    @property
    def data_type(self):
        """
        Gets the data_type of this MaskingColumn.
        The data type of the masking column.


        :return: The data_type of this MaskingColumn.
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """
        Sets the data_type of this MaskingColumn.
        The data type of the masking column.


        :param data_type: The data_type of this MaskingColumn.
        :type: str
        """
        self._data_type = data_type

    @property
    def masking_formats(self):
        """
        Gets the masking_formats of this MaskingColumn.
        An array of masking formats assigned to the masking column.


        :return: The masking_formats of this MaskingColumn.
        :rtype: list[oci.data_safe.models.MaskingFormat]
        """
        return self._masking_formats

    @masking_formats.setter
    def masking_formats(self, masking_formats):
        """
        Sets the masking_formats of this MaskingColumn.
        An array of masking formats assigned to the masking column.


        :param masking_formats: The masking_formats of this MaskingColumn.
        :type: list[oci.data_safe.models.MaskingFormat]
        """
        self._masking_formats = masking_formats

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
