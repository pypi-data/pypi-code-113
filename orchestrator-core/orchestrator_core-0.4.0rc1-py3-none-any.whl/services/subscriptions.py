# Copyright 2019-2020 SURF.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Module that provides service functions on subscriptions."""

from collections import defaultdict
from datetime import datetime
from typing import Any, Dict, List, Optional, Sequence, Tuple, TypeVar, Union, overload
from uuid import UUID

import more_itertools
import structlog
from deprecated import deprecated
from sqlalchemy import Text, cast, not_
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Query, aliased, joinedload
from sqlalchemy.sql.expression import or_

from orchestrator.db import (
    ProductTable,
    ResourceTypeTable,
    SubscriptionInstanceTable,
    SubscriptionInstanceValueTable,
    SubscriptionTable,
    db,
)
from orchestrator.db.models import SubscriptionInstanceRelationTable
from orchestrator.targets import Target
from orchestrator.types import UUIDstr
from orchestrator.utils.datetime import nowtz

logger = structlog.get_logger(__name__)


T = TypeVar("T", bound=SubscriptionTable)


@overload
def get_subscription(subscription_id: Union[UUID, UUIDstr], for_update: bool = False) -> SubscriptionTable:
    ...


@overload
def get_subscription(
    subscription_id: Union[UUID, UUIDstr], for_update: bool = False, model: T = SubscriptionTable
) -> T:
    ...


def get_subscription(
    subscription_id: Union[UUID, UUIDstr], for_update: bool = False, model: T = SubscriptionTable
) -> T:
    """Get the subscription.

    Args:
        subscription_id: The subscription_id
        for_update: specific whether we intend to update the subscription
        model: SubscriptionModelType

    Returns: A subscription object

    Raises: ValueError: if the requested Subscription does not exist in de database.

    """
    query = model.query
    if for_update:
        query = query.with_for_update()

    try:
        subscription = query.get(subscription_id)
    except SQLAlchemyError as e:
        raise ValueError("Invalid subscription id") from e

    if subscription:
        return subscription
    else:
        raise ValueError(f"Subscription with {subscription_id} does not exist in the database")


def update_subscription_status(subscription_id: UUIDstr, status: str) -> SubscriptionTable:
    """Update the subscription status.

    Args:
        subscription_id: Id of the subscription to update.
        status: Status to transition to.

    Returns: Subscription

    """
    subscription = get_subscription(subscription_id, for_update=True)
    subscription.status = status
    return subscription


def update_subscription_description(subscription_id: UUIDstr, description: str) -> SubscriptionTable:
    """Update a subscriptions description.

    Args:
        subscription_id: subscription id of the subscription to update
        description: new subscription description

    Returns: Subscription

    """
    subscription = get_subscription(subscription_id, for_update=True)
    subscription.description = description
    return subscription


def activate_subscription(subscription_id: UUIDstr) -> SubscriptionTable:
    """Activate subscription by subscription id.

    Args:
        subscription_id: subscription id of the subscription

    Returns: Subscription object

    """
    subscription = get_subscription(subscription_id, for_update=True)
    subscription.status = "active"
    subscription.start_date = nowtz()
    subscription.insync = True
    return subscription


def provision_subscription(subscription_id: UUIDstr) -> SubscriptionTable:
    """Provision subscription by subscription id.

    Args:
        subscription_id: Subscription id of the subscription

    Returns: Updated subscription object

    """
    subscription = get_subscription(subscription_id, for_update=True)
    subscription.status = "provisioning"
    subscription.insync = True
    return subscription


def migrate_subscription(subscription_id: UUIDstr) -> SubscriptionTable:
    """Migrate subscription by subscription id.

    Args:
        subscription_id: Subscription id of the subscription

    Returns: Updated subscription object

    """
    subscription = get_subscription(subscription_id, for_update=True)
    subscription.status = "migrating"
    subscription.insync = False
    return subscription


def unsync(subscription_id: UUIDstr, checked: bool = True) -> SubscriptionTable:
    """Unsync subscription by subscription id.

    Args:
        subscription_id: Subscription id of the subscription

    Returns: Updated subscription object

    """
    subscription = get_subscription(subscription_id, for_update=True)
    if checked and not subscription.insync:
        raise ValueError("Subscription is already out of sync, cannot continue!")
    subscription.insync = False
    return subscription


def resync(subscription_id: UUIDstr) -> SubscriptionTable:
    """
    Resync subscription by subscription id.

    Args:
        subscription_id: Subscription id of the subscription

    Returns: Updated subscription object

    """
    subscription = get_subscription(subscription_id, for_update=True)
    subscription.insync = True
    return subscription


def set_status_provisioning_subscription(subscription_id: UUIDstr) -> SubscriptionTable:
    return update_subscription_status(subscription_id, "provisioning")


def terminate_subscription(subscription_id: UUIDstr) -> SubscriptionTable:
    return update_subscription(subscription_id, status="terminated", end_date=nowtz())


def create_subscription(
    organisation: UUIDstr, product: ProductTable, subscription_name: str, subscription_id: UUIDstr
) -> UUID:
    subscription = SubscriptionTable(
        subscription_id=subscription_id,
        product_id=product.product_id,
        customer_id=organisation,
        description=subscription_name,
        start_date=None,
        end_date=None,
        insync=False,
        status="initial",
    )
    db.session.add(subscription)

    return subscription.subscription_id


def update_subscription(subscription_id: str, **attrs: Union[Dict, UUIDstr, str, datetime]) -> SubscriptionTable:
    """
    Update the subscription.

    Args:
        subscription_id: SubscriptionTable id of the subscription
        attrs: Attributes that will be set

    Returns: Subscription

    """

    subscription = get_subscription(subscription_id, for_update=True)

    for (key, value) in attrs.items():
        setattr(subscription, key, value)

    return subscription


def retrieve_node_subscriptions_by_name(node_name: str) -> List[SubscriptionTable]:
    node_subscriptions = (
        SubscriptionTable.query.join(
            ProductTable, SubscriptionInstanceTable, SubscriptionInstanceValueTable, ResourceTypeTable
        )
        .filter(SubscriptionInstanceValueTable.value == node_name)
        .filter(ResourceTypeTable.resource_type == "nso_device_id")
        .filter(SubscriptionTable.status.in_(["active", "provisioning"]))
        .all()
    )
    return node_subscriptions


def retrieve_subscription_by_subscription_instance_value(
    resource_type: str, value: str, sub_status: Tuple = ("provisioning", "active")
) -> Optional[SubscriptionTable]:
    """
    Retrieve a Subscriptions by resource_type and value.

    Args:
        resource_type: name of the resource type
        value: value of the resource type
        sub_status: status of the subscriptions

    Returns: Subscription or None

    """
    subscription = (
        SubscriptionTable.query.join(SubscriptionInstanceTable, SubscriptionInstanceValueTable, ResourceTypeTable)
        .filter(SubscriptionInstanceValueTable.value == value)
        .filter(ResourceTypeTable.resource_type == resource_type)
        .filter(SubscriptionTable.status.in_(sub_status))
        .one_or_none()
    )
    return subscription


def find_values_for_resource_types(
    subscription_id: Union[UUID, UUIDstr], resource_types: Sequence[str], strict: bool = True
) -> Dict[str, List[str]]:
    """Find values for resource types by subscription ID.

    This function issues a single SQL query to find one or more resource types for a given subscription. As
    multiple values per resource type are possible (think of a BGP subscription with multiple SAPs, with each SAP
    sharing the same resource types) values are always returned as a list, even when there is only a single value.

    In case of shared resource types (hence multiple values), the order of the values matches across resource types:
    Meaning: in case of the above example with multiple, say two, SAPs, should we have requested the resource types::

        ('customer_ipv4_mtu', 'customer_ipv6_mtu', 'port_subscription_id'),

    we would get back::

        {
            'customer_ipv4_mtu': ['1500', '9000'],
            'customer_ipv6_mtu': ['9000', '9000'],
            'port_subscription_id': ['654a1e7f-9afb-43b7-ba8f-cdf9d48494aa', '2f86be06-a5b7-40ee-a71b-137d6b48a37e']
        }

    The first element of each list belong to the same SAP, likewise the second element of each list belongs to the
    same SAP. This allows you to implicitly correlate values.

    Args:
        subscription_id: The id of the subscription.
        resource_types: A sequence of resource type names.
        strict:
            True: raise `ValueError` if one or more requested resource types were not found,
            False: ignore resource types that weren't found.

    Returns:
        A dictionary of resource type names to lists of values.

    Raises:
        ValueError: if strict == True and one or more resource types were requested but not found.

    """
    # the `order_by` on `subscription_instance_id` is there to guarantee the matched ordering across resource_types
    # (see also docstring)
    query_result = (
        SubscriptionInstanceValueTable.query.join(ResourceTypeTable, SubscriptionInstanceTable)
        .filter(
            SubscriptionInstanceTable.subscription_id == subscription_id,
            ResourceTypeTable.resource_type.in_(resource_types),
        )
        .order_by(SubscriptionInstanceTable.subscription_instance_id)
        .values(ResourceTypeTable.resource_type, SubscriptionInstanceValueTable.value)
    )
    resource_type_values = tuple(query_result)

    rt2v: Dict[str, List[str]] = defaultdict(list)
    for resource_type, value in resource_type_values:
        rt2v[resource_type].append(value)
    if strict:
        missing = set(resource_types) - set(rt2v.keys())
        if missing:
            raise ValueError(f"Could not find requested resource types: '{','.join(missing)}'!")
    return rt2v


def query_in_use_by_subscriptions(subscription_id: UUID) -> Query:
    """
    Return a query with all subscriptions -in_use_by- that use this subscription with resource_type or direct relation.

    The query can be used to add extra filters when/where needed.
    """
    # Find relations through resource types
    resource_type_relations = (
        SubscriptionTable.query.join(SubscriptionInstanceTable)
        .options(joinedload("customer_descriptions"))
        .join(SubscriptionInstanceValueTable)
        .join(ResourceTypeTable)
        .filter(ResourceTypeTable.resource_type.in_(RELATION_RESOURCE_TYPES))
        .filter(SubscriptionInstanceValueTable.value == str(subscription_id))
        .with_entities(SubscriptionTable.subscription_id)
    )

    # Find relations through instance hierarchy
    in_use_by_instances = aliased(SubscriptionInstanceTable)
    dependent_on_instances = aliased(SubscriptionInstanceTable)
    relation_relations = (
        SubscriptionTable.query.join(in_use_by_instances.subscription)
        .join(in_use_by_instances.dependent_on_block_relations)
        .join(dependent_on_instances, SubscriptionInstanceRelationTable.dependent_on)
        .filter(dependent_on_instances.subscription_id == subscription_id)
        .filter(in_use_by_instances.subscription_id != subscription_id)
        .with_entities(SubscriptionTable.subscription_id)
    )

    return SubscriptionTable.query.filter(
        or_(
            SubscriptionTable.subscription_id.in_(resource_type_relations.scalar_subquery()),
            SubscriptionTable.subscription_id.in_(relation_relations.scalar_subquery()),
        )
    )


@deprecated("Has been renamed to query_in_use_by_subscriptions")
def query_parent_subscriptions(subscription_id: UUID) -> Query:
    return query_in_use_by_subscriptions(subscription_id)


def query_dependent_on_subscriptions(subscription_id: UUID) -> Query:
    """
    Return a query with all subscriptions -dependent_on- that this subscription is dependent on with resource_type or direct relation.

    The query can be used to add extra filters when/where needed.
    """
    # Find relations through resource types
    resource_type_relations = (
        SubscriptionInstanceTable.query.join(SubscriptionInstanceValueTable)
        .join(ResourceTypeTable)
        .filter(ResourceTypeTable.resource_type.in_(RELATION_RESOURCE_TYPES))
        .filter(SubscriptionInstanceTable.subscription_id == subscription_id)
        .join(SubscriptionTable, SubscriptionInstanceValueTable.value == cast(SubscriptionTable.subscription_id, Text))
        .with_entities(SubscriptionTable.subscription_id)
    )

    # Find relations through instance hierarchy
    in_use_by_instances = aliased(SubscriptionInstanceTable)
    dependent_on_instances = aliased(SubscriptionInstanceTable)
    relation_relations = (
        SubscriptionTable.query.join(dependent_on_instances.subscription)
        .join(dependent_on_instances.in_use_by_block_relations)
        .join(in_use_by_instances, SubscriptionInstanceRelationTable.in_use_by)
        .filter(in_use_by_instances.subscription_id == subscription_id)
        .filter(dependent_on_instances.subscription_id != subscription_id)
        .with_entities(SubscriptionTable.subscription_id)
    )

    return SubscriptionTable.query.filter(
        or_(
            SubscriptionTable.subscription_id.in_(resource_type_relations.scalar_subquery()),
            SubscriptionTable.subscription_id.in_(relation_relations.scalar_subquery()),
        )
    )


@deprecated("Has been renamed to query_dependent_on_subscriptions")
def query_child_subscriptions(subscription_id: UUID) -> Query:
    return query_dependent_on_subscriptions(subscription_id)


def _terminated_filter(query: Query) -> List[UUID]:
    return list(
        more_itertools.flatten(
            query.filter(SubscriptionTable.status != "terminated").with_entities(SubscriptionTable.subscription_id)
        )
    )


def _in_sync_filter(query: Query) -> List[UUID]:
    return list(
        more_itertools.flatten(
            query.filter(not_(SubscriptionTable.insync)).with_entities(SubscriptionTable.subscription_id)
        )
    )


RELATION_RESOURCE_TYPES: List[str] = []


def status_relations(subscription: SubscriptionTable) -> Dict[str, List[UUID]]:
    """Return info about locked subscription dependencies.

    This call will be used by the client to determine if it's safe to
    start a modify or terminate workflow. There are 4 cases:

    1) The subscription is a IP, LightPath or ELAN: the dependent_on subscriptions are checked for not 'insync' instances.
    2) The subscription is a ServicePort: in_use_by subscriptions are checked for not 'insync' instances and for in_use_by
       services that are not terminated.
    3) The subscription is a Node: Related Core link subscriptions are checked that there are no active instances
       This is only used for the terminate workflow and ignored for modify
    4) IP_prefix cannot be terminated when in use

    """
    in_use_by_query = query_in_use_by_subscriptions(subscription.subscription_id)

    unterminated_dependent_subscriptions = _terminated_filter(in_use_by_query)
    locked_in_use_by_block_relations = _in_sync_filter(in_use_by_query)

    dependent_on_query = query_dependent_on_subscriptions(subscription.subscription_id)

    locked_dependent_on_block_relations = _in_sync_filter(dependent_on_query)

    result = {
        "locked_relations": locked_in_use_by_block_relations + locked_dependent_on_block_relations,
        # unterminated_parents deprecated since "0.4.0", renamed to unterminated_dependent_subscriptions
        "unterminated_parents": unterminated_dependent_subscriptions,
        "unterminated_dependent_subscriptions": unterminated_dependent_subscriptions,
    }

    logger.debug(
        "Returning status info for related subscriptions",
        result=result,
        subscription_id=str(subscription.subscription_id),
    )
    return result


def get_relations(subscription_id: UUIDstr) -> Dict[str, List[UUID]]:
    subscription_table = SubscriptionTable.query.options(joinedload("product"), joinedload("product.workflows")).get(
        subscription_id
    )
    relations = status_relations(subscription_table)
    return relations


TARGET_DEFAULT_USABLE_MAP: Dict[Target, List[str]] = {
    Target.CREATE: [],
    Target.MODIFY: ["active"],
    Target.TERMINATE: ["active", "provisioning"],
    Target.SYSTEM: ["active"],
}

WF_USABLE_MAP: Dict[str, List[str]] = {}

# WF_BLOCKED_BY_PARENTS deprecated since "0.4.0", renamed to WF_BLOCKED_BY_DEPENDENT_SUBSCRIPTIONS
WF_BLOCKED_BY_PARENTS: Dict[str, bool] = {}
WF_BLOCKED_BY_DEPENDENT_SUBSCRIPTIONS: Dict[str, bool] = {}

WF_USABLE_WHILE_OUT_OF_SYNC: List[str] = ["modify_note"]


def subscription_workflows(subscription: SubscriptionTable) -> Dict[str, Any]:
    """
    Return a dict containing all the workflows a user can start for this subscription.

    Args:
        subscription: an SqlAlchemy instance of a `db.SubscriptionTable`

    Returns:
        A dictionary with the following structure (reason and its related keys are only present when workflows are blocked):

        >>> {  # doctest:+SKIP
        ...     "reason": "Optional global reason like subscription is in use"
        ...     "create": [{"name": "workflow.name", "description": "workflow.description", "reason": "Optional reason why this specific workflow is blocked"}],
        ...     "modify": [],
        ...     "terminate": [],
        ...     "system": [],
        ... }

    """
    default_json: Dict[str, Any] = {}

    if not subscription.insync:
        default_json["reason"] = "subscription.not_in_sync"
    else:
        data = status_relations(subscription)

        if data["locked_relations"]:
            default_json["reason"] = "subscription.relations_not_in_sync"
            default_json["locked_relations"] = data["locked_relations"]

    workflows: Dict[str, Any] = {
        "create": [],
        "modify": [],
        "terminate": [],
        "system": [],
    }

    for workflow in subscription.product.workflows:
        if workflow.name in WF_USABLE_WHILE_OUT_OF_SYNC or workflow.target == Target.SYSTEM:
            # validations and modify note are also possible with: not in sync or locked relations
            workflow_json = {"name": workflow.name, "description": workflow.description}
        else:
            workflow_json = {"name": workflow.name, "description": workflow.description, **default_json}

        # Simple reasons like "not in sync" and "locked_relations" are handled now. Handle special lifecycle cases:
        if "reason" not in workflow_json:

            default = TARGET_DEFAULT_USABLE_MAP[workflow.target]
            usable_when = WF_USABLE_MAP.get(workflow.name, default)

            if subscription.status not in usable_when:
                workflow_json["reason"] = "subscription.no_modify_invalid_status"
                workflow_json["usable_when"] = usable_when
                workflow_json["status"] = subscription.status
                workflow_json["action"] = "terminated" if workflow.target == Target.TERMINATE else "modified"

            # Check if this workflow is blocked because there are unterminated relations
            blocked_by_dependent_subscriptions = WF_BLOCKED_BY_DEPENDENT_SUBSCRIPTIONS.get(
                workflow.name, workflow.target == Target.TERMINATE
            )

            # WF_BLOCKED_BY_PARENTS deprecated since "0.4.0", renamed to WF_BLOCKED_BY_DEPENDENT_SUBSCRIPTIONS
            if not blocked_by_dependent_subscriptions:
                blocked_by_dependent_subscriptions = WF_BLOCKED_BY_PARENTS.get(
                    workflow.name, workflow.target == Target.TERMINATE
                )
            if blocked_by_dependent_subscriptions and data["unterminated_dependent_subscriptions"]:
                workflow_json["reason"] = "subscription.no_modify_subscription_in_use_by_others"
                # unterminated_parents deprecated since "0.4.0", renamed to unterminated_dependent_subscriptions
                workflow_json["unterminated_parents"] = data["unterminated_parents"]
                workflow_json["unterminated_dependent_subscriptions"] = data["unterminated_dependent_subscriptions"]
                workflow_json["action"] = "terminated" if workflow.target == Target.TERMINATE else "modified"

        workflows[workflow.target.lower()].append(workflow_json)

    return {**workflows, **default_json}
