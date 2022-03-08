# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ResolverEndpoint(object):
    """
    An OCI DNS resolver endpoint.

    **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.
    """

    #: A constant which can be used with the endpoint_type property of a ResolverEndpoint.
    #: This constant has a value of "VNIC"
    ENDPOINT_TYPE_VNIC = "VNIC"

    #: A constant which can be used with the lifecycle_state property of a ResolverEndpoint.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a ResolverEndpoint.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a ResolverEndpoint.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a ResolverEndpoint.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a ResolverEndpoint.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a ResolverEndpoint.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    def __init__(self, **kwargs):
        """
        Initializes a new ResolverEndpoint object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.dns.models.ResolverVnicEndpoint`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this ResolverEndpoint.
        :type name: str

        :param endpoint_type:
            The value to assign to the endpoint_type property of this ResolverEndpoint.
            Allowed values for this property are: "VNIC", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type endpoint_type: str

        :param forwarding_address:
            The value to assign to the forwarding_address property of this ResolverEndpoint.
        :type forwarding_address: str

        :param is_forwarding:
            The value to assign to the is_forwarding property of this ResolverEndpoint.
        :type is_forwarding: bool

        :param is_listening:
            The value to assign to the is_listening property of this ResolverEndpoint.
        :type is_listening: bool

        :param listening_address:
            The value to assign to the listening_address property of this ResolverEndpoint.
        :type listening_address: str

        :param compartment_id:
            The value to assign to the compartment_id property of this ResolverEndpoint.
        :type compartment_id: str

        :param time_created:
            The value to assign to the time_created property of this ResolverEndpoint.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this ResolverEndpoint.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ResolverEndpoint.
            Allowed values for this property are: "ACTIVE", "CREATING", "DELETED", "DELETING", "FAILED", "UPDATING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param _self:
            The value to assign to the _self property of this ResolverEndpoint.
        :type _self: str

        """
        self.swagger_types = {
            'name': 'str',
            'endpoint_type': 'str',
            'forwarding_address': 'str',
            'is_forwarding': 'bool',
            'is_listening': 'bool',
            'listening_address': 'str',
            'compartment_id': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            '_self': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'endpoint_type': 'endpointType',
            'forwarding_address': 'forwardingAddress',
            'is_forwarding': 'isForwarding',
            'is_listening': 'isListening',
            'listening_address': 'listeningAddress',
            'compartment_id': 'compartmentId',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            '_self': 'self'
        }

        self._name = None
        self._endpoint_type = None
        self._forwarding_address = None
        self._is_forwarding = None
        self._is_listening = None
        self._listening_address = None
        self._compartment_id = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self.__self = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['endpointType']

        if type == 'VNIC':
            return 'ResolverVnicEndpoint'
        else:
            return 'ResolverEndpoint'

    @property
    def name(self):
        """
        **[Required]** Gets the name of this ResolverEndpoint.
        The name of the resolver endpoint. Must be unique, case-insensitive, within the resolver.


        :return: The name of this ResolverEndpoint.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ResolverEndpoint.
        The name of the resolver endpoint. Must be unique, case-insensitive, within the resolver.


        :param name: The name of this ResolverEndpoint.
        :type: str
        """
        self._name = name

    @property
    def endpoint_type(self):
        """
        Gets the endpoint_type of this ResolverEndpoint.
        The type of resolver endpoint. VNIC is currently the only supported type.

        Allowed values for this property are: "VNIC", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The endpoint_type of this ResolverEndpoint.
        :rtype: str
        """
        return self._endpoint_type

    @endpoint_type.setter
    def endpoint_type(self, endpoint_type):
        """
        Sets the endpoint_type of this ResolverEndpoint.
        The type of resolver endpoint. VNIC is currently the only supported type.


        :param endpoint_type: The endpoint_type of this ResolverEndpoint.
        :type: str
        """
        allowed_values = ["VNIC"]
        if not value_allowed_none_or_none_sentinel(endpoint_type, allowed_values):
            endpoint_type = 'UNKNOWN_ENUM_VALUE'
        self._endpoint_type = endpoint_type

    @property
    def forwarding_address(self):
        """
        Gets the forwarding_address of this ResolverEndpoint.
        An IP address from which forwarded queries may be sent. For VNIC endpoints, this IP address must be part
        of the subnet and will be assigned by the system if unspecified when isForwarding is true.


        :return: The forwarding_address of this ResolverEndpoint.
        :rtype: str
        """
        return self._forwarding_address

    @forwarding_address.setter
    def forwarding_address(self, forwarding_address):
        """
        Sets the forwarding_address of this ResolverEndpoint.
        An IP address from which forwarded queries may be sent. For VNIC endpoints, this IP address must be part
        of the subnet and will be assigned by the system if unspecified when isForwarding is true.


        :param forwarding_address: The forwarding_address of this ResolverEndpoint.
        :type: str
        """
        self._forwarding_address = forwarding_address

    @property
    def is_forwarding(self):
        """
        **[Required]** Gets the is_forwarding of this ResolverEndpoint.
        A Boolean flag indicating whether or not the resolver endpoint is for forwarding.


        :return: The is_forwarding of this ResolverEndpoint.
        :rtype: bool
        """
        return self._is_forwarding

    @is_forwarding.setter
    def is_forwarding(self, is_forwarding):
        """
        Sets the is_forwarding of this ResolverEndpoint.
        A Boolean flag indicating whether or not the resolver endpoint is for forwarding.


        :param is_forwarding: The is_forwarding of this ResolverEndpoint.
        :type: bool
        """
        self._is_forwarding = is_forwarding

    @property
    def is_listening(self):
        """
        **[Required]** Gets the is_listening of this ResolverEndpoint.
        A Boolean flag indicating whether or not the resolver endpoint is for listening.


        :return: The is_listening of this ResolverEndpoint.
        :rtype: bool
        """
        return self._is_listening

    @is_listening.setter
    def is_listening(self, is_listening):
        """
        Sets the is_listening of this ResolverEndpoint.
        A Boolean flag indicating whether or not the resolver endpoint is for listening.


        :param is_listening: The is_listening of this ResolverEndpoint.
        :type: bool
        """
        self._is_listening = is_listening

    @property
    def listening_address(self):
        """
        Gets the listening_address of this ResolverEndpoint.
        An IP address to listen to queries on. For VNIC endpoints this IP address must be part of the
        subnet and will be assigned by the system if unspecified when isListening is true.


        :return: The listening_address of this ResolverEndpoint.
        :rtype: str
        """
        return self._listening_address

    @listening_address.setter
    def listening_address(self, listening_address):
        """
        Sets the listening_address of this ResolverEndpoint.
        An IP address to listen to queries on. For VNIC endpoints this IP address must be part of the
        subnet and will be assigned by the system if unspecified when isListening is true.


        :param listening_address: The listening_address of this ResolverEndpoint.
        :type: str
        """
        self._listening_address = listening_address

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this ResolverEndpoint.
        The OCID of the owning compartment. This will match the resolver that the resolver endpoint is under
        and will be updated if the resolver's compartment is changed.


        :return: The compartment_id of this ResolverEndpoint.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ResolverEndpoint.
        The OCID of the owning compartment. This will match the resolver that the resolver endpoint is under
        and will be updated if the resolver's compartment is changed.


        :param compartment_id: The compartment_id of this ResolverEndpoint.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this ResolverEndpoint.
        The date and time the resource was created in \"YYYY-MM-ddThh:mm:ssZ\" format
        with a Z offset, as defined by RFC 3339.

        **Example:** `2016-07-22T17:23:59:60Z`


        :return: The time_created of this ResolverEndpoint.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ResolverEndpoint.
        The date and time the resource was created in \"YYYY-MM-ddThh:mm:ssZ\" format
        with a Z offset, as defined by RFC 3339.

        **Example:** `2016-07-22T17:23:59:60Z`


        :param time_created: The time_created of this ResolverEndpoint.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this ResolverEndpoint.
        The date and time the resource was last updated in \"YYYY-MM-ddThh:mm:ssZ\"
        format with a Z offset, as defined by RFC 3339.

        **Example:** `2016-07-22T17:23:59:60Z`


        :return: The time_updated of this ResolverEndpoint.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this ResolverEndpoint.
        The date and time the resource was last updated in \"YYYY-MM-ddThh:mm:ssZ\"
        format with a Z offset, as defined by RFC 3339.

        **Example:** `2016-07-22T17:23:59:60Z`


        :param time_updated: The time_updated of this ResolverEndpoint.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this ResolverEndpoint.
        The current state of the resource.

        Allowed values for this property are: "ACTIVE", "CREATING", "DELETED", "DELETING", "FAILED", "UPDATING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this ResolverEndpoint.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this ResolverEndpoint.
        The current state of the resource.


        :param lifecycle_state: The lifecycle_state of this ResolverEndpoint.
        :type: str
        """
        allowed_values = ["ACTIVE", "CREATING", "DELETED", "DELETING", "FAILED", "UPDATING"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def _self(self):
        """
        **[Required]** Gets the _self of this ResolverEndpoint.
        The canonical absolute URL of the resource.


        :return: The _self of this ResolverEndpoint.
        :rtype: str
        """
        return self.__self

    @_self.setter
    def _self(self, _self):
        """
        Sets the _self of this ResolverEndpoint.
        The canonical absolute URL of the resource.


        :param _self: The _self of this ResolverEndpoint.
        :type: str
        """
        self.__self = _self

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
