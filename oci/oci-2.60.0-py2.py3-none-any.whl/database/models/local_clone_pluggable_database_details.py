# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class LocalClonePluggableDatabaseDetails(object):
    """
    Parameters for cloning a pluggable database (PDB) within the same database (CDB).

    **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new LocalClonePluggableDatabaseDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param cloned_pdb_name:
            The value to assign to the cloned_pdb_name property of this LocalClonePluggableDatabaseDetails.
        :type cloned_pdb_name: str

        :param pdb_admin_password:
            The value to assign to the pdb_admin_password property of this LocalClonePluggableDatabaseDetails.
        :type pdb_admin_password: str

        :param target_tde_wallet_password:
            The value to assign to the target_tde_wallet_password property of this LocalClonePluggableDatabaseDetails.
        :type target_tde_wallet_password: str

        :param should_pdb_admin_account_be_locked:
            The value to assign to the should_pdb_admin_account_be_locked property of this LocalClonePluggableDatabaseDetails.
        :type should_pdb_admin_account_be_locked: bool

        """
        self.swagger_types = {
            'cloned_pdb_name': 'str',
            'pdb_admin_password': 'str',
            'target_tde_wallet_password': 'str',
            'should_pdb_admin_account_be_locked': 'bool'
        }

        self.attribute_map = {
            'cloned_pdb_name': 'clonedPdbName',
            'pdb_admin_password': 'pdbAdminPassword',
            'target_tde_wallet_password': 'targetTdeWalletPassword',
            'should_pdb_admin_account_be_locked': 'shouldPdbAdminAccountBeLocked'
        }

        self._cloned_pdb_name = None
        self._pdb_admin_password = None
        self._target_tde_wallet_password = None
        self._should_pdb_admin_account_be_locked = None

    @property
    def cloned_pdb_name(self):
        """
        **[Required]** Gets the cloned_pdb_name of this LocalClonePluggableDatabaseDetails.
        The name for the pluggable database (PDB). The name is unique in the context of a :class:`Database`. The name must begin with an alphabetic character and can contain a maximum of thirty alphanumeric characters. Special characters are not permitted. The pluggable database name should not be same as the container database name.


        :return: The cloned_pdb_name of this LocalClonePluggableDatabaseDetails.
        :rtype: str
        """
        return self._cloned_pdb_name

    @cloned_pdb_name.setter
    def cloned_pdb_name(self, cloned_pdb_name):
        """
        Sets the cloned_pdb_name of this LocalClonePluggableDatabaseDetails.
        The name for the pluggable database (PDB). The name is unique in the context of a :class:`Database`. The name must begin with an alphabetic character and can contain a maximum of thirty alphanumeric characters. Special characters are not permitted. The pluggable database name should not be same as the container database name.


        :param cloned_pdb_name: The cloned_pdb_name of this LocalClonePluggableDatabaseDetails.
        :type: str
        """
        self._cloned_pdb_name = cloned_pdb_name

    @property
    def pdb_admin_password(self):
        """
        Gets the pdb_admin_password of this LocalClonePluggableDatabaseDetails.
        A strong password for PDB Admin of the newly cloned PDB. The password must be at least nine characters and contain at least two uppercase, two lowercase, two numbers, and two special characters. The special characters must be _, \\#, or -.


        :return: The pdb_admin_password of this LocalClonePluggableDatabaseDetails.
        :rtype: str
        """
        return self._pdb_admin_password

    @pdb_admin_password.setter
    def pdb_admin_password(self, pdb_admin_password):
        """
        Sets the pdb_admin_password of this LocalClonePluggableDatabaseDetails.
        A strong password for PDB Admin of the newly cloned PDB. The password must be at least nine characters and contain at least two uppercase, two lowercase, two numbers, and two special characters. The special characters must be _, \\#, or -.


        :param pdb_admin_password: The pdb_admin_password of this LocalClonePluggableDatabaseDetails.
        :type: str
        """
        self._pdb_admin_password = pdb_admin_password

    @property
    def target_tde_wallet_password(self):
        """
        Gets the target_tde_wallet_password of this LocalClonePluggableDatabaseDetails.
        The existing TDE wallet password of the target CDB.


        :return: The target_tde_wallet_password of this LocalClonePluggableDatabaseDetails.
        :rtype: str
        """
        return self._target_tde_wallet_password

    @target_tde_wallet_password.setter
    def target_tde_wallet_password(self, target_tde_wallet_password):
        """
        Sets the target_tde_wallet_password of this LocalClonePluggableDatabaseDetails.
        The existing TDE wallet password of the target CDB.


        :param target_tde_wallet_password: The target_tde_wallet_password of this LocalClonePluggableDatabaseDetails.
        :type: str
        """
        self._target_tde_wallet_password = target_tde_wallet_password

    @property
    def should_pdb_admin_account_be_locked(self):
        """
        Gets the should_pdb_admin_account_be_locked of this LocalClonePluggableDatabaseDetails.
        The locked mode of the pluggable database admin account. If false, the user needs to provide the PDB Admin Password to connect to it.
        If true, the pluggable database will be locked and user cannot login to it.


        :return: The should_pdb_admin_account_be_locked of this LocalClonePluggableDatabaseDetails.
        :rtype: bool
        """
        return self._should_pdb_admin_account_be_locked

    @should_pdb_admin_account_be_locked.setter
    def should_pdb_admin_account_be_locked(self, should_pdb_admin_account_be_locked):
        """
        Sets the should_pdb_admin_account_be_locked of this LocalClonePluggableDatabaseDetails.
        The locked mode of the pluggable database admin account. If false, the user needs to provide the PDB Admin Password to connect to it.
        If true, the pluggable database will be locked and user cannot login to it.


        :param should_pdb_admin_account_be_locked: The should_pdb_admin_account_be_locked of this LocalClonePluggableDatabaseDetails.
        :type: bool
        """
        self._should_pdb_admin_account_be_locked = should_pdb_admin_account_be_locked

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
