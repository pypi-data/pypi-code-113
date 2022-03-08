# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class JobRunSummary(object):
    """
    A summary of a specific job run.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new JobRunSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this JobRunSummary.
        :type id: str

        :param name:
            The value to assign to the name property of this JobRunSummary.
        :type name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this JobRunSummary.
        :type compartment_id: str

        :param job_id:
            The value to assign to the job_id property of this JobRunSummary.
        :type job_id: str

        :param job_name:
            The value to assign to the job_name property of this JobRunSummary.
        :type job_name: str

        :param managed_database_group_id:
            The value to assign to the managed_database_group_id property of this JobRunSummary.
        :type managed_database_group_id: str

        :param managed_database_id:
            The value to assign to the managed_database_id property of this JobRunSummary.
        :type managed_database_id: str

        :param run_status:
            The value to assign to the run_status property of this JobRunSummary.
        :type run_status: str

        :param time_submitted:
            The value to assign to the time_submitted property of this JobRunSummary.
        :type time_submitted: datetime

        :param time_updated:
            The value to assign to the time_updated property of this JobRunSummary.
        :type time_updated: datetime

        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'compartment_id': 'str',
            'job_id': 'str',
            'job_name': 'str',
            'managed_database_group_id': 'str',
            'managed_database_id': 'str',
            'run_status': 'str',
            'time_submitted': 'datetime',
            'time_updated': 'datetime'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'compartment_id': 'compartmentId',
            'job_id': 'jobId',
            'job_name': 'jobName',
            'managed_database_group_id': 'managedDatabaseGroupId',
            'managed_database_id': 'managedDatabaseId',
            'run_status': 'runStatus',
            'time_submitted': 'timeSubmitted',
            'time_updated': 'timeUpdated'
        }

        self._id = None
        self._name = None
        self._compartment_id = None
        self._job_id = None
        self._job_name = None
        self._managed_database_group_id = None
        self._managed_database_id = None
        self._run_status = None
        self._time_submitted = None
        self._time_updated = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this JobRunSummary.
        The identifier of the job run.


        :return: The id of this JobRunSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this JobRunSummary.
        The identifier of the job run.


        :param id: The id of this JobRunSummary.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """
        **[Required]** Gets the name of this JobRunSummary.
        The name of the job run.


        :return: The name of this JobRunSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this JobRunSummary.
        The name of the job run.


        :param name: The name of this JobRunSummary.
        :type: str
        """
        self._name = name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this JobRunSummary.
        The `OCID`__ of the compartment in which the parent job resides.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this JobRunSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this JobRunSummary.
        The `OCID`__ of the compartment in which the parent job resides.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this JobRunSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def job_id(self):
        """
        **[Required]** Gets the job_id of this JobRunSummary.
        The `OCID`__ of the parent job.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The job_id of this JobRunSummary.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """
        Sets the job_id of this JobRunSummary.
        The `OCID`__ of the parent job.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param job_id: The job_id of this JobRunSummary.
        :type: str
        """
        self._job_id = job_id

    @property
    def job_name(self):
        """
        **[Required]** Gets the job_name of this JobRunSummary.
        The name of the parent job.


        :return: The job_name of this JobRunSummary.
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        """
        Sets the job_name of this JobRunSummary.
        The name of the parent job.


        :param job_name: The job_name of this JobRunSummary.
        :type: str
        """
        self._job_name = job_name

    @property
    def managed_database_group_id(self):
        """
        Gets the managed_database_group_id of this JobRunSummary.
        The `OCID`__ of the Managed Database Group where the parent job has to be executed.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The managed_database_group_id of this JobRunSummary.
        :rtype: str
        """
        return self._managed_database_group_id

    @managed_database_group_id.setter
    def managed_database_group_id(self, managed_database_group_id):
        """
        Sets the managed_database_group_id of this JobRunSummary.
        The `OCID`__ of the Managed Database Group where the parent job has to be executed.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param managed_database_group_id: The managed_database_group_id of this JobRunSummary.
        :type: str
        """
        self._managed_database_group_id = managed_database_group_id

    @property
    def managed_database_id(self):
        """
        Gets the managed_database_id of this JobRunSummary.
        The `OCID`__ of the Managed Database where the parent job has to be executed.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The managed_database_id of this JobRunSummary.
        :rtype: str
        """
        return self._managed_database_id

    @managed_database_id.setter
    def managed_database_id(self, managed_database_id):
        """
        Sets the managed_database_id of this JobRunSummary.
        The `OCID`__ of the Managed Database where the parent job has to be executed.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param managed_database_id: The managed_database_id of this JobRunSummary.
        :type: str
        """
        self._managed_database_id = managed_database_id

    @property
    def run_status(self):
        """
        **[Required]** Gets the run_status of this JobRunSummary.
        The status of the job run.


        :return: The run_status of this JobRunSummary.
        :rtype: str
        """
        return self._run_status

    @run_status.setter
    def run_status(self, run_status):
        """
        Sets the run_status of this JobRunSummary.
        The status of the job run.


        :param run_status: The run_status of this JobRunSummary.
        :type: str
        """
        self._run_status = run_status

    @property
    def time_submitted(self):
        """
        **[Required]** Gets the time_submitted of this JobRunSummary.
        The date and time when the job run was submitted.


        :return: The time_submitted of this JobRunSummary.
        :rtype: datetime
        """
        return self._time_submitted

    @time_submitted.setter
    def time_submitted(self, time_submitted):
        """
        Sets the time_submitted of this JobRunSummary.
        The date and time when the job run was submitted.


        :param time_submitted: The time_submitted of this JobRunSummary.
        :type: datetime
        """
        self._time_submitted = time_submitted

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this JobRunSummary.
        The date and time when the job run was last updated.


        :return: The time_updated of this JobRunSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this JobRunSummary.
        The date and time when the job run was last updated.


        :param time_updated: The time_updated of this JobRunSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
