# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Sighting(object):
    """
    Sighting details.
    """

    #: A constant which can be used with the classification_status property of a Sighting.
    #: This constant has a value of "FALSE_POSITIVE"
    CLASSIFICATION_STATUS_FALSE_POSITIVE = "FALSE_POSITIVE"

    #: A constant which can be used with the classification_status property of a Sighting.
    #: This constant has a value of "FALSE_NEGATIVE"
    CLASSIFICATION_STATUS_FALSE_NEGATIVE = "FALSE_NEGATIVE"

    #: A constant which can be used with the classification_status property of a Sighting.
    #: This constant has a value of "TRUE_POSITIVE"
    CLASSIFICATION_STATUS_TRUE_POSITIVE = "TRUE_POSITIVE"

    #: A constant which can be used with the classification_status property of a Sighting.
    #: This constant has a value of "TRUE_NEGATIVE"
    CLASSIFICATION_STATUS_TRUE_NEGATIVE = "TRUE_NEGATIVE"

    #: A constant which can be used with the classification_status property of a Sighting.
    #: This constant has a value of "NOT_CLASSIFIED"
    CLASSIFICATION_STATUS_NOT_CLASSIFIED = "NOT_CLASSIFIED"

    #: A constant which can be used with the severity property of a Sighting.
    #: This constant has a value of "CRITICAL"
    SEVERITY_CRITICAL = "CRITICAL"

    #: A constant which can be used with the severity property of a Sighting.
    #: This constant has a value of "HIGH"
    SEVERITY_HIGH = "HIGH"

    #: A constant which can be used with the severity property of a Sighting.
    #: This constant has a value of "MEDIUM"
    SEVERITY_MEDIUM = "MEDIUM"

    #: A constant which can be used with the severity property of a Sighting.
    #: This constant has a value of "LOW"
    SEVERITY_LOW = "LOW"

    #: A constant which can be used with the severity property of a Sighting.
    #: This constant has a value of "MINOR"
    SEVERITY_MINOR = "MINOR"

    #: A constant which can be used with the confidence property of a Sighting.
    #: This constant has a value of "CRITICAL"
    CONFIDENCE_CRITICAL = "CRITICAL"

    #: A constant which can be used with the confidence property of a Sighting.
    #: This constant has a value of "HIGH"
    CONFIDENCE_HIGH = "HIGH"

    #: A constant which can be used with the confidence property of a Sighting.
    #: This constant has a value of "MEDIUM"
    CONFIDENCE_MEDIUM = "MEDIUM"

    #: A constant which can be used with the confidence property of a Sighting.
    #: This constant has a value of "LOW"
    CONFIDENCE_LOW = "LOW"

    #: A constant which can be used with the confidence property of a Sighting.
    #: This constant has a value of "MINOR"
    CONFIDENCE_MINOR = "MINOR"

    def __init__(self, **kwargs):
        """
        Initializes a new Sighting object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this Sighting.
        :type id: str

        :param description:
            The value to assign to the description property of this Sighting.
        :type description: str

        :param problem_id:
            The value to assign to the problem_id property of this Sighting.
        :type problem_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this Sighting.
        :type compartment_id: str

        :param actor_principal_id:
            The value to assign to the actor_principal_id property of this Sighting.
        :type actor_principal_id: str

        :param actor_principal_name:
            The value to assign to the actor_principal_name property of this Sighting.
        :type actor_principal_name: str

        :param actor_principal_type:
            The value to assign to the actor_principal_type property of this Sighting.
        :type actor_principal_type: str

        :param classification_status:
            The value to assign to the classification_status property of this Sighting.
            Allowed values for this property are: "FALSE_POSITIVE", "FALSE_NEGATIVE", "TRUE_POSITIVE", "TRUE_NEGATIVE", "NOT_CLASSIFIED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type classification_status: str

        :param sighting_type:
            The value to assign to the sighting_type property of this Sighting.
        :type sighting_type: str

        :param sighting_type_display_name:
            The value to assign to the sighting_type_display_name property of this Sighting.
        :type sighting_type_display_name: str

        :param tactic_name:
            The value to assign to the tactic_name property of this Sighting.
        :type tactic_name: str

        :param technique_name:
            The value to assign to the technique_name property of this Sighting.
        :type technique_name: str

        :param sighting_score:
            The value to assign to the sighting_score property of this Sighting.
        :type sighting_score: int

        :param risk_score:
            The value to assign to the risk_score property of this Sighting.
        :type risk_score: float

        :param severity:
            The value to assign to the severity property of this Sighting.
            Allowed values for this property are: "CRITICAL", "HIGH", "MEDIUM", "LOW", "MINOR", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type severity: str

        :param confidence:
            The value to assign to the confidence property of this Sighting.
            Allowed values for this property are: "CRITICAL", "HIGH", "MEDIUM", "LOW", "MINOR", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type confidence: str

        :param time_first_detected:
            The value to assign to the time_first_detected property of this Sighting.
        :type time_first_detected: datetime

        :param time_last_detected:
            The value to assign to the time_last_detected property of this Sighting.
        :type time_last_detected: datetime

        :param regions:
            The value to assign to the regions property of this Sighting.
        :type regions: list[str]

        :param additional_details:
            The value to assign to the additional_details property of this Sighting.
        :type additional_details: dict(str, str)

        """
        self.swagger_types = {
            'id': 'str',
            'description': 'str',
            'problem_id': 'str',
            'compartment_id': 'str',
            'actor_principal_id': 'str',
            'actor_principal_name': 'str',
            'actor_principal_type': 'str',
            'classification_status': 'str',
            'sighting_type': 'str',
            'sighting_type_display_name': 'str',
            'tactic_name': 'str',
            'technique_name': 'str',
            'sighting_score': 'int',
            'risk_score': 'float',
            'severity': 'str',
            'confidence': 'str',
            'time_first_detected': 'datetime',
            'time_last_detected': 'datetime',
            'regions': 'list[str]',
            'additional_details': 'dict(str, str)'
        }

        self.attribute_map = {
            'id': 'id',
            'description': 'description',
            'problem_id': 'problemId',
            'compartment_id': 'compartmentId',
            'actor_principal_id': 'actorPrincipalId',
            'actor_principal_name': 'actorPrincipalName',
            'actor_principal_type': 'actorPrincipalType',
            'classification_status': 'classificationStatus',
            'sighting_type': 'sightingType',
            'sighting_type_display_name': 'sightingTypeDisplayName',
            'tactic_name': 'tacticName',
            'technique_name': 'techniqueName',
            'sighting_score': 'sightingScore',
            'risk_score': 'riskScore',
            'severity': 'severity',
            'confidence': 'confidence',
            'time_first_detected': 'timeFirstDetected',
            'time_last_detected': 'timeLastDetected',
            'regions': 'regions',
            'additional_details': 'additionalDetails'
        }

        self._id = None
        self._description = None
        self._problem_id = None
        self._compartment_id = None
        self._actor_principal_id = None
        self._actor_principal_name = None
        self._actor_principal_type = None
        self._classification_status = None
        self._sighting_type = None
        self._sighting_type_display_name = None
        self._tactic_name = None
        self._technique_name = None
        self._sighting_score = None
        self._risk_score = None
        self._severity = None
        self._confidence = None
        self._time_first_detected = None
        self._time_last_detected = None
        self._regions = None
        self._additional_details = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this Sighting.
        Unique identifier for sighting event


        :return: The id of this Sighting.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Sighting.
        Unique identifier for sighting event


        :param id: The id of this Sighting.
        :type: str
        """
        self._id = id

    @property
    def description(self):
        """
        **[Required]** Gets the description of this Sighting.
        Description of the sighting event


        :return: The description of this Sighting.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Sighting.
        Description of the sighting event


        :param description: The description of this Sighting.
        :type: str
        """
        self._description = description

    @property
    def problem_id(self):
        """
        Gets the problem_id of this Sighting.
        Problem Id to which the Sighting is associated


        :return: The problem_id of this Sighting.
        :rtype: str
        """
        return self._problem_id

    @problem_id.setter
    def problem_id(self, problem_id):
        """
        Sets the problem_id of this Sighting.
        Problem Id to which the Sighting is associated


        :param problem_id: The problem_id of this Sighting.
        :type: str
        """
        self._problem_id = problem_id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this Sighting.
        Compartment Id where the resource is created


        :return: The compartment_id of this Sighting.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this Sighting.
        Compartment Id where the resource is created


        :param compartment_id: The compartment_id of this Sighting.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def actor_principal_id(self):
        """
        Gets the actor_principal_id of this Sighting.
        Unique identifier for principal actor


        :return: The actor_principal_id of this Sighting.
        :rtype: str
        """
        return self._actor_principal_id

    @actor_principal_id.setter
    def actor_principal_id(self, actor_principal_id):
        """
        Sets the actor_principal_id of this Sighting.
        Unique identifier for principal actor


        :param actor_principal_id: The actor_principal_id of this Sighting.
        :type: str
        """
        self._actor_principal_id = actor_principal_id

    @property
    def actor_principal_name(self):
        """
        Gets the actor_principal_name of this Sighting.
        Name of the principal actor


        :return: The actor_principal_name of this Sighting.
        :rtype: str
        """
        return self._actor_principal_name

    @actor_principal_name.setter
    def actor_principal_name(self, actor_principal_name):
        """
        Sets the actor_principal_name of this Sighting.
        Name of the principal actor


        :param actor_principal_name: The actor_principal_name of this Sighting.
        :type: str
        """
        self._actor_principal_name = actor_principal_name

    @property
    def actor_principal_type(self):
        """
        Gets the actor_principal_type of this Sighting.
        Type of the principal actor


        :return: The actor_principal_type of this Sighting.
        :rtype: str
        """
        return self._actor_principal_type

    @actor_principal_type.setter
    def actor_principal_type(self, actor_principal_type):
        """
        Sets the actor_principal_type of this Sighting.
        Type of the principal actor


        :param actor_principal_type: The actor_principal_type of this Sighting.
        :type: str
        """
        self._actor_principal_type = actor_principal_type

    @property
    def classification_status(self):
        """
        **[Required]** Gets the classification_status of this Sighting.
        ClassificationStatus of the sighting event

        Allowed values for this property are: "FALSE_POSITIVE", "FALSE_NEGATIVE", "TRUE_POSITIVE", "TRUE_NEGATIVE", "NOT_CLASSIFIED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The classification_status of this Sighting.
        :rtype: str
        """
        return self._classification_status

    @classification_status.setter
    def classification_status(self, classification_status):
        """
        Sets the classification_status of this Sighting.
        ClassificationStatus of the sighting event


        :param classification_status: The classification_status of this Sighting.
        :type: str
        """
        allowed_values = ["FALSE_POSITIVE", "FALSE_NEGATIVE", "TRUE_POSITIVE", "TRUE_NEGATIVE", "NOT_CLASSIFIED"]
        if not value_allowed_none_or_none_sentinel(classification_status, allowed_values):
            classification_status = 'UNKNOWN_ENUM_VALUE'
        self._classification_status = classification_status

    @property
    def sighting_type(self):
        """
        **[Required]** Gets the sighting_type of this Sighting.
        Identifier for the sighting type


        :return: The sighting_type of this Sighting.
        :rtype: str
        """
        return self._sighting_type

    @sighting_type.setter
    def sighting_type(self, sighting_type):
        """
        Sets the sighting_type of this Sighting.
        Identifier for the sighting type


        :param sighting_type: The sighting_type of this Sighting.
        :type: str
        """
        self._sighting_type = sighting_type

    @property
    def sighting_type_display_name(self):
        """
        **[Required]** Gets the sighting_type_display_name of this Sighting.
        Display name of the sighting type


        :return: The sighting_type_display_name of this Sighting.
        :rtype: str
        """
        return self._sighting_type_display_name

    @sighting_type_display_name.setter
    def sighting_type_display_name(self, sighting_type_display_name):
        """
        Sets the sighting_type_display_name of this Sighting.
        Display name of the sighting type


        :param sighting_type_display_name: The sighting_type_display_name of this Sighting.
        :type: str
        """
        self._sighting_type_display_name = sighting_type_display_name

    @property
    def tactic_name(self):
        """
        **[Required]** Gets the tactic_name of this Sighting.
        Name of the Mitre att&ck tactic


        :return: The tactic_name of this Sighting.
        :rtype: str
        """
        return self._tactic_name

    @tactic_name.setter
    def tactic_name(self, tactic_name):
        """
        Sets the tactic_name of this Sighting.
        Name of the Mitre att&ck tactic


        :param tactic_name: The tactic_name of this Sighting.
        :type: str
        """
        self._tactic_name = tactic_name

    @property
    def technique_name(self):
        """
        **[Required]** Gets the technique_name of this Sighting.
        Name of the Mitre att&ck technique


        :return: The technique_name of this Sighting.
        :rtype: str
        """
        return self._technique_name

    @technique_name.setter
    def technique_name(self, technique_name):
        """
        Sets the technique_name of this Sighting.
        Name of the Mitre att&ck technique


        :param technique_name: The technique_name of this Sighting.
        :type: str
        """
        self._technique_name = technique_name

    @property
    def sighting_score(self):
        """
        **[Required]** Gets the sighting_score of this Sighting.
        Score for the sighting


        :return: The sighting_score of this Sighting.
        :rtype: int
        """
        return self._sighting_score

    @sighting_score.setter
    def sighting_score(self, sighting_score):
        """
        Sets the sighting_score of this Sighting.
        Score for the sighting


        :param sighting_score: The sighting_score of this Sighting.
        :type: int
        """
        self._sighting_score = sighting_score

    @property
    def risk_score(self):
        """
        Gets the risk_score of this Sighting.
        DEPRECATED


        :return: The risk_score of this Sighting.
        :rtype: float
        """
        return self._risk_score

    @risk_score.setter
    def risk_score(self, risk_score):
        """
        Sets the risk_score of this Sighting.
        DEPRECATED


        :param risk_score: The risk_score of this Sighting.
        :type: float
        """
        self._risk_score = risk_score

    @property
    def severity(self):
        """
        **[Required]** Gets the severity of this Sighting.
        Severity of the sighting

        Allowed values for this property are: "CRITICAL", "HIGH", "MEDIUM", "LOW", "MINOR", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The severity of this Sighting.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """
        Sets the severity of this Sighting.
        Severity of the sighting


        :param severity: The severity of this Sighting.
        :type: str
        """
        allowed_values = ["CRITICAL", "HIGH", "MEDIUM", "LOW", "MINOR"]
        if not value_allowed_none_or_none_sentinel(severity, allowed_values):
            severity = 'UNKNOWN_ENUM_VALUE'
        self._severity = severity

    @property
    def confidence(self):
        """
        **[Required]** Gets the confidence of this Sighting.
        Confidence of the sighting

        Allowed values for this property are: "CRITICAL", "HIGH", "MEDIUM", "LOW", "MINOR", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The confidence of this Sighting.
        :rtype: str
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """
        Sets the confidence of this Sighting.
        Confidence of the sighting


        :param confidence: The confidence of this Sighting.
        :type: str
        """
        allowed_values = ["CRITICAL", "HIGH", "MEDIUM", "LOW", "MINOR"]
        if not value_allowed_none_or_none_sentinel(confidence, allowed_values):
            confidence = 'UNKNOWN_ENUM_VALUE'
        self._confidence = confidence

    @property
    def time_first_detected(self):
        """
        **[Required]** Gets the time_first_detected of this Sighting.
        The date and time the sighting was first detected. Format defined by RFC3339.


        :return: The time_first_detected of this Sighting.
        :rtype: datetime
        """
        return self._time_first_detected

    @time_first_detected.setter
    def time_first_detected(self, time_first_detected):
        """
        Sets the time_first_detected of this Sighting.
        The date and time the sighting was first detected. Format defined by RFC3339.


        :param time_first_detected: The time_first_detected of this Sighting.
        :type: datetime
        """
        self._time_first_detected = time_first_detected

    @property
    def time_last_detected(self):
        """
        **[Required]** Gets the time_last_detected of this Sighting.
        The date and time the sighting was last detected. Format defined by RFC3339.


        :return: The time_last_detected of this Sighting.
        :rtype: datetime
        """
        return self._time_last_detected

    @time_last_detected.setter
    def time_last_detected(self, time_last_detected):
        """
        Sets the time_last_detected of this Sighting.
        The date and time the sighting was last detected. Format defined by RFC3339.


        :param time_last_detected: The time_last_detected of this Sighting.
        :type: datetime
        """
        self._time_last_detected = time_last_detected

    @property
    def regions(self):
        """
        **[Required]** Gets the regions of this Sighting.
        regions involved in the sighting


        :return: The regions of this Sighting.
        :rtype: list[str]
        """
        return self._regions

    @regions.setter
    def regions(self, regions):
        """
        Sets the regions of this Sighting.
        regions involved in the sighting


        :param regions: The regions of this Sighting.
        :type: list[str]
        """
        self._regions = regions

    @property
    def additional_details(self):
        """
        Gets the additional_details of this Sighting.
        The additional details of the Sighting


        :return: The additional_details of this Sighting.
        :rtype: dict(str, str)
        """
        return self._additional_details

    @additional_details.setter
    def additional_details(self, additional_details):
        """
        Sets the additional_details of this Sighting.
        The additional details of the Sighting


        :param additional_details: The additional_details of this Sighting.
        :type: dict(str, str)
        """
        self._additional_details = additional_details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
