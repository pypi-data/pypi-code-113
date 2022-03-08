# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class WorkRequestResource(object):
    """
    A resource related to a Data Flow work request.
    """

    #: A constant which can be used with the action_type property of a WorkRequestResource.
    #: This constant has a value of "CREATED"
    ACTION_TYPE_CREATED = "CREATED"

    #: A constant which can be used with the action_type property of a WorkRequestResource.
    #: This constant has a value of "UPDATED"
    ACTION_TYPE_UPDATED = "UPDATED"

    #: A constant which can be used with the action_type property of a WorkRequestResource.
    #: This constant has a value of "DELETED"
    ACTION_TYPE_DELETED = "DELETED"

    #: A constant which can be used with the action_type property of a WorkRequestResource.
    #: This constant has a value of "INPROGRESS"
    ACTION_TYPE_INPROGRESS = "INPROGRESS"

    #: A constant which can be used with the action_type property of a WorkRequestResource.
    #: This constant has a value of "RELATED"
    ACTION_TYPE_RELATED = "RELATED"

    def __init__(self, **kwargs):
        """
        Initializes a new WorkRequestResource object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param action_type:
            The value to assign to the action_type property of this WorkRequestResource.
            Allowed values for this property are: "CREATED", "UPDATED", "DELETED", "INPROGRESS", "RELATED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type action_type: str

        :param id:
            The value to assign to the id property of this WorkRequestResource.
        :type id: int

        :param resource_id:
            The value to assign to the resource_id property of this WorkRequestResource.
        :type resource_id: str

        :param resource_type:
            The value to assign to the resource_type property of this WorkRequestResource.
        :type resource_type: str

        :param resource_uri:
            The value to assign to the resource_uri property of this WorkRequestResource.
        :type resource_uri: str

        :param work_requestid:
            The value to assign to the work_requestid property of this WorkRequestResource.
        :type work_requestid: str

        """
        self.swagger_types = {
            'action_type': 'str',
            'id': 'int',
            'resource_id': 'str',
            'resource_type': 'str',
            'resource_uri': 'str',
            'work_requestid': 'str'
        }

        self.attribute_map = {
            'action_type': 'actionType',
            'id': 'id',
            'resource_id': 'resourceId',
            'resource_type': 'resourceType',
            'resource_uri': 'resourceUri',
            'work_requestid': 'workRequestid'
        }

        self._action_type = None
        self._id = None
        self._resource_id = None
        self._resource_type = None
        self._resource_uri = None
        self._work_requestid = None

    @property
    def action_type(self):
        """
        **[Required]** Gets the action_type of this WorkRequestResource.
        The way in which this resource is affected by the work tracked in the work request.

        Allowed values for this property are: "CREATED", "UPDATED", "DELETED", "INPROGRESS", "RELATED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The action_type of this WorkRequestResource.
        :rtype: str
        """
        return self._action_type

    @action_type.setter
    def action_type(self, action_type):
        """
        Sets the action_type of this WorkRequestResource.
        The way in which this resource is affected by the work tracked in the work request.


        :param action_type: The action_type of this WorkRequestResource.
        :type: str
        """
        allowed_values = ["CREATED", "UPDATED", "DELETED", "INPROGRESS", "RELATED"]
        if not value_allowed_none_or_none_sentinel(action_type, allowed_values):
            action_type = 'UNKNOWN_ENUM_VALUE'
        self._action_type = action_type

    @property
    def id(self):
        """
        Gets the id of this WorkRequestResource.
        The id of a work request resource object.


        :return: The id of this WorkRequestResource.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this WorkRequestResource.
        The id of a work request resource object.


        :param id: The id of this WorkRequestResource.
        :type: int
        """
        self._id = id

    @property
    def resource_id(self):
        """
        **[Required]** Gets the resource_id of this WorkRequestResource.
        The id of the releated resource. See resourceType to identity the specific type of resource.


        :return: The resource_id of this WorkRequestResource.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """
        Sets the resource_id of this WorkRequestResource.
        The id of the releated resource. See resourceType to identity the specific type of resource.


        :param resource_id: The resource_id of this WorkRequestResource.
        :type: str
        """
        self._resource_id = resource_id

    @property
    def resource_type(self):
        """
        **[Required]** Gets the resource_type of this WorkRequestResource.
        The type of resource.  See resourceId for the id of the specific resource.


        :return: The resource_type of this WorkRequestResource.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """
        Sets the resource_type of this WorkRequestResource.
        The type of resource.  See resourceId for the id of the specific resource.


        :param resource_type: The resource_type of this WorkRequestResource.
        :type: str
        """
        self._resource_type = resource_type

    @property
    def resource_uri(self):
        """
        Gets the resource_uri of this WorkRequestResource.
        The URI path that the user can use to get access to the resource metadata


        :return: The resource_uri of this WorkRequestResource.
        :rtype: str
        """
        return self._resource_uri

    @resource_uri.setter
    def resource_uri(self, resource_uri):
        """
        Sets the resource_uri of this WorkRequestResource.
        The URI path that the user can use to get access to the resource metadata


        :param resource_uri: The resource_uri of this WorkRequestResource.
        :type: str
        """
        self._resource_uri = resource_uri

    @property
    def work_requestid(self):
        """
        Gets the work_requestid of this WorkRequestResource.
        The OCID of a work request.


        :return: The work_requestid of this WorkRequestResource.
        :rtype: str
        """
        return self._work_requestid

    @work_requestid.setter
    def work_requestid(self, work_requestid):
        """
        Sets the work_requestid of this WorkRequestResource.
        The OCID of a work request.


        :param work_requestid: The work_requestid of this WorkRequestResource.
        :type: str
        """
        self._work_requestid = work_requestid

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
