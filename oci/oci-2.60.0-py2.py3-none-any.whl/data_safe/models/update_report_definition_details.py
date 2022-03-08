# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateReportDefinitionDetails(object):
    """
    Description of a new report definition.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateReportDefinitionDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this UpdateReportDefinitionDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this UpdateReportDefinitionDetails.
        :type description: str

        :param column_info:
            The value to assign to the column_info property of this UpdateReportDefinitionDetails.
        :type column_info: list[oci.data_safe.models.Column]

        :param column_filters:
            The value to assign to the column_filters property of this UpdateReportDefinitionDetails.
        :type column_filters: list[oci.data_safe.models.ColumnFilter]

        :param column_sortings:
            The value to assign to the column_sortings property of this UpdateReportDefinitionDetails.
        :type column_sortings: list[oci.data_safe.models.ColumnSorting]

        :param summary:
            The value to assign to the summary property of this UpdateReportDefinitionDetails.
        :type summary: list[oci.data_safe.models.Summary]

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateReportDefinitionDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateReportDefinitionDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'description': 'str',
            'column_info': 'list[Column]',
            'column_filters': 'list[ColumnFilter]',
            'column_sortings': 'list[ColumnSorting]',
            'summary': 'list[Summary]',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'description': 'description',
            'column_info': 'columnInfo',
            'column_filters': 'columnFilters',
            'column_sortings': 'columnSortings',
            'summary': 'summary',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._display_name = None
        self._description = None
        self._column_info = None
        self._column_filters = None
        self._column_sortings = None
        self._summary = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this UpdateReportDefinitionDetails.
        Specifies the name of the report definition.


        :return: The display_name of this UpdateReportDefinitionDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateReportDefinitionDetails.
        Specifies the name of the report definition.


        :param display_name: The display_name of this UpdateReportDefinitionDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this UpdateReportDefinitionDetails.
        A description of the report definition.


        :return: The description of this UpdateReportDefinitionDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this UpdateReportDefinitionDetails.
        A description of the report definition.


        :param description: The description of this UpdateReportDefinitionDetails.
        :type: str
        """
        self._description = description

    @property
    def column_info(self):
        """
        **[Required]** Gets the column_info of this UpdateReportDefinitionDetails.
        An array of column objects in the order (left to right) displayed in the report. A column object stores all information about a column, including the name displayed on the UI, corresponding field name in the data source, data type of the column, and column visibility (if the column is visible to the user).


        :return: The column_info of this UpdateReportDefinitionDetails.
        :rtype: list[oci.data_safe.models.Column]
        """
        return self._column_info

    @column_info.setter
    def column_info(self, column_info):
        """
        Sets the column_info of this UpdateReportDefinitionDetails.
        An array of column objects in the order (left to right) displayed in the report. A column object stores all information about a column, including the name displayed on the UI, corresponding field name in the data source, data type of the column, and column visibility (if the column is visible to the user).


        :param column_info: The column_info of this UpdateReportDefinitionDetails.
        :type: list[oci.data_safe.models.Column]
        """
        self._column_info = column_info

    @property
    def column_filters(self):
        """
        **[Required]** Gets the column_filters of this UpdateReportDefinitionDetails.
        An array of column filter objects. A column Filter object stores all information about a column filter including field name, an operator, one or more expressions, if the filter is enabled, or if the filter is hidden.


        :return: The column_filters of this UpdateReportDefinitionDetails.
        :rtype: list[oci.data_safe.models.ColumnFilter]
        """
        return self._column_filters

    @column_filters.setter
    def column_filters(self, column_filters):
        """
        Sets the column_filters of this UpdateReportDefinitionDetails.
        An array of column filter objects. A column Filter object stores all information about a column filter including field name, an operator, one or more expressions, if the filter is enabled, or if the filter is hidden.


        :param column_filters: The column_filters of this UpdateReportDefinitionDetails.
        :type: list[oci.data_safe.models.ColumnFilter]
        """
        self._column_filters = column_filters

    @property
    def column_sortings(self):
        """
        **[Required]** Gets the column_sortings of this UpdateReportDefinitionDetails.
        An array of column sorting objects. Each column sorting object stores the column name to be sorted and if the sorting is in ascending order; sorting is done by the first column in the array, then by the second column in the array, etc.


        :return: The column_sortings of this UpdateReportDefinitionDetails.
        :rtype: list[oci.data_safe.models.ColumnSorting]
        """
        return self._column_sortings

    @column_sortings.setter
    def column_sortings(self, column_sortings):
        """
        Sets the column_sortings of this UpdateReportDefinitionDetails.
        An array of column sorting objects. Each column sorting object stores the column name to be sorted and if the sorting is in ascending order; sorting is done by the first column in the array, then by the second column in the array, etc.


        :param column_sortings: The column_sortings of this UpdateReportDefinitionDetails.
        :type: list[oci.data_safe.models.ColumnSorting]
        """
        self._column_sortings = column_sortings

    @property
    def summary(self):
        """
        **[Required]** Gets the summary of this UpdateReportDefinitionDetails.
        An array of report summary objects in the order (left to right)  displayed in the report.  A  report summary object stores all information about summary of report to be displayed, including the name displayed on UI, the display order, corresponding group by and count of values, summary visibility (if the summary is visible to user).


        :return: The summary of this UpdateReportDefinitionDetails.
        :rtype: list[oci.data_safe.models.Summary]
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """
        Sets the summary of this UpdateReportDefinitionDetails.
        An array of report summary objects in the order (left to right)  displayed in the report.  A  report summary object stores all information about summary of report to be displayed, including the name displayed on UI, the display order, corresponding group by and count of values, summary visibility (if the summary is visible to user).


        :param summary: The summary of this UpdateReportDefinitionDetails.
        :type: list[oci.data_safe.models.Summary]
        """
        self._summary = summary

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateReportDefinitionDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see `Resource Tags`__

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this UpdateReportDefinitionDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateReportDefinitionDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see `Resource Tags`__

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this UpdateReportDefinitionDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateReportDefinitionDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this UpdateReportDefinitionDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateReportDefinitionDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this UpdateReportDefinitionDetails.
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
