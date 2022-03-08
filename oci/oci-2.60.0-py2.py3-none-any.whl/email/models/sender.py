# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Sender(object):
    """
    The full information representing an approved sender.
    """

    #: A constant which can be used with the lifecycle_state property of a Sender.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a Sender.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a Sender.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a Sender.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    def __init__(self, **kwargs):
        """
        Initializes a new Sender object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this Sender.
        :type compartment_id: str

        :param email_address:
            The value to assign to the email_address property of this Sender.
        :type email_address: str

        :param id:
            The value to assign to the id property of this Sender.
        :type id: str

        :param is_spf:
            The value to assign to the is_spf property of this Sender.
        :type is_spf: bool

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this Sender.
            Allowed values for this property are: "CREATING", "ACTIVE", "DELETING", "DELETED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param time_created:
            The value to assign to the time_created property of this Sender.
        :type time_created: datetime

        :param email_domain_id:
            The value to assign to the email_domain_id property of this Sender.
        :type email_domain_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this Sender.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this Sender.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'email_address': 'str',
            'id': 'str',
            'is_spf': 'bool',
            'lifecycle_state': 'str',
            'time_created': 'datetime',
            'email_domain_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'email_address': 'emailAddress',
            'id': 'id',
            'is_spf': 'isSpf',
            'lifecycle_state': 'lifecycleState',
            'time_created': 'timeCreated',
            'email_domain_id': 'emailDomainId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._compartment_id = None
        self._email_address = None
        self._id = None
        self._is_spf = None
        self._lifecycle_state = None
        self._time_created = None
        self._email_domain_id = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this Sender.
        The OCID for the compartment.


        :return: The compartment_id of this Sender.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this Sender.
        The OCID for the compartment.


        :param compartment_id: The compartment_id of this Sender.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def email_address(self):
        """
        **[Required]** Gets the email_address of this Sender.
        Email address of the sender.


        :return: The email_address of this Sender.
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """
        Sets the email_address of this Sender.
        Email address of the sender.


        :param email_address: The email_address of this Sender.
        :type: str
        """
        self._email_address = email_address

    @property
    def id(self):
        """
        **[Required]** Gets the id of this Sender.
        The unique OCID of the sender.


        :return: The id of this Sender.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Sender.
        The unique OCID of the sender.


        :param id: The id of this Sender.
        :type: str
        """
        self._id = id

    @property
    def is_spf(self):
        """
        Gets the is_spf of this Sender.
        Value of the SPF field. For more information about SPF, please see
        `SPF Authentication`__.

        __ https://docs.cloud.oracle.com/Content/Email/Concepts/overview.htm#components


        :return: The is_spf of this Sender.
        :rtype: bool
        """
        return self._is_spf

    @is_spf.setter
    def is_spf(self, is_spf):
        """
        Sets the is_spf of this Sender.
        Value of the SPF field. For more information about SPF, please see
        `SPF Authentication`__.

        __ https://docs.cloud.oracle.com/Content/Email/Concepts/overview.htm#components


        :param is_spf: The is_spf of this Sender.
        :type: bool
        """
        self._is_spf = is_spf

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this Sender.
        The sender's current lifecycle state.

        Allowed values for this property are: "CREATING", "ACTIVE", "DELETING", "DELETED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this Sender.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this Sender.
        The sender's current lifecycle state.


        :param lifecycle_state: The lifecycle_state of this Sender.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "DELETING", "DELETED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def time_created(self):
        """
        Gets the time_created of this Sender.
        The date and time the approved sender was added in \"YYYY-MM-ddThh:mmZ\"
        format with a Z offset, as defined by RFC 3339.


        :return: The time_created of this Sender.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this Sender.
        The date and time the approved sender was added in \"YYYY-MM-ddThh:mmZ\"
        format with a Z offset, as defined by RFC 3339.


        :param time_created: The time_created of this Sender.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def email_domain_id(self):
        """
        Gets the email_domain_id of this Sender.
        The email domain used to assert responsibility for emails sent from this sender.


        :return: The email_domain_id of this Sender.
        :rtype: str
        """
        return self._email_domain_id

    @email_domain_id.setter
    def email_domain_id(self, email_domain_id):
        """
        Sets the email_domain_id of this Sender.
        The email domain used to assert responsibility for emails sent from this sender.


        :param email_domain_id: The email_domain_id of this Sender.
        :type: str
        """
        self._email_domain_id = email_domain_id

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this Sender.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this Sender.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this Sender.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this Sender.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this Sender.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this Sender.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this Sender.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this Sender.
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
