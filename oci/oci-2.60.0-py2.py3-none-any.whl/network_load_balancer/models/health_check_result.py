# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class HealthCheckResult(object):
    """
    Information about a single backend server health check result reported by a network load balancer.
    """

    #: A constant which can be used with the health_check_status property of a HealthCheckResult.
    #: This constant has a value of "OK"
    HEALTH_CHECK_STATUS_OK = "OK"

    #: A constant which can be used with the health_check_status property of a HealthCheckResult.
    #: This constant has a value of "INVALID_STATUS_CODE"
    HEALTH_CHECK_STATUS_INVALID_STATUS_CODE = "INVALID_STATUS_CODE"

    #: A constant which can be used with the health_check_status property of a HealthCheckResult.
    #: This constant has a value of "TIMED_OUT"
    HEALTH_CHECK_STATUS_TIMED_OUT = "TIMED_OUT"

    #: A constant which can be used with the health_check_status property of a HealthCheckResult.
    #: This constant has a value of "HEALTH_PAYLOAD_MISMATCH"
    HEALTH_CHECK_STATUS_HEALTH_PAYLOAD_MISMATCH = "HEALTH_PAYLOAD_MISMATCH"

    #: A constant which can be used with the health_check_status property of a HealthCheckResult.
    #: This constant has a value of "CONNECT_FAILED"
    HEALTH_CHECK_STATUS_CONNECT_FAILED = "CONNECT_FAILED"

    #: A constant which can be used with the health_check_status property of a HealthCheckResult.
    #: This constant has a value of "UNKNOWN"
    HEALTH_CHECK_STATUS_UNKNOWN = "UNKNOWN"

    def __init__(self, **kwargs):
        """
        Initializes a new HealthCheckResult object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param timestamp:
            The value to assign to the timestamp property of this HealthCheckResult.
        :type timestamp: datetime

        :param health_check_status:
            The value to assign to the health_check_status property of this HealthCheckResult.
            Allowed values for this property are: "OK", "INVALID_STATUS_CODE", "TIMED_OUT", "HEALTH_PAYLOAD_MISMATCH", "CONNECT_FAILED", "UNKNOWN", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type health_check_status: str

        """
        self.swagger_types = {
            'timestamp': 'datetime',
            'health_check_status': 'str'
        }

        self.attribute_map = {
            'timestamp': 'timestamp',
            'health_check_status': 'healthCheckStatus'
        }

        self._timestamp = None
        self._health_check_status = None

    @property
    def timestamp(self):
        """
        **[Required]** Gets the timestamp of this HealthCheckResult.
        The date and time the data was retrieved, in the format defined by RFC3339.

        Example: `2020-05-01T18:28:11+00:00`


        :return: The timestamp of this HealthCheckResult.
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """
        Sets the timestamp of this HealthCheckResult.
        The date and time the data was retrieved, in the format defined by RFC3339.

        Example: `2020-05-01T18:28:11+00:00`


        :param timestamp: The timestamp of this HealthCheckResult.
        :type: datetime
        """
        self._timestamp = timestamp

    @property
    def health_check_status(self):
        """
        **[Required]** Gets the health_check_status of this HealthCheckResult.
        The result of the most recent health check.

        Allowed values for this property are: "OK", "INVALID_STATUS_CODE", "TIMED_OUT", "HEALTH_PAYLOAD_MISMATCH", "CONNECT_FAILED", "UNKNOWN", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The health_check_status of this HealthCheckResult.
        :rtype: str
        """
        return self._health_check_status

    @health_check_status.setter
    def health_check_status(self, health_check_status):
        """
        Sets the health_check_status of this HealthCheckResult.
        The result of the most recent health check.


        :param health_check_status: The health_check_status of this HealthCheckResult.
        :type: str
        """
        allowed_values = ["OK", "INVALID_STATUS_CODE", "TIMED_OUT", "HEALTH_PAYLOAD_MISMATCH", "CONNECT_FAILED", "UNKNOWN"]
        if not value_allowed_none_or_none_sentinel(health_check_status, allowed_values):
            health_check_status = 'UNKNOWN_ENUM_VALUE'
        self._health_check_status = health_check_status

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
