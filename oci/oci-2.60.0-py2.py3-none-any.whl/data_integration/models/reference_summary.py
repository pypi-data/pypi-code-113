# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ReferenceSummary(object):
    """
    This is the reference summary information.
    """

    #: A constant which can be used with the type property of a ReferenceSummary.
    #: This constant has a value of "ORACLE_DATA_ASSET"
    TYPE_ORACLE_DATA_ASSET = "ORACLE_DATA_ASSET"

    #: A constant which can be used with the type property of a ReferenceSummary.
    #: This constant has a value of "ORACLE_OBJECT_STORAGE_DATA_ASSET"
    TYPE_ORACLE_OBJECT_STORAGE_DATA_ASSET = "ORACLE_OBJECT_STORAGE_DATA_ASSET"

    #: A constant which can be used with the type property of a ReferenceSummary.
    #: This constant has a value of "ORACLE_ATP_DATA_ASSET"
    TYPE_ORACLE_ATP_DATA_ASSET = "ORACLE_ATP_DATA_ASSET"

    #: A constant which can be used with the type property of a ReferenceSummary.
    #: This constant has a value of "ORACLE_ADWC_DATA_ASSET"
    TYPE_ORACLE_ADWC_DATA_ASSET = "ORACLE_ADWC_DATA_ASSET"

    #: A constant which can be used with the type property of a ReferenceSummary.
    #: This constant has a value of "MYSQL_DATA_ASSET"
    TYPE_MYSQL_DATA_ASSET = "MYSQL_DATA_ASSET"

    #: A constant which can be used with the type property of a ReferenceSummary.
    #: This constant has a value of "GENERIC_JDBC_DATA_ASSET"
    TYPE_GENERIC_JDBC_DATA_ASSET = "GENERIC_JDBC_DATA_ASSET"

    def __init__(self, **kwargs):
        """
        Initializes a new ReferenceSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this ReferenceSummary.
        :type key: str

        :param name:
            The value to assign to the name property of this ReferenceSummary.
        :type name: str

        :param identifier:
            The value to assign to the identifier property of this ReferenceSummary.
        :type identifier: str

        :param identifier_path:
            The value to assign to the identifier_path property of this ReferenceSummary.
        :type identifier_path: str

        :param description:
            The value to assign to the description property of this ReferenceSummary.
        :type description: str

        :param type:
            The value to assign to the type property of this ReferenceSummary.
            Allowed values for this property are: "ORACLE_DATA_ASSET", "ORACLE_OBJECT_STORAGE_DATA_ASSET", "ORACLE_ATP_DATA_ASSET", "ORACLE_ADWC_DATA_ASSET", "MYSQL_DATA_ASSET", "GENERIC_JDBC_DATA_ASSET", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param target_object:
            The value to assign to the target_object property of this ReferenceSummary.
        :type target_object: object

        :param aggregator_key:
            The value to assign to the aggregator_key property of this ReferenceSummary.
        :type aggregator_key: str

        :param used_by:
            The value to assign to the used_by property of this ReferenceSummary.
        :type used_by: list[oci.data_integration.models.ReferenceUsedBy]

        :param child_references:
            The value to assign to the child_references property of this ReferenceSummary.
        :type child_references: list[oci.data_integration.models.ChildReference]

        """
        self.swagger_types = {
            'key': 'str',
            'name': 'str',
            'identifier': 'str',
            'identifier_path': 'str',
            'description': 'str',
            'type': 'str',
            'target_object': 'object',
            'aggregator_key': 'str',
            'used_by': 'list[ReferenceUsedBy]',
            'child_references': 'list[ChildReference]'
        }

        self.attribute_map = {
            'key': 'key',
            'name': 'name',
            'identifier': 'identifier',
            'identifier_path': 'identifierPath',
            'description': 'description',
            'type': 'type',
            'target_object': 'targetObject',
            'aggregator_key': 'aggregatorKey',
            'used_by': 'usedBy',
            'child_references': 'childReferences'
        }

        self._key = None
        self._name = None
        self._identifier = None
        self._identifier_path = None
        self._description = None
        self._type = None
        self._target_object = None
        self._aggregator_key = None
        self._used_by = None
        self._child_references = None

    @property
    def key(self):
        """
        Gets the key of this ReferenceSummary.
        The reference's key, key of the object that is being used by a published object or its dependents.


        :return: The key of this ReferenceSummary.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this ReferenceSummary.
        The reference's key, key of the object that is being used by a published object or its dependents.


        :param key: The key of this ReferenceSummary.
        :type: str
        """
        self._key = key

    @property
    def name(self):
        """
        Gets the name of this ReferenceSummary.
        The name of reference object.


        :return: The name of this ReferenceSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ReferenceSummary.
        The name of reference object.


        :param name: The name of this ReferenceSummary.
        :type: str
        """
        self._name = name

    @property
    def identifier(self):
        """
        Gets the identifier of this ReferenceSummary.
        The identifier of reference object.


        :return: The identifier of this ReferenceSummary.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """
        Sets the identifier of this ReferenceSummary.
        The identifier of reference object.


        :param identifier: The identifier of this ReferenceSummary.
        :type: str
        """
        self._identifier = identifier

    @property
    def identifier_path(self):
        """
        Gets the identifier_path of this ReferenceSummary.
        The identifier path of reference object.


        :return: The identifier_path of this ReferenceSummary.
        :rtype: str
        """
        return self._identifier_path

    @identifier_path.setter
    def identifier_path(self, identifier_path):
        """
        Sets the identifier_path of this ReferenceSummary.
        The identifier path of reference object.


        :param identifier_path: The identifier_path of this ReferenceSummary.
        :type: str
        """
        self._identifier_path = identifier_path

    @property
    def description(self):
        """
        Gets the description of this ReferenceSummary.
        The description of reference object.


        :return: The description of this ReferenceSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ReferenceSummary.
        The description of reference object.


        :param description: The description of this ReferenceSummary.
        :type: str
        """
        self._description = description

    @property
    def type(self):
        """
        Gets the type of this ReferenceSummary.
        The type of reference object.

        Allowed values for this property are: "ORACLE_DATA_ASSET", "ORACLE_OBJECT_STORAGE_DATA_ASSET", "ORACLE_ATP_DATA_ASSET", "ORACLE_ADWC_DATA_ASSET", "MYSQL_DATA_ASSET", "GENERIC_JDBC_DATA_ASSET", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this ReferenceSummary.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this ReferenceSummary.
        The type of reference object.


        :param type: The type of this ReferenceSummary.
        :type: str
        """
        allowed_values = ["ORACLE_DATA_ASSET", "ORACLE_OBJECT_STORAGE_DATA_ASSET", "ORACLE_ATP_DATA_ASSET", "ORACLE_ADWC_DATA_ASSET", "MYSQL_DATA_ASSET", "GENERIC_JDBC_DATA_ASSET"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    @property
    def target_object(self):
        """
        Gets the target_object of this ReferenceSummary.
        The target object referenced. References are made to data assets and child references are made to connections. The type defining this reference is mentioned in the property type.


        :return: The target_object of this ReferenceSummary.
        :rtype: object
        """
        return self._target_object

    @target_object.setter
    def target_object(self, target_object):
        """
        Sets the target_object of this ReferenceSummary.
        The target object referenced. References are made to data assets and child references are made to connections. The type defining this reference is mentioned in the property type.


        :param target_object: The target_object of this ReferenceSummary.
        :type: object
        """
        self._target_object = target_object

    @property
    def aggregator_key(self):
        """
        Gets the aggregator_key of this ReferenceSummary.
        The aggregator of reference object.


        :return: The aggregator_key of this ReferenceSummary.
        :rtype: str
        """
        return self._aggregator_key

    @aggregator_key.setter
    def aggregator_key(self, aggregator_key):
        """
        Sets the aggregator_key of this ReferenceSummary.
        The aggregator of reference object.


        :param aggregator_key: The aggregator_key of this ReferenceSummary.
        :type: str
        """
        self._aggregator_key = aggregator_key

    @property
    def used_by(self):
        """
        Gets the used_by of this ReferenceSummary.
        List of published objects where this is used.


        :return: The used_by of this ReferenceSummary.
        :rtype: list[oci.data_integration.models.ReferenceUsedBy]
        """
        return self._used_by

    @used_by.setter
    def used_by(self, used_by):
        """
        Sets the used_by of this ReferenceSummary.
        List of published objects where this is used.


        :param used_by: The used_by of this ReferenceSummary.
        :type: list[oci.data_integration.models.ReferenceUsedBy]
        """
        self._used_by = used_by

    @property
    def child_references(self):
        """
        Gets the child_references of this ReferenceSummary.
        List of references that are dependent on this reference.


        :return: The child_references of this ReferenceSummary.
        :rtype: list[oci.data_integration.models.ChildReference]
        """
        return self._child_references

    @child_references.setter
    def child_references(self, child_references):
        """
        Sets the child_references of this ReferenceSummary.
        List of references that are dependent on this reference.


        :param child_references: The child_references of this ReferenceSummary.
        :type: list[oci.data_integration.models.ChildReference]
        """
        self._child_references = child_references

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
