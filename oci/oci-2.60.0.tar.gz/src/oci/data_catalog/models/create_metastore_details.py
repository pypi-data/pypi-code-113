# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateMetastoreDetails(object):
    """
    Information about a new metastore.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateMetastoreDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this CreateMetastoreDetails.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateMetastoreDetails.
        :type compartment_id: str

        :param default_managed_table_location:
            The value to assign to the default_managed_table_location property of this CreateMetastoreDetails.
        :type default_managed_table_location: str

        :param default_external_table_location:
            The value to assign to the default_external_table_location property of this CreateMetastoreDetails.
        :type default_external_table_location: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateMetastoreDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateMetastoreDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'compartment_id': 'str',
            'default_managed_table_location': 'str',
            'default_external_table_location': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'default_managed_table_location': 'defaultManagedTableLocation',
            'default_external_table_location': 'defaultExternalTableLocation',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._display_name = None
        self._compartment_id = None
        self._default_managed_table_location = None
        self._default_external_table_location = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateMetastoreDetails.
        Mutable name of the metastore.


        :return: The display_name of this CreateMetastoreDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateMetastoreDetails.
        Mutable name of the metastore.


        :param display_name: The display_name of this CreateMetastoreDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateMetastoreDetails.
        OCID of the compartment which holds the metastore.


        :return: The compartment_id of this CreateMetastoreDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateMetastoreDetails.
        OCID of the compartment which holds the metastore.


        :param compartment_id: The compartment_id of this CreateMetastoreDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def default_managed_table_location(self):
        """
        **[Required]** Gets the default_managed_table_location of this CreateMetastoreDetails.
        Location under which managed tables will be created by default. This references Object Storage
        using an HDFS URI format. Example: oci://bucket@namespace/sub-dir/


        :return: The default_managed_table_location of this CreateMetastoreDetails.
        :rtype: str
        """
        return self._default_managed_table_location

    @default_managed_table_location.setter
    def default_managed_table_location(self, default_managed_table_location):
        """
        Sets the default_managed_table_location of this CreateMetastoreDetails.
        Location under which managed tables will be created by default. This references Object Storage
        using an HDFS URI format. Example: oci://bucket@namespace/sub-dir/


        :param default_managed_table_location: The default_managed_table_location of this CreateMetastoreDetails.
        :type: str
        """
        self._default_managed_table_location = default_managed_table_location

    @property
    def default_external_table_location(self):
        """
        **[Required]** Gets the default_external_table_location of this CreateMetastoreDetails.
        Location under which external tables will be created by default. This references Object Storage
        using an HDFS URI format. Example: oci://bucket@namespace/sub-dir/


        :return: The default_external_table_location of this CreateMetastoreDetails.
        :rtype: str
        """
        return self._default_external_table_location

    @default_external_table_location.setter
    def default_external_table_location(self, default_external_table_location):
        """
        Sets the default_external_table_location of this CreateMetastoreDetails.
        Location under which external tables will be created by default. This references Object Storage
        using an HDFS URI format. Example: oci://bucket@namespace/sub-dir/


        :param default_external_table_location: The default_external_table_location of this CreateMetastoreDetails.
        :type: str
        """
        self._default_external_table_location = default_external_table_location

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateMetastoreDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this CreateMetastoreDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateMetastoreDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this CreateMetastoreDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateMetastoreDetails.
        Usage of predefined tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this CreateMetastoreDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateMetastoreDetails.
        Usage of predefined tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this CreateMetastoreDetails.
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
