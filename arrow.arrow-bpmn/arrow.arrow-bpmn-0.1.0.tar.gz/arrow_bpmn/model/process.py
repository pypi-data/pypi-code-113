from collections import UserDict
from typing import List

from arrow_bpmn.__spi__ import BpmnEdge
from arrow_bpmn.__spi__ import BpmnNode
from arrow_bpmn.engine.registry.abstract_event_registry import EventRegistryAware, ProcessRef, EventRegistry


class EventDict(UserDict):
    @property
    def messages(self):
        return self["message"]

    @property
    def signals(self):
        return self["signal"]

    @property
    def errors(self):
        return self["error"]


class Process(EventRegistryAware):

    def __init__(self,
                 attributes: dict,
                 sequence_flows: List[BpmnEdge],
                 tasks: List[BpmnNode],
                 start_events: List[BpmnNode],
                 end_events: List[BpmnNode],
                 boundary_events: List[BpmnNode],
                 intermediate_events: List[BpmnNode],
                 gateways: List[BpmnNode],
                 events: EventDict):
        self.__dict__ = attributes
        self.sequence_flows = sequence_flows
        self.tasks = tasks
        self.start_events = start_events
        self.end_events = end_events
        self.boundary_events = boundary_events
        self.intermediate_events = intermediate_events
        self.gateways = gateways
        self.events = events

    @property
    def id(self):
        return self.__dict__["id"]

    def with_event_registry(self, process_ref: ProcessRef, event_registry: EventRegistry):
        process_ref = ProcessRef(process_ref.group, self.id)

        for start_event in self.start_events:
            if isinstance(start_event, EventRegistryAware):
                start_event.with_event_registry(process_ref, event_registry)
