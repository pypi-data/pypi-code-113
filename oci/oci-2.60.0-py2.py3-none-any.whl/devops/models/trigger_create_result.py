# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TriggerCreateResult(object):
    """
    Details of the trigger create response.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new TriggerCreateResult object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.devops.models.GithubTriggerCreateResult`
        * :class:`~oci.devops.models.GitlabTriggerCreateResult`
        * :class:`~oci.devops.models.DevopsCodeRepositoryTriggerCreateResult`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this TriggerCreateResult.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this TriggerCreateResult.
        :type display_name: str

        :param description:
            The value to assign to the description property of this TriggerCreateResult.
        :type description: str

        :param project_id:
            The value to assign to the project_id property of this TriggerCreateResult.
        :type project_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this TriggerCreateResult.
        :type compartment_id: str

        :param trigger_source:
            The value to assign to the trigger_source property of this TriggerCreateResult.
        :type trigger_source: str

        :param time_created:
            The value to assign to the time_created property of this TriggerCreateResult.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this TriggerCreateResult.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this TriggerCreateResult.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this TriggerCreateResult.
        :type lifecycle_details: str

        :param actions:
            The value to assign to the actions property of this TriggerCreateResult.
        :type actions: list[oci.devops.models.TriggerAction]

        :param freeform_tags:
            The value to assign to the freeform_tags property of this TriggerCreateResult.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this TriggerCreateResult.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this TriggerCreateResult.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'description': 'str',
            'project_id': 'str',
            'compartment_id': 'str',
            'trigger_source': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'actions': 'list[TriggerAction]',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'description': 'description',
            'project_id': 'projectId',
            'compartment_id': 'compartmentId',
            'trigger_source': 'triggerSource',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'actions': 'actions',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._id = None
        self._display_name = None
        self._description = None
        self._project_id = None
        self._compartment_id = None
        self._trigger_source = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._actions = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['triggerSource']

        if type == 'GITHUB':
            return 'GithubTriggerCreateResult'

        if type == 'GITLAB':
            return 'GitlabTriggerCreateResult'

        if type == 'DEVOPS_CODE_REPOSITORY':
            return 'DevopsCodeRepositoryTriggerCreateResult'
        else:
            return 'TriggerCreateResult'

    @property
    def id(self):
        """
        **[Required]** Gets the id of this TriggerCreateResult.
        Unique identifier that is immutable on creation.


        :return: The id of this TriggerCreateResult.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this TriggerCreateResult.
        Unique identifier that is immutable on creation.


        :param id: The id of this TriggerCreateResult.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        Gets the display_name of this TriggerCreateResult.
        Trigger display name. Avoid entering confidential information.


        :return: The display_name of this TriggerCreateResult.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this TriggerCreateResult.
        Trigger display name. Avoid entering confidential information.


        :param display_name: The display_name of this TriggerCreateResult.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this TriggerCreateResult.
        Description about the trigger.


        :return: The description of this TriggerCreateResult.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this TriggerCreateResult.
        Description about the trigger.


        :param description: The description of this TriggerCreateResult.
        :type: str
        """
        self._description = description

    @property
    def project_id(self):
        """
        **[Required]** Gets the project_id of this TriggerCreateResult.
        The OCID of the DevOps project to which the trigger belongs to.


        :return: The project_id of this TriggerCreateResult.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """
        Sets the project_id of this TriggerCreateResult.
        The OCID of the DevOps project to which the trigger belongs to.


        :param project_id: The project_id of this TriggerCreateResult.
        :type: str
        """
        self._project_id = project_id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this TriggerCreateResult.
        The OCID of the compartment that contains the trigger.


        :return: The compartment_id of this TriggerCreateResult.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this TriggerCreateResult.
        The OCID of the compartment that contains the trigger.


        :param compartment_id: The compartment_id of this TriggerCreateResult.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def trigger_source(self):
        """
        **[Required]** Gets the trigger_source of this TriggerCreateResult.
        Source of the trigger. Allowed values are, GITHUB and GITLAB.


        :return: The trigger_source of this TriggerCreateResult.
        :rtype: str
        """
        return self._trigger_source

    @trigger_source.setter
    def trigger_source(self, trigger_source):
        """
        Sets the trigger_source of this TriggerCreateResult.
        Source of the trigger. Allowed values are, GITHUB and GITLAB.


        :param trigger_source: The trigger_source of this TriggerCreateResult.
        :type: str
        """
        self._trigger_source = trigger_source

    @property
    def time_created(self):
        """
        Gets the time_created of this TriggerCreateResult.
        The time the trigger was created. Format defined by `RFC3339`__.

        __ https://datatracker.ietf.org/doc/html/rfc3339


        :return: The time_created of this TriggerCreateResult.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this TriggerCreateResult.
        The time the trigger was created. Format defined by `RFC3339`__.

        __ https://datatracker.ietf.org/doc/html/rfc3339


        :param time_created: The time_created of this TriggerCreateResult.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this TriggerCreateResult.
        The time the trigger was updated. Format defined by `RFC3339`__.

        __ https://datatracker.ietf.org/doc/html/rfc3339


        :return: The time_updated of this TriggerCreateResult.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this TriggerCreateResult.
        The time the trigger was updated. Format defined by `RFC3339`__.

        __ https://datatracker.ietf.org/doc/html/rfc3339


        :param time_updated: The time_updated of this TriggerCreateResult.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this TriggerCreateResult.
        The current state of the trigger.


        :return: The lifecycle_state of this TriggerCreateResult.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this TriggerCreateResult.
        The current state of the trigger.


        :param lifecycle_state: The lifecycle_state of this TriggerCreateResult.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this TriggerCreateResult.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :return: The lifecycle_details of this TriggerCreateResult.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this TriggerCreateResult.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :param lifecycle_details: The lifecycle_details of this TriggerCreateResult.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def actions(self):
        """
        **[Required]** Gets the actions of this TriggerCreateResult.
        The list of actions that are to be performed for this trigger.


        :return: The actions of this TriggerCreateResult.
        :rtype: list[oci.devops.models.TriggerAction]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """
        Sets the actions of this TriggerCreateResult.
        The list of actions that are to be performed for this trigger.


        :param actions: The actions of this TriggerCreateResult.
        :type: list[oci.devops.models.TriggerAction]
        """
        self._actions = actions

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this TriggerCreateResult.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See `Resource Tags`__. Example: `{\"bar-key\": \"value\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this TriggerCreateResult.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this TriggerCreateResult.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See `Resource Tags`__. Example: `{\"bar-key\": \"value\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this TriggerCreateResult.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this TriggerCreateResult.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. See `Resource Tags`__. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this TriggerCreateResult.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this TriggerCreateResult.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. See `Resource Tags`__. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this TriggerCreateResult.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this TriggerCreateResult.
        Usage of system tag keys. These predefined keys are scoped to namespaces. See `Resource Tags`__. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The system_tags of this TriggerCreateResult.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this TriggerCreateResult.
        Usage of system tag keys. These predefined keys are scoped to namespaces. See `Resource Tags`__. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param system_tags: The system_tags of this TriggerCreateResult.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
