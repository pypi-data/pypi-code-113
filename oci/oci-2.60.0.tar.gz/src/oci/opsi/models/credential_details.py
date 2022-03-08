# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CredentialDetails(object):
    """
    User credential details to connect to the database. This is supplied via the External Database Service.
    """

    #: A constant which can be used with the credential_type property of a CredentialDetails.
    #: This constant has a value of "CREDENTIALS_BY_SOURCE"
    CREDENTIAL_TYPE_CREDENTIALS_BY_SOURCE = "CREDENTIALS_BY_SOURCE"

    def __init__(self, **kwargs):
        """
        Initializes a new CredentialDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.opsi.models.CredentialsBySource`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param credential_source_name:
            The value to assign to the credential_source_name property of this CredentialDetails.
        :type credential_source_name: str

        :param credential_type:
            The value to assign to the credential_type property of this CredentialDetails.
            Allowed values for this property are: "CREDENTIALS_BY_SOURCE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type credential_type: str

        """
        self.swagger_types = {
            'credential_source_name': 'str',
            'credential_type': 'str'
        }

        self.attribute_map = {
            'credential_source_name': 'credentialSourceName',
            'credential_type': 'credentialType'
        }

        self._credential_source_name = None
        self._credential_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['credentialType']

        if type == 'CREDENTIALS_BY_SOURCE':
            return 'CredentialsBySource'
        else:
            return 'CredentialDetails'

    @property
    def credential_source_name(self):
        """
        **[Required]** Gets the credential_source_name of this CredentialDetails.
        Credential source name that had been added in Management Agent wallet. This is supplied in the External Database Service.


        :return: The credential_source_name of this CredentialDetails.
        :rtype: str
        """
        return self._credential_source_name

    @credential_source_name.setter
    def credential_source_name(self, credential_source_name):
        """
        Sets the credential_source_name of this CredentialDetails.
        Credential source name that had been added in Management Agent wallet. This is supplied in the External Database Service.


        :param credential_source_name: The credential_source_name of this CredentialDetails.
        :type: str
        """
        self._credential_source_name = credential_source_name

    @property
    def credential_type(self):
        """
        **[Required]** Gets the credential_type of this CredentialDetails.
        Credential type.

        Allowed values for this property are: "CREDENTIALS_BY_SOURCE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The credential_type of this CredentialDetails.
        :rtype: str
        """
        return self._credential_type

    @credential_type.setter
    def credential_type(self, credential_type):
        """
        Sets the credential_type of this CredentialDetails.
        Credential type.


        :param credential_type: The credential_type of this CredentialDetails.
        :type: str
        """
        allowed_values = ["CREDENTIALS_BY_SOURCE"]
        if not value_allowed_none_or_none_sentinel(credential_type, allowed_values):
            credential_type = 'UNKNOWN_ENUM_VALUE'
        self._credential_type = credential_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
