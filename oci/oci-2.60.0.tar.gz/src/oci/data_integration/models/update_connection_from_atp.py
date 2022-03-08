# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .update_connection_details import UpdateConnectionDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateConnectionFromAtp(UpdateConnectionDetails):
    """
    The details to update an Autonomous Transaction Processing data asset connection.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateConnectionFromAtp object with values from keyword arguments. The default value of the :py:attr:`~oci.data_integration.models.UpdateConnectionFromAtp.model_type` attribute
        of this class is ``ORACLE_ATP_CONNECTION`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this UpdateConnectionFromAtp.
            Allowed values for this property are: "ORACLE_ADWC_CONNECTION", "ORACLE_ATP_CONNECTION", "ORACLE_OBJECT_STORAGE_CONNECTION", "ORACLEDB_CONNECTION", "MYSQL_CONNECTION", "GENERIC_JDBC_CONNECTION", "BICC_CONNECTION", "AMAZON_S3_CONNECTION"
        :type model_type: str

        :param key:
            The value to assign to the key property of this UpdateConnectionFromAtp.
        :type key: str

        :param model_version:
            The value to assign to the model_version property of this UpdateConnectionFromAtp.
        :type model_version: str

        :param parent_ref:
            The value to assign to the parent_ref property of this UpdateConnectionFromAtp.
        :type parent_ref: oci.data_integration.models.ParentReference

        :param name:
            The value to assign to the name property of this UpdateConnectionFromAtp.
        :type name: str

        :param description:
            The value to assign to the description property of this UpdateConnectionFromAtp.
        :type description: str

        :param object_status:
            The value to assign to the object_status property of this UpdateConnectionFromAtp.
        :type object_status: int

        :param object_version:
            The value to assign to the object_version property of this UpdateConnectionFromAtp.
        :type object_version: int

        :param identifier:
            The value to assign to the identifier property of this UpdateConnectionFromAtp.
        :type identifier: str

        :param connection_properties:
            The value to assign to the connection_properties property of this UpdateConnectionFromAtp.
        :type connection_properties: list[oci.data_integration.models.ConnectionProperty]

        :param registry_metadata:
            The value to assign to the registry_metadata property of this UpdateConnectionFromAtp.
        :type registry_metadata: oci.data_integration.models.RegistryMetadata

        :param tns_alias:
            The value to assign to the tns_alias property of this UpdateConnectionFromAtp.
        :type tns_alias: str

        :param tns_names:
            The value to assign to the tns_names property of this UpdateConnectionFromAtp.
        :type tns_names: list[str]

        :param username:
            The value to assign to the username property of this UpdateConnectionFromAtp.
        :type username: str

        :param password:
            The value to assign to the password property of this UpdateConnectionFromAtp.
        :type password: str

        :param password_secret:
            The value to assign to the password_secret property of this UpdateConnectionFromAtp.
        :type password_secret: oci.data_integration.models.SensitiveAttribute

        """
        self.swagger_types = {
            'model_type': 'str',
            'key': 'str',
            'model_version': 'str',
            'parent_ref': 'ParentReference',
            'name': 'str',
            'description': 'str',
            'object_status': 'int',
            'object_version': 'int',
            'identifier': 'str',
            'connection_properties': 'list[ConnectionProperty]',
            'registry_metadata': 'RegistryMetadata',
            'tns_alias': 'str',
            'tns_names': 'list[str]',
            'username': 'str',
            'password': 'str',
            'password_secret': 'SensitiveAttribute'
        }

        self.attribute_map = {
            'model_type': 'modelType',
            'key': 'key',
            'model_version': 'modelVersion',
            'parent_ref': 'parentRef',
            'name': 'name',
            'description': 'description',
            'object_status': 'objectStatus',
            'object_version': 'objectVersion',
            'identifier': 'identifier',
            'connection_properties': 'connectionProperties',
            'registry_metadata': 'registryMetadata',
            'tns_alias': 'tnsAlias',
            'tns_names': 'tnsNames',
            'username': 'username',
            'password': 'password',
            'password_secret': 'passwordSecret'
        }

        self._model_type = None
        self._key = None
        self._model_version = None
        self._parent_ref = None
        self._name = None
        self._description = None
        self._object_status = None
        self._object_version = None
        self._identifier = None
        self._connection_properties = None
        self._registry_metadata = None
        self._tns_alias = None
        self._tns_names = None
        self._username = None
        self._password = None
        self._password_secret = None
        self._model_type = 'ORACLE_ATP_CONNECTION'

    @property
    def tns_alias(self):
        """
        Gets the tns_alias of this UpdateConnectionFromAtp.
        The Autonomous Transaction Processing instance service name.


        :return: The tns_alias of this UpdateConnectionFromAtp.
        :rtype: str
        """
        return self._tns_alias

    @tns_alias.setter
    def tns_alias(self, tns_alias):
        """
        Sets the tns_alias of this UpdateConnectionFromAtp.
        The Autonomous Transaction Processing instance service name.


        :param tns_alias: The tns_alias of this UpdateConnectionFromAtp.
        :type: str
        """
        self._tns_alias = tns_alias

    @property
    def tns_names(self):
        """
        Gets the tns_names of this UpdateConnectionFromAtp.
        Array of service names that are available for selection in the tnsAlias property.


        :return: The tns_names of this UpdateConnectionFromAtp.
        :rtype: list[str]
        """
        return self._tns_names

    @tns_names.setter
    def tns_names(self, tns_names):
        """
        Sets the tns_names of this UpdateConnectionFromAtp.
        Array of service names that are available for selection in the tnsAlias property.


        :param tns_names: The tns_names of this UpdateConnectionFromAtp.
        :type: list[str]
        """
        self._tns_names = tns_names

    @property
    def username(self):
        """
        Gets the username of this UpdateConnectionFromAtp.
        The user name for the connection.


        :return: The username of this UpdateConnectionFromAtp.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this UpdateConnectionFromAtp.
        The user name for the connection.


        :param username: The username of this UpdateConnectionFromAtp.
        :type: str
        """
        self._username = username

    @property
    def password(self):
        """
        Gets the password of this UpdateConnectionFromAtp.
        The password for the connection.


        :return: The password of this UpdateConnectionFromAtp.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this UpdateConnectionFromAtp.
        The password for the connection.


        :param password: The password of this UpdateConnectionFromAtp.
        :type: str
        """
        self._password = password

    @property
    def password_secret(self):
        """
        Gets the password_secret of this UpdateConnectionFromAtp.

        :return: The password_secret of this UpdateConnectionFromAtp.
        :rtype: oci.data_integration.models.SensitiveAttribute
        """
        return self._password_secret

    @password_secret.setter
    def password_secret(self, password_secret):
        """
        Sets the password_secret of this UpdateConnectionFromAtp.

        :param password_secret: The password_secret of this UpdateConnectionFromAtp.
        :type: oci.data_integration.models.SensitiveAttribute
        """
        self._password_secret = password_secret

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
