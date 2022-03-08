from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional, List

from arrow_bpmn.__spi__.registry.event import Event
# TODO: remove_event_subscriptions
from arrow_bpmn.__spi__.registry.node_ref import NodeRef


class EventRegistry(ABC):

    @abstractmethod
    def create_subscription(self, event: Event, node_ref: NodeRef):
        pass

    @abstractmethod
    def delete_subscription(self, event: Optional[Event], node_ref: NodeRef):
        pass

    @abstractmethod
    def get_subscriptions(self, event: Event, consume: bool = True) -> List[NodeRef]:
        pass


@dataclass
class ProcessRef:
    group: str
    process_id: str


class EventRegistryAware(ABC):

    def with_event_registry(self, process_ref: ProcessRef, event_registry: EventRegistry):
        pass


@dataclass
class NoneEvent(Event):
    process_id: str

    def __repr__(self):
        return f"{self.group}:{self.process_id}"


@dataclass
class MessageEvent(Event):
    name: str

    def __repr__(self):
        return self.group + ":" + self.name


@dataclass
class TimerEvent(Event):
    pass


@dataclass
class TimerDateEvent(TimerEvent):
    timer_date: str


@dataclass
class TimerCycleEvent(TimerEvent):
    timer_cycle: str


@dataclass
class TimerDurationEvent(TimerEvent):
    timer_duration: str


@dataclass
class SignalEvent(Event):
    name: str

    def __repr__(self):
        return self.group + ":" + self.name


@dataclass
class ErrorEvent(Event):
    error_ref: str


@dataclass
class UserEvent(Event):
    process_id: str
    node_id: str
    attributes: dict
    
    def __repr__(self):
        return f"{self.group}:{self.process_id}:{self.node_id}"

@dataclass
class ManualEvent(Event):
    process_id: str
    node_id: str
    attributes: dict

    def __repr__(self):
        return f"{self.group}:{self.process_id}:{self.node_id}"


@dataclass
class ConditionalEvent(Event):
    condition: str
    context: Optional[dict]
