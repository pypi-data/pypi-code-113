# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateNetworkSourceDetails(object):
    """
    UpdateNetworkSourceDetails model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateNetworkSourceDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param description:
            The value to assign to the description property of this UpdateNetworkSourceDetails.
        :type description: str

        :param public_source_list:
            The value to assign to the public_source_list property of this UpdateNetworkSourceDetails.
        :type public_source_list: list[str]

        :param virtual_source_list:
            The value to assign to the virtual_source_list property of this UpdateNetworkSourceDetails.
        :type virtual_source_list: list[oci.identity.models.NetworkSourcesVirtualSourceList]

        :param services:
            The value to assign to the services property of this UpdateNetworkSourceDetails.
        :type services: list[str]

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateNetworkSourceDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateNetworkSourceDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'description': 'str',
            'public_source_list': 'list[str]',
            'virtual_source_list': 'list[NetworkSourcesVirtualSourceList]',
            'services': 'list[str]',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'description': 'description',
            'public_source_list': 'publicSourceList',
            'virtual_source_list': 'virtualSourceList',
            'services': 'services',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._description = None
        self._public_source_list = None
        self._virtual_source_list = None
        self._services = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def description(self):
        """
        Gets the description of this UpdateNetworkSourceDetails.
        The description you assign to the network source. Does not have to be unique, and it's changeable.


        :return: The description of this UpdateNetworkSourceDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this UpdateNetworkSourceDetails.
        The description you assign to the network source. Does not have to be unique, and it's changeable.


        :param description: The description of this UpdateNetworkSourceDetails.
        :type: str
        """
        self._description = description

    @property
    def public_source_list(self):
        """
        Gets the public_source_list of this UpdateNetworkSourceDetails.
        A list of allowed public IP addresses and CIDR ranges.


        :return: The public_source_list of this UpdateNetworkSourceDetails.
        :rtype: list[str]
        """
        return self._public_source_list

    @public_source_list.setter
    def public_source_list(self, public_source_list):
        """
        Sets the public_source_list of this UpdateNetworkSourceDetails.
        A list of allowed public IP addresses and CIDR ranges.


        :param public_source_list: The public_source_list of this UpdateNetworkSourceDetails.
        :type: list[str]
        """
        self._public_source_list = public_source_list

    @property
    def virtual_source_list(self):
        """
        Gets the virtual_source_list of this UpdateNetworkSourceDetails.
        A list of allowed VCN OCID and IP range pairs.
        Example:`\"vcnId\": \"ocid1.vcn.oc1.iad.aaaaaaaaexampleuniqueID\", \"ipRanges\": [ \"129.213.39.0/24\" ]`


        :return: The virtual_source_list of this UpdateNetworkSourceDetails.
        :rtype: list[oci.identity.models.NetworkSourcesVirtualSourceList]
        """
        return self._virtual_source_list

    @virtual_source_list.setter
    def virtual_source_list(self, virtual_source_list):
        """
        Sets the virtual_source_list of this UpdateNetworkSourceDetails.
        A list of allowed VCN OCID and IP range pairs.
        Example:`\"vcnId\": \"ocid1.vcn.oc1.iad.aaaaaaaaexampleuniqueID\", \"ipRanges\": [ \"129.213.39.0/24\" ]`


        :param virtual_source_list: The virtual_source_list of this UpdateNetworkSourceDetails.
        :type: list[oci.identity.models.NetworkSourcesVirtualSourceList]
        """
        self._virtual_source_list = virtual_source_list

    @property
    def services(self):
        """
        Gets the services of this UpdateNetworkSourceDetails.
        A list of services allowed to make on-behalf-of requests. These requests can have different source IPs than
        those specified in the network source. Currently, only `all` and `none` are supported. The default is `all`.


        :return: The services of this UpdateNetworkSourceDetails.
        :rtype: list[str]
        """
        return self._services

    @services.setter
    def services(self, services):
        """
        Sets the services of this UpdateNetworkSourceDetails.
        A list of services allowed to make on-behalf-of requests. These requests can have different source IPs than
        those specified in the network source. Currently, only `all` and `none` are supported. The default is `all`.


        :param services: The services of this UpdateNetworkSourceDetails.
        :type: list[str]
        """
        self._services = services

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateNetworkSourceDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this UpdateNetworkSourceDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateNetworkSourceDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this UpdateNetworkSourceDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateNetworkSourceDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this UpdateNetworkSourceDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateNetworkSourceDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this UpdateNetworkSourceDetails.
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
