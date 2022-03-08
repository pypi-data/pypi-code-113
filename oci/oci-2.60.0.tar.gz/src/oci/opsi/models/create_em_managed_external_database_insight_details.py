# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .create_database_insight_details import CreateDatabaseInsightDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateEmManagedExternalDatabaseInsightDetails(CreateDatabaseInsightDetails):
    """
    The information about database to be analyzed.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateEmManagedExternalDatabaseInsightDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.opsi.models.CreateEmManagedExternalDatabaseInsightDetails.entity_source` attribute
        of this class is ``EM_MANAGED_EXTERNAL_DATABASE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param entity_source:
            The value to assign to the entity_source property of this CreateEmManagedExternalDatabaseInsightDetails.
            Allowed values for this property are: "EM_MANAGED_EXTERNAL_DATABASE"
        :type entity_source: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateEmManagedExternalDatabaseInsightDetails.
        :type compartment_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateEmManagedExternalDatabaseInsightDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateEmManagedExternalDatabaseInsightDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param enterprise_manager_identifier:
            The value to assign to the enterprise_manager_identifier property of this CreateEmManagedExternalDatabaseInsightDetails.
        :type enterprise_manager_identifier: str

        :param enterprise_manager_bridge_id:
            The value to assign to the enterprise_manager_bridge_id property of this CreateEmManagedExternalDatabaseInsightDetails.
        :type enterprise_manager_bridge_id: str

        :param enterprise_manager_entity_identifier:
            The value to assign to the enterprise_manager_entity_identifier property of this CreateEmManagedExternalDatabaseInsightDetails.
        :type enterprise_manager_entity_identifier: str

        :param exadata_insight_id:
            The value to assign to the exadata_insight_id property of this CreateEmManagedExternalDatabaseInsightDetails.
        :type exadata_insight_id: str

        """
        self.swagger_types = {
            'entity_source': 'str',
            'compartment_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'enterprise_manager_identifier': 'str',
            'enterprise_manager_bridge_id': 'str',
            'enterprise_manager_entity_identifier': 'str',
            'exadata_insight_id': 'str'
        }

        self.attribute_map = {
            'entity_source': 'entitySource',
            'compartment_id': 'compartmentId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'enterprise_manager_identifier': 'enterpriseManagerIdentifier',
            'enterprise_manager_bridge_id': 'enterpriseManagerBridgeId',
            'enterprise_manager_entity_identifier': 'enterpriseManagerEntityIdentifier',
            'exadata_insight_id': 'exadataInsightId'
        }

        self._entity_source = None
        self._compartment_id = None
        self._freeform_tags = None
        self._defined_tags = None
        self._enterprise_manager_identifier = None
        self._enterprise_manager_bridge_id = None
        self._enterprise_manager_entity_identifier = None
        self._exadata_insight_id = None
        self._entity_source = 'EM_MANAGED_EXTERNAL_DATABASE'

    @property
    def enterprise_manager_identifier(self):
        """
        **[Required]** Gets the enterprise_manager_identifier of this CreateEmManagedExternalDatabaseInsightDetails.
        Enterprise Manager Unique Identifier


        :return: The enterprise_manager_identifier of this CreateEmManagedExternalDatabaseInsightDetails.
        :rtype: str
        """
        return self._enterprise_manager_identifier

    @enterprise_manager_identifier.setter
    def enterprise_manager_identifier(self, enterprise_manager_identifier):
        """
        Sets the enterprise_manager_identifier of this CreateEmManagedExternalDatabaseInsightDetails.
        Enterprise Manager Unique Identifier


        :param enterprise_manager_identifier: The enterprise_manager_identifier of this CreateEmManagedExternalDatabaseInsightDetails.
        :type: str
        """
        self._enterprise_manager_identifier = enterprise_manager_identifier

    @property
    def enterprise_manager_bridge_id(self):
        """
        **[Required]** Gets the enterprise_manager_bridge_id of this CreateEmManagedExternalDatabaseInsightDetails.
        OPSI Enterprise Manager Bridge OCID


        :return: The enterprise_manager_bridge_id of this CreateEmManagedExternalDatabaseInsightDetails.
        :rtype: str
        """
        return self._enterprise_manager_bridge_id

    @enterprise_manager_bridge_id.setter
    def enterprise_manager_bridge_id(self, enterprise_manager_bridge_id):
        """
        Sets the enterprise_manager_bridge_id of this CreateEmManagedExternalDatabaseInsightDetails.
        OPSI Enterprise Manager Bridge OCID


        :param enterprise_manager_bridge_id: The enterprise_manager_bridge_id of this CreateEmManagedExternalDatabaseInsightDetails.
        :type: str
        """
        self._enterprise_manager_bridge_id = enterprise_manager_bridge_id

    @property
    def enterprise_manager_entity_identifier(self):
        """
        **[Required]** Gets the enterprise_manager_entity_identifier of this CreateEmManagedExternalDatabaseInsightDetails.
        Enterprise Manager Entity Unique Identifier


        :return: The enterprise_manager_entity_identifier of this CreateEmManagedExternalDatabaseInsightDetails.
        :rtype: str
        """
        return self._enterprise_manager_entity_identifier

    @enterprise_manager_entity_identifier.setter
    def enterprise_manager_entity_identifier(self, enterprise_manager_entity_identifier):
        """
        Sets the enterprise_manager_entity_identifier of this CreateEmManagedExternalDatabaseInsightDetails.
        Enterprise Manager Entity Unique Identifier


        :param enterprise_manager_entity_identifier: The enterprise_manager_entity_identifier of this CreateEmManagedExternalDatabaseInsightDetails.
        :type: str
        """
        self._enterprise_manager_entity_identifier = enterprise_manager_entity_identifier

    @property
    def exadata_insight_id(self):
        """
        Gets the exadata_insight_id of this CreateEmManagedExternalDatabaseInsightDetails.
        The `OCID`__ of the Exadata insight.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The exadata_insight_id of this CreateEmManagedExternalDatabaseInsightDetails.
        :rtype: str
        """
        return self._exadata_insight_id

    @exadata_insight_id.setter
    def exadata_insight_id(self, exadata_insight_id):
        """
        Sets the exadata_insight_id of this CreateEmManagedExternalDatabaseInsightDetails.
        The `OCID`__ of the Exadata insight.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param exadata_insight_id: The exadata_insight_id of this CreateEmManagedExternalDatabaseInsightDetails.
        :type: str
        """
        self._exadata_insight_id = exadata_insight_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
