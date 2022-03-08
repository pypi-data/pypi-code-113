# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TopologyAssociatedWithRelationshipDetails(object):
    """
    Defines association details for an `associatedWith` relationship.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new TopologyAssociatedWithRelationshipDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param via:
            The value to assign to the via property of this TopologyAssociatedWithRelationshipDetails.
        :type via: list[str]

        """
        self.swagger_types = {
            'via': 'list[str]'
        }

        self.attribute_map = {
            'via': 'via'
        }

        self._via = None

    @property
    def via(self):
        """
        Gets the via of this TopologyAssociatedWithRelationshipDetails.
        The `OCID`__ of the entities via which the relationship is created. For example an instance is associated with a network security group via the VNIC attachment and the VNIC.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The via of this TopologyAssociatedWithRelationshipDetails.
        :rtype: list[str]
        """
        return self._via

    @via.setter
    def via(self, via):
        """
        Sets the via of this TopologyAssociatedWithRelationshipDetails.
        The `OCID`__ of the entities via which the relationship is created. For example an instance is associated with a network security group via the VNIC attachment and the VNIC.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param via: The via of this TopologyAssociatedWithRelationshipDetails.
        :type: list[str]
        """
        self._via = via

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
