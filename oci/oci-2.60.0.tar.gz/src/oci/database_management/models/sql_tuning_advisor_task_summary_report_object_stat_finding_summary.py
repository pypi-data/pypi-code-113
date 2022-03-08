# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SqlTuningAdvisorTaskSummaryReportObjectStatFindingSummary(object):
    """
    A summary for all the statistic findings of an object in a SQL Tuning Advisor task. Includes the object's hash, name, type, schema, problem type and the object reference count.
    """

    #: A constant which can be used with the problem_type property of a SqlTuningAdvisorTaskSummaryReportObjectStatFindingSummary.
    #: This constant has a value of "MISSING"
    PROBLEM_TYPE_MISSING = "MISSING"

    #: A constant which can be used with the problem_type property of a SqlTuningAdvisorTaskSummaryReportObjectStatFindingSummary.
    #: This constant has a value of "STALE"
    PROBLEM_TYPE_STALE = "STALE"

    def __init__(self, **kwargs):
        """
        Initializes a new SqlTuningAdvisorTaskSummaryReportObjectStatFindingSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param object_hash_value:
            The value to assign to the object_hash_value property of this SqlTuningAdvisorTaskSummaryReportObjectStatFindingSummary.
        :type object_hash_value: int

        :param object_name:
            The value to assign to the object_name property of this SqlTuningAdvisorTaskSummaryReportObjectStatFindingSummary.
        :type object_name: str

        :param object_type:
            The value to assign to the object_type property of this SqlTuningAdvisorTaskSummaryReportObjectStatFindingSummary.
        :type object_type: str

        :param schema:
            The value to assign to the schema property of this SqlTuningAdvisorTaskSummaryReportObjectStatFindingSummary.
        :type schema: str

        :param problem_type:
            The value to assign to the problem_type property of this SqlTuningAdvisorTaskSummaryReportObjectStatFindingSummary.
            Allowed values for this property are: "MISSING", "STALE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type problem_type: str

        :param reference_count:
            The value to assign to the reference_count property of this SqlTuningAdvisorTaskSummaryReportObjectStatFindingSummary.
        :type reference_count: int

        """
        self.swagger_types = {
            'object_hash_value': 'int',
            'object_name': 'str',
            'object_type': 'str',
            'schema': 'str',
            'problem_type': 'str',
            'reference_count': 'int'
        }

        self.attribute_map = {
            'object_hash_value': 'objectHashValue',
            'object_name': 'objectName',
            'object_type': 'objectType',
            'schema': 'schema',
            'problem_type': 'problemType',
            'reference_count': 'referenceCount'
        }

        self._object_hash_value = None
        self._object_name = None
        self._object_type = None
        self._schema = None
        self._problem_type = None
        self._reference_count = None

    @property
    def object_hash_value(self):
        """
        **[Required]** Gets the object_hash_value of this SqlTuningAdvisorTaskSummaryReportObjectStatFindingSummary.
        Numerical representation of the object.


        :return: The object_hash_value of this SqlTuningAdvisorTaskSummaryReportObjectStatFindingSummary.
        :rtype: int
        """
        return self._object_hash_value

    @object_hash_value.setter
    def object_hash_value(self, object_hash_value):
        """
        Sets the object_hash_value of this SqlTuningAdvisorTaskSummaryReportObjectStatFindingSummary.
        Numerical representation of the object.


        :param object_hash_value: The object_hash_value of this SqlTuningAdvisorTaskSummaryReportObjectStatFindingSummary.
        :type: int
        """
        self._object_hash_value = object_hash_value

    @property
    def object_name(self):
        """
        **[Required]** Gets the object_name of this SqlTuningAdvisorTaskSummaryReportObjectStatFindingSummary.
        Name of the object.


        :return: The object_name of this SqlTuningAdvisorTaskSummaryReportObjectStatFindingSummary.
        :rtype: str
        """
        return self._object_name

    @object_name.setter
    def object_name(self, object_name):
        """
        Sets the object_name of this SqlTuningAdvisorTaskSummaryReportObjectStatFindingSummary.
        Name of the object.


        :param object_name: The object_name of this SqlTuningAdvisorTaskSummaryReportObjectStatFindingSummary.
        :type: str
        """
        self._object_name = object_name

    @property
    def object_type(self):
        """
        **[Required]** Gets the object_type of this SqlTuningAdvisorTaskSummaryReportObjectStatFindingSummary.
        Type of the object.


        :return: The object_type of this SqlTuningAdvisorTaskSummaryReportObjectStatFindingSummary.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this SqlTuningAdvisorTaskSummaryReportObjectStatFindingSummary.
        Type of the object.


        :param object_type: The object_type of this SqlTuningAdvisorTaskSummaryReportObjectStatFindingSummary.
        :type: str
        """
        self._object_type = object_type

    @property
    def schema(self):
        """
        **[Required]** Gets the schema of this SqlTuningAdvisorTaskSummaryReportObjectStatFindingSummary.
        Schema of the object.


        :return: The schema of this SqlTuningAdvisorTaskSummaryReportObjectStatFindingSummary.
        :rtype: str
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        """
        Sets the schema of this SqlTuningAdvisorTaskSummaryReportObjectStatFindingSummary.
        Schema of the object.


        :param schema: The schema of this SqlTuningAdvisorTaskSummaryReportObjectStatFindingSummary.
        :type: str
        """
        self._schema = schema

    @property
    def problem_type(self):
        """
        **[Required]** Gets the problem_type of this SqlTuningAdvisorTaskSummaryReportObjectStatFindingSummary.
        Type of statistics problem related to the object.

        Allowed values for this property are: "MISSING", "STALE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The problem_type of this SqlTuningAdvisorTaskSummaryReportObjectStatFindingSummary.
        :rtype: str
        """
        return self._problem_type

    @problem_type.setter
    def problem_type(self, problem_type):
        """
        Sets the problem_type of this SqlTuningAdvisorTaskSummaryReportObjectStatFindingSummary.
        Type of statistics problem related to the object.


        :param problem_type: The problem_type of this SqlTuningAdvisorTaskSummaryReportObjectStatFindingSummary.
        :type: str
        """
        allowed_values = ["MISSING", "STALE"]
        if not value_allowed_none_or_none_sentinel(problem_type, allowed_values):
            problem_type = 'UNKNOWN_ENUM_VALUE'
        self._problem_type = problem_type

    @property
    def reference_count(self):
        """
        **[Required]** Gets the reference_count of this SqlTuningAdvisorTaskSummaryReportObjectStatFindingSummary.
        The number of the times the object is referenced within the SQL Tuning advisor task findings.


        :return: The reference_count of this SqlTuningAdvisorTaskSummaryReportObjectStatFindingSummary.
        :rtype: int
        """
        return self._reference_count

    @reference_count.setter
    def reference_count(self, reference_count):
        """
        Sets the reference_count of this SqlTuningAdvisorTaskSummaryReportObjectStatFindingSummary.
        The number of the times the object is referenced within the SQL Tuning advisor task findings.


        :param reference_count: The reference_count of this SqlTuningAdvisorTaskSummaryReportObjectStatFindingSummary.
        :type: int
        """
        self._reference_count = reference_count

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
