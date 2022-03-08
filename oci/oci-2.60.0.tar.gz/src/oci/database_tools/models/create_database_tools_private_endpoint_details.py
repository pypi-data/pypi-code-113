# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateDatabaseToolsPrivateEndpointDetails(object):
    """
    The information about new DatabaseToolsPrivateEndpoint.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateDatabaseToolsPrivateEndpointDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateDatabaseToolsPrivateEndpointDetails.
        :type compartment_id: str

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateDatabaseToolsPrivateEndpointDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateDatabaseToolsPrivateEndpointDetails.
        :type freeform_tags: dict(str, str)

        :param display_name:
            The value to assign to the display_name property of this CreateDatabaseToolsPrivateEndpointDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this CreateDatabaseToolsPrivateEndpointDetails.
        :type description: str

        :param endpoint_service_id:
            The value to assign to the endpoint_service_id property of this CreateDatabaseToolsPrivateEndpointDetails.
        :type endpoint_service_id: str

        :param subnet_id:
            The value to assign to the subnet_id property of this CreateDatabaseToolsPrivateEndpointDetails.
        :type subnet_id: str

        :param private_endpoint_ip:
            The value to assign to the private_endpoint_ip property of this CreateDatabaseToolsPrivateEndpointDetails.
        :type private_endpoint_ip: str

        :param nsg_ids:
            The value to assign to the nsg_ids property of this CreateDatabaseToolsPrivateEndpointDetails.
        :type nsg_ids: list[str]

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'defined_tags': 'dict(str, dict(str, object))',
            'freeform_tags': 'dict(str, str)',
            'display_name': 'str',
            'description': 'str',
            'endpoint_service_id': 'str',
            'subnet_id': 'str',
            'private_endpoint_ip': 'str',
            'nsg_ids': 'list[str]'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'defined_tags': 'definedTags',
            'freeform_tags': 'freeformTags',
            'display_name': 'displayName',
            'description': 'description',
            'endpoint_service_id': 'endpointServiceId',
            'subnet_id': 'subnetId',
            'private_endpoint_ip': 'privateEndpointIp',
            'nsg_ids': 'nsgIds'
        }

        self._compartment_id = None
        self._defined_tags = None
        self._freeform_tags = None
        self._display_name = None
        self._description = None
        self._endpoint_service_id = None
        self._subnet_id = None
        self._private_endpoint_ip = None
        self._nsg_ids = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateDatabaseToolsPrivateEndpointDetails.
        The `OCID`__ of the containing Compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this CreateDatabaseToolsPrivateEndpointDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateDatabaseToolsPrivateEndpointDetails.
        The `OCID`__ of the containing Compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this CreateDatabaseToolsPrivateEndpointDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateDatabaseToolsPrivateEndpointDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this CreateDatabaseToolsPrivateEndpointDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateDatabaseToolsPrivateEndpointDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this CreateDatabaseToolsPrivateEndpointDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateDatabaseToolsPrivateEndpointDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this CreateDatabaseToolsPrivateEndpointDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateDatabaseToolsPrivateEndpointDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this CreateDatabaseToolsPrivateEndpointDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this CreateDatabaseToolsPrivateEndpointDetails.
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.


        :return: The display_name of this CreateDatabaseToolsPrivateEndpointDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateDatabaseToolsPrivateEndpointDetails.
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.


        :param display_name: The display_name of this CreateDatabaseToolsPrivateEndpointDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this CreateDatabaseToolsPrivateEndpointDetails.
        A description of the DatabaseToolsPrivateEndpoint.


        :return: The description of this CreateDatabaseToolsPrivateEndpointDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateDatabaseToolsPrivateEndpointDetails.
        A description of the DatabaseToolsPrivateEndpoint.


        :param description: The description of this CreateDatabaseToolsPrivateEndpointDetails.
        :type: str
        """
        self._description = description

    @property
    def endpoint_service_id(self):
        """
        **[Required]** Gets the endpoint_service_id of this CreateDatabaseToolsPrivateEndpointDetails.
        The `OCID`__ of the DatabaseToolsEndpointService.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The endpoint_service_id of this CreateDatabaseToolsPrivateEndpointDetails.
        :rtype: str
        """
        return self._endpoint_service_id

    @endpoint_service_id.setter
    def endpoint_service_id(self, endpoint_service_id):
        """
        Sets the endpoint_service_id of this CreateDatabaseToolsPrivateEndpointDetails.
        The `OCID`__ of the DatabaseToolsEndpointService.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param endpoint_service_id: The endpoint_service_id of this CreateDatabaseToolsPrivateEndpointDetails.
        :type: str
        """
        self._endpoint_service_id = endpoint_service_id

    @property
    def subnet_id(self):
        """
        **[Required]** Gets the subnet_id of this CreateDatabaseToolsPrivateEndpointDetails.
        The `OCID`__ of the subnet that the private endpoint belongs to.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The subnet_id of this CreateDatabaseToolsPrivateEndpointDetails.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """
        Sets the subnet_id of this CreateDatabaseToolsPrivateEndpointDetails.
        The `OCID`__ of the subnet that the private endpoint belongs to.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param subnet_id: The subnet_id of this CreateDatabaseToolsPrivateEndpointDetails.
        :type: str
        """
        self._subnet_id = subnet_id

    @property
    def private_endpoint_ip(self):
        """
        Gets the private_endpoint_ip of this CreateDatabaseToolsPrivateEndpointDetails.
        The private IP address that represents the access point for the associated endpoint service.


        :return: The private_endpoint_ip of this CreateDatabaseToolsPrivateEndpointDetails.
        :rtype: str
        """
        return self._private_endpoint_ip

    @private_endpoint_ip.setter
    def private_endpoint_ip(self, private_endpoint_ip):
        """
        Sets the private_endpoint_ip of this CreateDatabaseToolsPrivateEndpointDetails.
        The private IP address that represents the access point for the associated endpoint service.


        :param private_endpoint_ip: The private_endpoint_ip of this CreateDatabaseToolsPrivateEndpointDetails.
        :type: str
        """
        self._private_endpoint_ip = private_endpoint_ip

    @property
    def nsg_ids(self):
        """
        Gets the nsg_ids of this CreateDatabaseToolsPrivateEndpointDetails.
        The `OCID`__ of the network security groups
        that the private endpoint's VNIC belongs to.  For more information about NSGs, see
        :class:`NetworkSecurityGroup`.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The nsg_ids of this CreateDatabaseToolsPrivateEndpointDetails.
        :rtype: list[str]
        """
        return self._nsg_ids

    @nsg_ids.setter
    def nsg_ids(self, nsg_ids):
        """
        Sets the nsg_ids of this CreateDatabaseToolsPrivateEndpointDetails.
        The `OCID`__ of the network security groups
        that the private endpoint's VNIC belongs to.  For more information about NSGs, see
        :class:`NetworkSecurityGroup`.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param nsg_ids: The nsg_ids of this CreateDatabaseToolsPrivateEndpointDetails.
        :type: list[str]
        """
        self._nsg_ids = nsg_ids

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
