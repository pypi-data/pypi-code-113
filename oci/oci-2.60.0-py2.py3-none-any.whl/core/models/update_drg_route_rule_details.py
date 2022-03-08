# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateDrgRouteRuleDetails(object):
    """
    Details used to update a route rule in the DRG route table.
    """

    #: A constant which can be used with the destination_type property of a UpdateDrgRouteRuleDetails.
    #: This constant has a value of "CIDR_BLOCK"
    DESTINATION_TYPE_CIDR_BLOCK = "CIDR_BLOCK"

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateDrgRouteRuleDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this UpdateDrgRouteRuleDetails.
        :type id: str

        :param destination:
            The value to assign to the destination property of this UpdateDrgRouteRuleDetails.
        :type destination: str

        :param destination_type:
            The value to assign to the destination_type property of this UpdateDrgRouteRuleDetails.
            Allowed values for this property are: "CIDR_BLOCK"
        :type destination_type: str

        :param next_hop_drg_attachment_id:
            The value to assign to the next_hop_drg_attachment_id property of this UpdateDrgRouteRuleDetails.
        :type next_hop_drg_attachment_id: str

        """
        self.swagger_types = {
            'id': 'str',
            'destination': 'str',
            'destination_type': 'str',
            'next_hop_drg_attachment_id': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'destination': 'destination',
            'destination_type': 'destinationType',
            'next_hop_drg_attachment_id': 'nextHopDrgAttachmentId'
        }

        self._id = None
        self._destination = None
        self._destination_type = None
        self._next_hop_drg_attachment_id = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this UpdateDrgRouteRuleDetails.
        The Oracle-assigned ID of each DRG route rule to update.


        :return: The id of this UpdateDrgRouteRuleDetails.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this UpdateDrgRouteRuleDetails.
        The Oracle-assigned ID of each DRG route rule to update.


        :param id: The id of this UpdateDrgRouteRuleDetails.
        :type: str
        """
        self._id = id

    @property
    def destination(self):
        """
        Gets the destination of this UpdateDrgRouteRuleDetails.
        The range of IP addresses used for matching when routing traffic.

        Potential values:
          * IP address range in CIDR notation. Can be an IPv4 or IPv6 CIDR. For example: `192.168.1.0/24`
          or `2001:0db8:0123:45::/56`.


        :return: The destination of this UpdateDrgRouteRuleDetails.
        :rtype: str
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        """
        Sets the destination of this UpdateDrgRouteRuleDetails.
        The range of IP addresses used for matching when routing traffic.

        Potential values:
          * IP address range in CIDR notation. Can be an IPv4 or IPv6 CIDR. For example: `192.168.1.0/24`
          or `2001:0db8:0123:45::/56`.


        :param destination: The destination of this UpdateDrgRouteRuleDetails.
        :type: str
        """
        self._destination = destination

    @property
    def destination_type(self):
        """
        Gets the destination_type of this UpdateDrgRouteRuleDetails.
        Type of destination for the rule. Required if `direction` = `EGRESS`.
        Allowed values:
          * `CIDR_BLOCK`: If the rule's `destination` is an IP address range in CIDR notation.

        Allowed values for this property are: "CIDR_BLOCK"


        :return: The destination_type of this UpdateDrgRouteRuleDetails.
        :rtype: str
        """
        return self._destination_type

    @destination_type.setter
    def destination_type(self, destination_type):
        """
        Sets the destination_type of this UpdateDrgRouteRuleDetails.
        Type of destination for the rule. Required if `direction` = `EGRESS`.
        Allowed values:
          * `CIDR_BLOCK`: If the rule's `destination` is an IP address range in CIDR notation.


        :param destination_type: The destination_type of this UpdateDrgRouteRuleDetails.
        :type: str
        """
        allowed_values = ["CIDR_BLOCK"]
        if not value_allowed_none_or_none_sentinel(destination_type, allowed_values):
            raise ValueError(
                "Invalid value for `destination_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._destination_type = destination_type

    @property
    def next_hop_drg_attachment_id(self):
        """
        Gets the next_hop_drg_attachment_id of this UpdateDrgRouteRuleDetails.
        The `OCID`__ of the next hop DRG attachment. The next hop DRG attachment is responsible
        for reaching the network destination.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The next_hop_drg_attachment_id of this UpdateDrgRouteRuleDetails.
        :rtype: str
        """
        return self._next_hop_drg_attachment_id

    @next_hop_drg_attachment_id.setter
    def next_hop_drg_attachment_id(self, next_hop_drg_attachment_id):
        """
        Sets the next_hop_drg_attachment_id of this UpdateDrgRouteRuleDetails.
        The `OCID`__ of the next hop DRG attachment. The next hop DRG attachment is responsible
        for reaching the network destination.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param next_hop_drg_attachment_id: The next_hop_drg_attachment_id of this UpdateDrgRouteRuleDetails.
        :type: str
        """
        self._next_hop_drg_attachment_id = next_hop_drg_attachment_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
