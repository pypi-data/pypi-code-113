# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DeployStageExecutionStep(object):
    """
    Details about each steps in stage execution for a target environment.
    """

    #: A constant which can be used with the state property of a DeployStageExecutionStep.
    #: This constant has a value of "WAITING"
    STATE_WAITING = "WAITING"

    #: A constant which can be used with the state property of a DeployStageExecutionStep.
    #: This constant has a value of "IN_PROGRESS"
    STATE_IN_PROGRESS = "IN_PROGRESS"

    #: A constant which can be used with the state property of a DeployStageExecutionStep.
    #: This constant has a value of "FAILED"
    STATE_FAILED = "FAILED"

    #: A constant which can be used with the state property of a DeployStageExecutionStep.
    #: This constant has a value of "SUCCEEDED"
    STATE_SUCCEEDED = "SUCCEEDED"

    #: A constant which can be used with the state property of a DeployStageExecutionStep.
    #: This constant has a value of "CANCELED"
    STATE_CANCELED = "CANCELED"

    def __init__(self, **kwargs):
        """
        Initializes a new DeployStageExecutionStep object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this DeployStageExecutionStep.
        :type name: str

        :param state:
            The value to assign to the state property of this DeployStageExecutionStep.
            Allowed values for this property are: "WAITING", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type state: str

        :param time_started:
            The value to assign to the time_started property of this DeployStageExecutionStep.
        :type time_started: datetime

        :param time_finished:
            The value to assign to the time_finished property of this DeployStageExecutionStep.
        :type time_finished: datetime

        """
        self.swagger_types = {
            'name': 'str',
            'state': 'str',
            'time_started': 'datetime',
            'time_finished': 'datetime'
        }

        self.attribute_map = {
            'name': 'name',
            'state': 'state',
            'time_started': 'timeStarted',
            'time_finished': 'timeFinished'
        }

        self._name = None
        self._state = None
        self._time_started = None
        self._time_finished = None

    @property
    def name(self):
        """
        Gets the name of this DeployStageExecutionStep.
        Name of the step.


        :return: The name of this DeployStageExecutionStep.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this DeployStageExecutionStep.
        Name of the step.


        :param name: The name of this DeployStageExecutionStep.
        :type: str
        """
        self._name = name

    @property
    def state(self):
        """
        Gets the state of this DeployStageExecutionStep.
        State of the step.

        Allowed values for this property are: "WAITING", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The state of this DeployStageExecutionStep.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this DeployStageExecutionStep.
        State of the step.


        :param state: The state of this DeployStageExecutionStep.
        :type: str
        """
        allowed_values = ["WAITING", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELED"]
        if not value_allowed_none_or_none_sentinel(state, allowed_values):
            state = 'UNKNOWN_ENUM_VALUE'
        self._state = state

    @property
    def time_started(self):
        """
        Gets the time_started of this DeployStageExecutionStep.
        Time when the step started.


        :return: The time_started of this DeployStageExecutionStep.
        :rtype: datetime
        """
        return self._time_started

    @time_started.setter
    def time_started(self, time_started):
        """
        Sets the time_started of this DeployStageExecutionStep.
        Time when the step started.


        :param time_started: The time_started of this DeployStageExecutionStep.
        :type: datetime
        """
        self._time_started = time_started

    @property
    def time_finished(self):
        """
        Gets the time_finished of this DeployStageExecutionStep.
        Time when the step finished.


        :return: The time_finished of this DeployStageExecutionStep.
        :rtype: datetime
        """
        return self._time_finished

    @time_finished.setter
    def time_finished(self, time_finished):
        """
        Sets the time_finished of this DeployStageExecutionStep.
        Time when the step finished.


        :param time_finished: The time_finished of this DeployStageExecutionStep.
        :type: datetime
        """
        self._time_finished = time_finished

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
