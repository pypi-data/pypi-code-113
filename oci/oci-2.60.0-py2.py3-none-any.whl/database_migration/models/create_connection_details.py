# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateConnectionDetails(object):
    """
    Details to create a Database Connection resource.
    """

    #: A constant which can be used with the database_type property of a CreateConnectionDetails.
    #: This constant has a value of "MANUAL"
    DATABASE_TYPE_MANUAL = "MANUAL"

    #: A constant which can be used with the database_type property of a CreateConnectionDetails.
    #: This constant has a value of "AUTONOMOUS"
    DATABASE_TYPE_AUTONOMOUS = "AUTONOMOUS"

    #: A constant which can be used with the database_type property of a CreateConnectionDetails.
    #: This constant has a value of "USER_MANAGED_OCI"
    DATABASE_TYPE_USER_MANAGED_OCI = "USER_MANAGED_OCI"

    #: A constant which can be used with the manual_database_sub_type property of a CreateConnectionDetails.
    #: This constant has a value of "ORACLE"
    MANUAL_DATABASE_SUB_TYPE_ORACLE = "ORACLE"

    #: A constant which can be used with the manual_database_sub_type property of a CreateConnectionDetails.
    #: This constant has a value of "RDS_ORACLE"
    MANUAL_DATABASE_SUB_TYPE_RDS_ORACLE = "RDS_ORACLE"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateConnectionDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateConnectionDetails.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this CreateConnectionDetails.
        :type display_name: str

        :param database_type:
            The value to assign to the database_type property of this CreateConnectionDetails.
            Allowed values for this property are: "MANUAL", "AUTONOMOUS", "USER_MANAGED_OCI"
        :type database_type: str

        :param manual_database_sub_type:
            The value to assign to the manual_database_sub_type property of this CreateConnectionDetails.
            Allowed values for this property are: "ORACLE", "RDS_ORACLE"
        :type manual_database_sub_type: str

        :param database_id:
            The value to assign to the database_id property of this CreateConnectionDetails.
        :type database_id: str

        :param connect_descriptor:
            The value to assign to the connect_descriptor property of this CreateConnectionDetails.
        :type connect_descriptor: oci.database_migration.models.CreateConnectDescriptor

        :param certificate_tdn:
            The value to assign to the certificate_tdn property of this CreateConnectionDetails.
        :type certificate_tdn: str

        :param tls_wallet:
            The value to assign to the tls_wallet property of this CreateConnectionDetails.
        :type tls_wallet: str

        :param tls_keystore:
            The value to assign to the tls_keystore property of this CreateConnectionDetails.
        :type tls_keystore: str

        :param ssh_details:
            The value to assign to the ssh_details property of this CreateConnectionDetails.
        :type ssh_details: oci.database_migration.models.CreateSshDetails

        :param admin_credentials:
            The value to assign to the admin_credentials property of this CreateConnectionDetails.
        :type admin_credentials: oci.database_migration.models.CreateAdminCredentials

        :param private_endpoint:
            The value to assign to the private_endpoint property of this CreateConnectionDetails.
        :type private_endpoint: oci.database_migration.models.CreatePrivateEndpoint

        :param vault_details:
            The value to assign to the vault_details property of this CreateConnectionDetails.
        :type vault_details: oci.database_migration.models.CreateVaultDetails

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateConnectionDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateConnectionDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'display_name': 'str',
            'database_type': 'str',
            'manual_database_sub_type': 'str',
            'database_id': 'str',
            'connect_descriptor': 'CreateConnectDescriptor',
            'certificate_tdn': 'str',
            'tls_wallet': 'str',
            'tls_keystore': 'str',
            'ssh_details': 'CreateSshDetails',
            'admin_credentials': 'CreateAdminCredentials',
            'private_endpoint': 'CreatePrivateEndpoint',
            'vault_details': 'CreateVaultDetails',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'database_type': 'databaseType',
            'manual_database_sub_type': 'manualDatabaseSubType',
            'database_id': 'databaseId',
            'connect_descriptor': 'connectDescriptor',
            'certificate_tdn': 'certificateTdn',
            'tls_wallet': 'tlsWallet',
            'tls_keystore': 'tlsKeystore',
            'ssh_details': 'sshDetails',
            'admin_credentials': 'adminCredentials',
            'private_endpoint': 'privateEndpoint',
            'vault_details': 'vaultDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._compartment_id = None
        self._display_name = None
        self._database_type = None
        self._manual_database_sub_type = None
        self._database_id = None
        self._connect_descriptor = None
        self._certificate_tdn = None
        self._tls_wallet = None
        self._tls_keystore = None
        self._ssh_details = None
        self._admin_credentials = None
        self._private_endpoint = None
        self._vault_details = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateConnectionDetails.
        OCID of the compartment


        :return: The compartment_id of this CreateConnectionDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateConnectionDetails.
        OCID of the compartment


        :param compartment_id: The compartment_id of this CreateConnectionDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateConnectionDetails.
        Database Connection display name identifier.


        :return: The display_name of this CreateConnectionDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateConnectionDetails.
        Database Connection display name identifier.


        :param display_name: The display_name of this CreateConnectionDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def database_type(self):
        """
        **[Required]** Gets the database_type of this CreateConnectionDetails.
        Database connection type.

        Allowed values for this property are: "MANUAL", "AUTONOMOUS", "USER_MANAGED_OCI"


        :return: The database_type of this CreateConnectionDetails.
        :rtype: str
        """
        return self._database_type

    @database_type.setter
    def database_type(self, database_type):
        """
        Sets the database_type of this CreateConnectionDetails.
        Database connection type.


        :param database_type: The database_type of this CreateConnectionDetails.
        :type: str
        """
        allowed_values = ["MANUAL", "AUTONOMOUS", "USER_MANAGED_OCI"]
        if not value_allowed_none_or_none_sentinel(database_type, allowed_values):
            raise ValueError(
                "Invalid value for `database_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._database_type = database_type

    @property
    def manual_database_sub_type(self):
        """
        Gets the manual_database_sub_type of this CreateConnectionDetails.
        Database manual connection subtype. This value can only be specified for manual connections.

        Allowed values for this property are: "ORACLE", "RDS_ORACLE"


        :return: The manual_database_sub_type of this CreateConnectionDetails.
        :rtype: str
        """
        return self._manual_database_sub_type

    @manual_database_sub_type.setter
    def manual_database_sub_type(self, manual_database_sub_type):
        """
        Sets the manual_database_sub_type of this CreateConnectionDetails.
        Database manual connection subtype. This value can only be specified for manual connections.


        :param manual_database_sub_type: The manual_database_sub_type of this CreateConnectionDetails.
        :type: str
        """
        allowed_values = ["ORACLE", "RDS_ORACLE"]
        if not value_allowed_none_or_none_sentinel(manual_database_sub_type, allowed_values):
            raise ValueError(
                "Invalid value for `manual_database_sub_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._manual_database_sub_type = manual_database_sub_type

    @property
    def database_id(self):
        """
        Gets the database_id of this CreateConnectionDetails.
        The OCID of the cloud database. Required if the database connection type is Autonomous.


        :return: The database_id of this CreateConnectionDetails.
        :rtype: str
        """
        return self._database_id

    @database_id.setter
    def database_id(self, database_id):
        """
        Sets the database_id of this CreateConnectionDetails.
        The OCID of the cloud database. Required if the database connection type is Autonomous.


        :param database_id: The database_id of this CreateConnectionDetails.
        :type: str
        """
        self._database_id = database_id

    @property
    def connect_descriptor(self):
        """
        Gets the connect_descriptor of this CreateConnectionDetails.

        :return: The connect_descriptor of this CreateConnectionDetails.
        :rtype: oci.database_migration.models.CreateConnectDescriptor
        """
        return self._connect_descriptor

    @connect_descriptor.setter
    def connect_descriptor(self, connect_descriptor):
        """
        Sets the connect_descriptor of this CreateConnectionDetails.

        :param connect_descriptor: The connect_descriptor of this CreateConnectionDetails.
        :type: oci.database_migration.models.CreateConnectDescriptor
        """
        self._connect_descriptor = connect_descriptor

    @property
    def certificate_tdn(self):
        """
        Gets the certificate_tdn of this CreateConnectionDetails.
        This name is the distinguished name used while creating the certificate on target database. Requires a TLS wallet to be specified.
        Not required for source container database connections.


        :return: The certificate_tdn of this CreateConnectionDetails.
        :rtype: str
        """
        return self._certificate_tdn

    @certificate_tdn.setter
    def certificate_tdn(self, certificate_tdn):
        """
        Sets the certificate_tdn of this CreateConnectionDetails.
        This name is the distinguished name used while creating the certificate on target database. Requires a TLS wallet to be specified.
        Not required for source container database connections.


        :param certificate_tdn: The certificate_tdn of this CreateConnectionDetails.
        :type: str
        """
        self._certificate_tdn = certificate_tdn

    @property
    def tls_wallet(self):
        """
        Gets the tls_wallet of this CreateConnectionDetails.
        cwallet.sso containing containing the TCPS/SSL certificate; base64 encoded String. Not required for source container database connections.


        :return: The tls_wallet of this CreateConnectionDetails.
        :rtype: str
        """
        return self._tls_wallet

    @tls_wallet.setter
    def tls_wallet(self, tls_wallet):
        """
        Sets the tls_wallet of this CreateConnectionDetails.
        cwallet.sso containing containing the TCPS/SSL certificate; base64 encoded String. Not required for source container database connections.


        :param tls_wallet: The tls_wallet of this CreateConnectionDetails.
        :type: str
        """
        self._tls_wallet = tls_wallet

    @property
    def tls_keystore(self):
        """
        Gets the tls_keystore of this CreateConnectionDetails.
        keystore.jks file contents; base64 encoded String. Requires a TLS wallet to be specified. Not required for source container database connections.


        :return: The tls_keystore of this CreateConnectionDetails.
        :rtype: str
        """
        return self._tls_keystore

    @tls_keystore.setter
    def tls_keystore(self, tls_keystore):
        """
        Sets the tls_keystore of this CreateConnectionDetails.
        keystore.jks file contents; base64 encoded String. Requires a TLS wallet to be specified. Not required for source container database connections.


        :param tls_keystore: The tls_keystore of this CreateConnectionDetails.
        :type: str
        """
        self._tls_keystore = tls_keystore

    @property
    def ssh_details(self):
        """
        Gets the ssh_details of this CreateConnectionDetails.

        :return: The ssh_details of this CreateConnectionDetails.
        :rtype: oci.database_migration.models.CreateSshDetails
        """
        return self._ssh_details

    @ssh_details.setter
    def ssh_details(self, ssh_details):
        """
        Sets the ssh_details of this CreateConnectionDetails.

        :param ssh_details: The ssh_details of this CreateConnectionDetails.
        :type: oci.database_migration.models.CreateSshDetails
        """
        self._ssh_details = ssh_details

    @property
    def admin_credentials(self):
        """
        **[Required]** Gets the admin_credentials of this CreateConnectionDetails.

        :return: The admin_credentials of this CreateConnectionDetails.
        :rtype: oci.database_migration.models.CreateAdminCredentials
        """
        return self._admin_credentials

    @admin_credentials.setter
    def admin_credentials(self, admin_credentials):
        """
        Sets the admin_credentials of this CreateConnectionDetails.

        :param admin_credentials: The admin_credentials of this CreateConnectionDetails.
        :type: oci.database_migration.models.CreateAdminCredentials
        """
        self._admin_credentials = admin_credentials

    @property
    def private_endpoint(self):
        """
        Gets the private_endpoint of this CreateConnectionDetails.

        :return: The private_endpoint of this CreateConnectionDetails.
        :rtype: oci.database_migration.models.CreatePrivateEndpoint
        """
        return self._private_endpoint

    @private_endpoint.setter
    def private_endpoint(self, private_endpoint):
        """
        Sets the private_endpoint of this CreateConnectionDetails.

        :param private_endpoint: The private_endpoint of this CreateConnectionDetails.
        :type: oci.database_migration.models.CreatePrivateEndpoint
        """
        self._private_endpoint = private_endpoint

    @property
    def vault_details(self):
        """
        **[Required]** Gets the vault_details of this CreateConnectionDetails.

        :return: The vault_details of this CreateConnectionDetails.
        :rtype: oci.database_migration.models.CreateVaultDetails
        """
        return self._vault_details

    @vault_details.setter
    def vault_details(self, vault_details):
        """
        Sets the vault_details of this CreateConnectionDetails.

        :param vault_details: The vault_details of this CreateConnectionDetails.
        :type: oci.database_migration.models.CreateVaultDetails
        """
        self._vault_details = vault_details

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateConnectionDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this CreateConnectionDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateConnectionDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this CreateConnectionDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateConnectionDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this CreateConnectionDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateConnectionDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this CreateConnectionDetails.
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
