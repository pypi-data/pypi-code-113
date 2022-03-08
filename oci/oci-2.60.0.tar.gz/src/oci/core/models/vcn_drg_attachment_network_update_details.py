# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .drg_attachment_network_update_details import DrgAttachmentNetworkUpdateDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class VcnDrgAttachmentNetworkUpdateDetails(DrgAttachmentNetworkUpdateDetails):
    """
    Specifies the update details for the VCN attachment.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new VcnDrgAttachmentNetworkUpdateDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.core.models.VcnDrgAttachmentNetworkUpdateDetails.type` attribute
        of this class is ``VCN`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this VcnDrgAttachmentNetworkUpdateDetails.
            Allowed values for this property are: "VCN"
        :type type: str

        :param route_table_id:
            The value to assign to the route_table_id property of this VcnDrgAttachmentNetworkUpdateDetails.
        :type route_table_id: str

        :param vcn_route_type:
            The value to assign to the vcn_route_type property of this VcnDrgAttachmentNetworkUpdateDetails.
        :type vcn_route_type: str

        """
        self.swagger_types = {
            'type': 'str',
            'route_table_id': 'str',
            'vcn_route_type': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'route_table_id': 'routeTableId',
            'vcn_route_type': 'vcnRouteType'
        }

        self._type = None
        self._route_table_id = None
        self._vcn_route_type = None
        self._type = 'VCN'

    @property
    def route_table_id(self):
        """
        Gets the route_table_id of this VcnDrgAttachmentNetworkUpdateDetails.
        This is the `OCID`__ of the route table that is used to route the traffic as it enters a VCN through this attachment.

        For information about why you would associate a route table with a DRG attachment, see:

          * `Transit Routing: Access to Multiple VCNs in Same Region`__
          * `Transit Routing: Private Access to Oracle Services`__

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm
        __ https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/transitrouting.htm
        __ https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/transitroutingoracleservices.htm


        :return: The route_table_id of this VcnDrgAttachmentNetworkUpdateDetails.
        :rtype: str
        """
        return self._route_table_id

    @route_table_id.setter
    def route_table_id(self, route_table_id):
        """
        Sets the route_table_id of this VcnDrgAttachmentNetworkUpdateDetails.
        This is the `OCID`__ of the route table that is used to route the traffic as it enters a VCN through this attachment.

        For information about why you would associate a route table with a DRG attachment, see:

          * `Transit Routing: Access to Multiple VCNs in Same Region`__
          * `Transit Routing: Private Access to Oracle Services`__

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm
        __ https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/transitrouting.htm
        __ https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/transitroutingoracleservices.htm


        :param route_table_id: The route_table_id of this VcnDrgAttachmentNetworkUpdateDetails.
        :type: str
        """
        self._route_table_id = route_table_id

    @property
    def vcn_route_type(self):
        """
        Gets the vcn_route_type of this VcnDrgAttachmentNetworkUpdateDetails.
        Indicates whether the VCN CIDR(s) or the individual Subnet CIDR(s) are imported from the attachment.
        Routes from the VCN Ingress Route Table are always imported.


        :return: The vcn_route_type of this VcnDrgAttachmentNetworkUpdateDetails.
        :rtype: str
        """
        return self._vcn_route_type

    @vcn_route_type.setter
    def vcn_route_type(self, vcn_route_type):
        """
        Sets the vcn_route_type of this VcnDrgAttachmentNetworkUpdateDetails.
        Indicates whether the VCN CIDR(s) or the individual Subnet CIDR(s) are imported from the attachment.
        Routes from the VCN Ingress Route Table are always imported.


        :param vcn_route_type: The vcn_route_type of this VcnDrgAttachmentNetworkUpdateDetails.
        :type: str
        """
        self._vcn_route_type = vcn_route_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
