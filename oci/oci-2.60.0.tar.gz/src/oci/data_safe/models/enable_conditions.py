# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class EnableConditions(object):
    """
    The details of the audit policy provisioning conditions.
    """

    #: A constant which can be used with the entity_selection property of a EnableConditions.
    #: This constant has a value of "INCLUDE"
    ENTITY_SELECTION_INCLUDE = "INCLUDE"

    #: A constant which can be used with the entity_selection property of a EnableConditions.
    #: This constant has a value of "EXCLUDE"
    ENTITY_SELECTION_EXCLUDE = "EXCLUDE"

    #: A constant which can be used with the entity_type property of a EnableConditions.
    #: This constant has a value of "USER"
    ENTITY_TYPE_USER = "USER"

    #: A constant which can be used with the entity_type property of a EnableConditions.
    #: This constant has a value of "ROLE"
    ENTITY_TYPE_ROLE = "ROLE"

    #: A constant which can be used with the entity_type property of a EnableConditions.
    #: This constant has a value of "ALL_USERS"
    ENTITY_TYPE_ALL_USERS = "ALL_USERS"

    #: A constant which can be used with the operation_status property of a EnableConditions.
    #: This constant has a value of "SUCCESS"
    OPERATION_STATUS_SUCCESS = "SUCCESS"

    #: A constant which can be used with the operation_status property of a EnableConditions.
    #: This constant has a value of "FAILURE"
    OPERATION_STATUS_FAILURE = "FAILURE"

    #: A constant which can be used with the operation_status property of a EnableConditions.
    #: This constant has a value of "BOTH"
    OPERATION_STATUS_BOTH = "BOTH"

    def __init__(self, **kwargs):
        """
        Initializes a new EnableConditions object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param entity_selection:
            The value to assign to the entity_selection property of this EnableConditions.
            Allowed values for this property are: "INCLUDE", "EXCLUDE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type entity_selection: str

        :param entity_type:
            The value to assign to the entity_type property of this EnableConditions.
            Allowed values for this property are: "USER", "ROLE", "ALL_USERS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type entity_type: str

        :param operation_status:
            The value to assign to the operation_status property of this EnableConditions.
            Allowed values for this property are: "SUCCESS", "FAILURE", "BOTH", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type operation_status: str

        :param entity_names:
            The value to assign to the entity_names property of this EnableConditions.
        :type entity_names: list[str]

        """
        self.swagger_types = {
            'entity_selection': 'str',
            'entity_type': 'str',
            'operation_status': 'str',
            'entity_names': 'list[str]'
        }

        self.attribute_map = {
            'entity_selection': 'entitySelection',
            'entity_type': 'entityType',
            'operation_status': 'operationStatus',
            'entity_names': 'entityNames'
        }

        self._entity_selection = None
        self._entity_type = None
        self._operation_status = None
        self._entity_names = None

    @property
    def entity_selection(self):
        """
        **[Required]** Gets the entity_selection of this EnableConditions.
        The entity include or exclude selection.

        Allowed values for this property are: "INCLUDE", "EXCLUDE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The entity_selection of this EnableConditions.
        :rtype: str
        """
        return self._entity_selection

    @entity_selection.setter
    def entity_selection(self, entity_selection):
        """
        Sets the entity_selection of this EnableConditions.
        The entity include or exclude selection.


        :param entity_selection: The entity_selection of this EnableConditions.
        :type: str
        """
        allowed_values = ["INCLUDE", "EXCLUDE"]
        if not value_allowed_none_or_none_sentinel(entity_selection, allowed_values):
            entity_selection = 'UNKNOWN_ENUM_VALUE'
        self._entity_selection = entity_selection

    @property
    def entity_type(self):
        """
        **[Required]** Gets the entity_type of this EnableConditions.
        The entity type that the policy must be enabled for.

        Allowed values for this property are: "USER", "ROLE", "ALL_USERS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The entity_type of this EnableConditions.
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """
        Sets the entity_type of this EnableConditions.
        The entity type that the policy must be enabled for.


        :param entity_type: The entity_type of this EnableConditions.
        :type: str
        """
        allowed_values = ["USER", "ROLE", "ALL_USERS"]
        if not value_allowed_none_or_none_sentinel(entity_type, allowed_values):
            entity_type = 'UNKNOWN_ENUM_VALUE'
        self._entity_type = entity_type

    @property
    def operation_status(self):
        """
        **[Required]** Gets the operation_status of this EnableConditions.
        The operation status that the policy must be enabled for.

        Allowed values for this property are: "SUCCESS", "FAILURE", "BOTH", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The operation_status of this EnableConditions.
        :rtype: str
        """
        return self._operation_status

    @operation_status.setter
    def operation_status(self, operation_status):
        """
        Sets the operation_status of this EnableConditions.
        The operation status that the policy must be enabled for.


        :param operation_status: The operation_status of this EnableConditions.
        :type: str
        """
        allowed_values = ["SUCCESS", "FAILURE", "BOTH"]
        if not value_allowed_none_or_none_sentinel(operation_status, allowed_values):
            operation_status = 'UNKNOWN_ENUM_VALUE'
        self._operation_status = operation_status

    @property
    def entity_names(self):
        """
        Gets the entity_names of this EnableConditions.
        List of users or roles that the policy must be enabled for.


        :return: The entity_names of this EnableConditions.
        :rtype: list[str]
        """
        return self._entity_names

    @entity_names.setter
    def entity_names(self, entity_names):
        """
        Sets the entity_names of this EnableConditions.
        List of users or roles that the policy must be enabled for.


        :param entity_names: The entity_names of this EnableConditions.
        :type: list[str]
        """
        self._entity_names = entity_names

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
