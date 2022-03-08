# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RoutingRule(object):
    """
    A routing rule examines an incoming request, routing matching requests to the specified backend set.
    Routing rules apply only to HTTP and HTTPS requests. They have no effect on TCP requests.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new RoutingRule object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this RoutingRule.
        :type name: str

        :param condition:
            The value to assign to the condition property of this RoutingRule.
        :type condition: str

        :param actions:
            The value to assign to the actions property of this RoutingRule.
        :type actions: list[oci.load_balancer.models.Action]

        """
        self.swagger_types = {
            'name': 'str',
            'condition': 'str',
            'actions': 'list[Action]'
        }

        self.attribute_map = {
            'name': 'name',
            'condition': 'condition',
            'actions': 'actions'
        }

        self._name = None
        self._condition = None
        self._actions = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this RoutingRule.
        A unique name for the routing policy rule. Avoid entering confidential information.


        :return: The name of this RoutingRule.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this RoutingRule.
        A unique name for the routing policy rule. Avoid entering confidential information.


        :param name: The name of this RoutingRule.
        :type: str
        """
        self._name = name

    @property
    def condition(self):
        """
        **[Required]** Gets the condition of this RoutingRule.
        A routing rule to evaluate defined conditions against the incoming HTTP request and perform an action.


        :return: The condition of this RoutingRule.
        :rtype: str
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        """
        Sets the condition of this RoutingRule.
        A routing rule to evaluate defined conditions against the incoming HTTP request and perform an action.


        :param condition: The condition of this RoutingRule.
        :type: str
        """
        self._condition = condition

    @property
    def actions(self):
        """
        **[Required]** Gets the actions of this RoutingRule.
        A list of actions to be applied when conditions of the routing rule are met.


        :return: The actions of this RoutingRule.
        :rtype: list[oci.load_balancer.models.Action]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """
        Sets the actions of this RoutingRule.
        A list of actions to be applied when conditions of the routing rule are met.


        :param actions: The actions of this RoutingRule.
        :type: list[oci.load_balancer.models.Action]
        """
        self._actions = actions

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
