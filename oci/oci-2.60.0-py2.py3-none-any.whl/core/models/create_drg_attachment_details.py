# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateDrgAttachmentDetails(object):
    """
    CreateDrgAttachmentDetails model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateDrgAttachmentDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this CreateDrgAttachmentDetails.
        :type display_name: str

        :param drg_id:
            The value to assign to the drg_id property of this CreateDrgAttachmentDetails.
        :type drg_id: str

        :param drg_route_table_id:
            The value to assign to the drg_route_table_id property of this CreateDrgAttachmentDetails.
        :type drg_route_table_id: str

        :param network_details:
            The value to assign to the network_details property of this CreateDrgAttachmentDetails.
        :type network_details: oci.core.models.DrgAttachmentNetworkCreateDetails

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateDrgAttachmentDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateDrgAttachmentDetails.
        :type freeform_tags: dict(str, str)

        :param route_table_id:
            The value to assign to the route_table_id property of this CreateDrgAttachmentDetails.
        :type route_table_id: str

        :param vcn_id:
            The value to assign to the vcn_id property of this CreateDrgAttachmentDetails.
        :type vcn_id: str

        """
        self.swagger_types = {
            'display_name': 'str',
            'drg_id': 'str',
            'drg_route_table_id': 'str',
            'network_details': 'DrgAttachmentNetworkCreateDetails',
            'defined_tags': 'dict(str, dict(str, object))',
            'freeform_tags': 'dict(str, str)',
            'route_table_id': 'str',
            'vcn_id': 'str'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'drg_id': 'drgId',
            'drg_route_table_id': 'drgRouteTableId',
            'network_details': 'networkDetails',
            'defined_tags': 'definedTags',
            'freeform_tags': 'freeformTags',
            'route_table_id': 'routeTableId',
            'vcn_id': 'vcnId'
        }

        self._display_name = None
        self._drg_id = None
        self._drg_route_table_id = None
        self._network_details = None
        self._defined_tags = None
        self._freeform_tags = None
        self._route_table_id = None
        self._vcn_id = None

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateDrgAttachmentDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this CreateDrgAttachmentDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateDrgAttachmentDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this CreateDrgAttachmentDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def drg_id(self):
        """
        **[Required]** Gets the drg_id of this CreateDrgAttachmentDetails.
        The `OCID`__ of the DRG.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The drg_id of this CreateDrgAttachmentDetails.
        :rtype: str
        """
        return self._drg_id

    @drg_id.setter
    def drg_id(self, drg_id):
        """
        Sets the drg_id of this CreateDrgAttachmentDetails.
        The `OCID`__ of the DRG.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param drg_id: The drg_id of this CreateDrgAttachmentDetails.
        :type: str
        """
        self._drg_id = drg_id

    @property
    def drg_route_table_id(self):
        """
        Gets the drg_route_table_id of this CreateDrgAttachmentDetails.
        The `OCID`__ of the DRG route table that is assigned to this attachment.

        The DRG route table manages traffic inside the DRG.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The drg_route_table_id of this CreateDrgAttachmentDetails.
        :rtype: str
        """
        return self._drg_route_table_id

    @drg_route_table_id.setter
    def drg_route_table_id(self, drg_route_table_id):
        """
        Sets the drg_route_table_id of this CreateDrgAttachmentDetails.
        The `OCID`__ of the DRG route table that is assigned to this attachment.

        The DRG route table manages traffic inside the DRG.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param drg_route_table_id: The drg_route_table_id of this CreateDrgAttachmentDetails.
        :type: str
        """
        self._drg_route_table_id = drg_route_table_id

    @property
    def network_details(self):
        """
        Gets the network_details of this CreateDrgAttachmentDetails.

        :return: The network_details of this CreateDrgAttachmentDetails.
        :rtype: oci.core.models.DrgAttachmentNetworkCreateDetails
        """
        return self._network_details

    @network_details.setter
    def network_details(self, network_details):
        """
        Sets the network_details of this CreateDrgAttachmentDetails.

        :param network_details: The network_details of this CreateDrgAttachmentDetails.
        :type: oci.core.models.DrgAttachmentNetworkCreateDetails
        """
        self._network_details = network_details

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateDrgAttachmentDetails.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateDrgAttachmentDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateDrgAttachmentDetails.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateDrgAttachmentDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateDrgAttachmentDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateDrgAttachmentDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateDrgAttachmentDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateDrgAttachmentDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def route_table_id(self):
        """
        Gets the route_table_id of this CreateDrgAttachmentDetails.
        The `OCID`__ of the route table used by the DRG attachment.

        If you don't specify a route table here, the DRG attachment is created without an associated route
        table. The Networking service does NOT automatically associate the attached VCN's default route table
        with the DRG attachment.
        For information about why you would associate a route table with a DRG attachment, see:

          * `Transit Routing: Access to Multiple VCNs in Same Region`__
          * `Transit Routing: Private Access to Oracle Services`__
        This field is deprecated. Instead, use the networkDetails field to specify the VCN route table for this attachment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm
        __ https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/transitrouting.htm
        __ https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/transitroutingoracleservices.htm


        :return: The route_table_id of this CreateDrgAttachmentDetails.
        :rtype: str
        """
        return self._route_table_id

    @route_table_id.setter
    def route_table_id(self, route_table_id):
        """
        Sets the route_table_id of this CreateDrgAttachmentDetails.
        The `OCID`__ of the route table used by the DRG attachment.

        If you don't specify a route table here, the DRG attachment is created without an associated route
        table. The Networking service does NOT automatically associate the attached VCN's default route table
        with the DRG attachment.
        For information about why you would associate a route table with a DRG attachment, see:

          * `Transit Routing: Access to Multiple VCNs in Same Region`__
          * `Transit Routing: Private Access to Oracle Services`__
        This field is deprecated. Instead, use the networkDetails field to specify the VCN route table for this attachment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm
        __ https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/transitrouting.htm
        __ https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/transitroutingoracleservices.htm


        :param route_table_id: The route_table_id of this CreateDrgAttachmentDetails.
        :type: str
        """
        self._route_table_id = route_table_id

    @property
    def vcn_id(self):
        """
        Gets the vcn_id of this CreateDrgAttachmentDetails.
        The `OCID`__ of the VCN.
        This field is deprecated. Instead, use the `networkDetails` field to specify the `OCID`__ of the attached resource.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm
        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The vcn_id of this CreateDrgAttachmentDetails.
        :rtype: str
        """
        return self._vcn_id

    @vcn_id.setter
    def vcn_id(self, vcn_id):
        """
        Sets the vcn_id of this CreateDrgAttachmentDetails.
        The `OCID`__ of the VCN.
        This field is deprecated. Instead, use the `networkDetails` field to specify the `OCID`__ of the attached resource.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm
        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param vcn_id: The vcn_id of this CreateDrgAttachmentDetails.
        :type: str
        """
        self._vcn_id = vcn_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
