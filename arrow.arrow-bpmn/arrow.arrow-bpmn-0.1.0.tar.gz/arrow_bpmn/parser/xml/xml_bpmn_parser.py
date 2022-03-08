import xml.etree.ElementTree as XmlTree
from pathlib import Path
from typing import List, Tuple

from arrow_bpmn.model.event.boundary.error_boundary_event import ErrorBoundaryEvent
from arrow_bpmn.model.event.endevent.error_end_event import ErrorEndEvent
from arrow_bpmn.model.event.endevent.message_end_event import MessageEndEvent
from arrow_bpmn.model.event.endevent.none_end_event import NoneEndEvent
from arrow_bpmn.model.event.endevent.signal_end_event import SignalEndEvent
from arrow_bpmn.model.event.intermediate.message_intermediate_catch_event import MessageIntermediateCatchEvent
from arrow_bpmn.model.event.intermediate.message_intermediate_throw_event import MessageIntermediateThrowEvent
from arrow_bpmn.model.event.intermediate.signal_intermediate_catch_event import SignalIntermediateCatchEvent
from arrow_bpmn.model.event.intermediate.signal_intermediate_throw_event import SignalIntermediateThrowEvent
from arrow_bpmn.model.event.startevent.message_start_event import MessageStartEvent
from arrow_bpmn.model.event.startevent.none_start_event import NoneStartEvent
from arrow_bpmn.model.event.startevent.signal_start_event import SignalStartEvent
from arrow_bpmn.model.gateway.exclusive_gateway import ExclusiveGateway
from arrow_bpmn.model.process import Process, EventDict
from arrow_bpmn.model.sequence.sequence_flow import SequenceFlow
from arrow_bpmn.model.task.call_activity import CallActivity, VariableMapping, ExpressionMapping
from arrow_bpmn.model.task.manual_task import ManualTask
from arrow_bpmn.model.task.receive_task import ReceiveTask
from arrow_bpmn.model.task.script_task import ScriptTask
from arrow_bpmn.model.task.send_task import SendTask
from arrow_bpmn.model.task.service_task import ServiceTask
from arrow_bpmn.model.task.user_task import UserTask
from arrow_bpmn.parser.abstract_bpmn_parser import BpmnParser
from arrow_bpmn.parser.xml.xml_element import XMLElement

DiagramSource = Path


class XmlBpmnParser(BpmnParser):

    def parse(self, source: DiagramSource) -> Tuple[str, List[Process]]:
        root = XMLElement(XmlTree.parse(source).getroot())

        messages = {x.get_attribute("id"): x.get_attribute("name") for x in root.get_tags("bpmn:message")}
        signals = {x.get_attribute("id"): x.get_attribute("name") for x in root.get_tags("bpmn:signal")}
        errors = {x.get_attribute("id"): x.get_attribute("errorCode") for x in root.get_tags("bpmn:error")}

        events = EventDict({"message": messages, "signal": signals, "error": errors})
        return "customGroup", [self._parse_process(x, events) for x in root.get_tags("./bpmn:process")]

    def _parse_process(self, process: XMLElement, events: EventDict) -> Process:
        sequence_flows = [SequenceFlow(x, self.script_factory) for x in process.get_tags("bpmn:sequenceFlow")]
        tasks = [ScriptTask(x, self.script_factory) for x in process.get_tags("bpmn:scriptTask")]
        tasks += [UserTask(x) for x in process.get_tags("bpmn:userTask")]
        tasks += [ManualTask(x) for x in process.get_tags("bpmn:manualTask")]
        tasks += [ReceiveTask(x) for x in process.get_tags("bpmn:receiveTask")]
        tasks += [SendTask(x) for x in process.get_tags("bpmn:sendTask")]
        tasks += [ServiceTask(x, self.service_factory) for x in process.get_tags("bpmn:serviceTask")]
        tasks += [self._parse_call_activity(x) for x in process.get_tags("bpmn:callActivity")]
        tasks += [self._parse_custom_task(x) for x in process.get_tags("bpmn:task")]
        start_events = [self._parse_start_event(x, events) for x in process.get_tags("bpmn:startEvent")]
        end_events = [self._parse_end_event(x, events) for x in process.get_tags("bpmn:endEvent")]
        boundary_events = [self._parse_boundary_event(x, events) for x in process.get_tags("bpmn:boundaryEvent")]
        gateways = [ExclusiveGateway(x) for x in process.get_tags("bpmn:exclusiveGateway")]

        ie1 = [self._parse_intermediate_catch_event(x, events) for x in process.get_tags("bpmn:intermediateCatchEvent")]
        ie2 = [self._parse_intermediate_throw_event(x, events) for x in process.get_tags("bpmn:intermediateThrowEvent")]
        intermediate_events = ie1 + ie2

        return Process(process.get_attributes(), sequence_flows, tasks, start_events, end_events, boundary_events,
                       intermediate_events, gateways, events)

    def _parse_custom_task(self, task: XMLElement, events: EventDict):
        raise ValueError("no task event specification found")

    def _parse_start_event(self, start_event: XMLElement, events: EventDict):
        event_definition = start_event.get_tag("bpmn:messageEventDefinition")
        if event_definition is not None:
            message_ref = event_definition.get_attribute("messageRef")
            return MessageStartEvent(start_event.get_attributes(), events.messages[message_ref])
        event_definition = start_event.get_tag("bpmn:signalEventDefinition")
        if event_definition is not None:
            signal_ref = event_definition.get_attribute("signalRef")
            return SignalStartEvent(start_event.get_attributes(), events.signals[signal_ref])
        return NoneStartEvent(start_event.get_attributes())

    def _parse_end_event(self, end_event: XMLElement, events: EventDict):
        # message event
        event_definition = end_event.get_tag("bpmn:messageEventDefinition")
        if event_definition is not None:
            message_ref = event_definition.get_attribute("messageRef")
            return MessageEndEvent(end_event.get_attributes(), events.messages[message_ref])

        # signal event
        event_definition = end_event.get_tag("bpmn:signalEventDefinition")
        if event_definition is not None:
            signal_ref = event_definition.get_attribute("signalRef")
            return SignalEndEvent(end_event.get_attributes(), events.signals[signal_ref])

        # error event
        event_definition = end_event.get_tag("bpmn:errorEventDefinition")
        if event_definition is not None:
            error_ref = event_definition.get_attribute("errorRef")
            return ErrorEndEvent(end_event.get_attributes(), events.errors[error_ref])

        return NoneEndEvent(end_event.get_attributes())

    def _parse_boundary_event(self, event: XMLElement, events: EventDict):
        # error event
        event_definition = event.get_tag("bpmn:errorEventDefinition")
        if event_definition is not None:
            error_ref = event_definition.get_attribute("errorRef")
            return ErrorBoundaryEvent(event.get_attributes(), events.errors[error_ref])

        raise ValueError(f"cannot parse boundary event {event}")

    def _parse_intermediate_catch_event(self, event: XMLElement, events: EventDict):
        # message event
        event_definition = event.get_tag("bpmn:messageEventDefinition")
        if event_definition is not None:
            message_ref = event_definition.get_attribute("messageRef")
            return MessageIntermediateCatchEvent(event.get_attributes(), events.messages[message_ref])

        # signal event
        event_definition = event.get_tag("bpmn:signalEventDefinition")
        if event_definition is not None:
            signal_ref = event_definition.get_attribute("signalRef")
            return SignalIntermediateCatchEvent(event.get_attributes(), events.signals[signal_ref])

        raise ValueError(f"cannot parse boundary event {event}")

    def _parse_intermediate_throw_event(self, event: XMLElement, events: EventDict):
        # message event
        event_definition = event.get_tag("bpmn:messageEventDefinition")
        if event_definition is not None:
            message_ref = event_definition.get_attribute("messageRef")
            return MessageIntermediateThrowEvent(event.get_attributes(), events.messages[message_ref])

        # signal event
        event_definition = event.get_tag("bpmn:signalEventDefinition")
        if event_definition is not None:
            signal_ref = event_definition.get_attribute("signalRef")
            return SignalIntermediateThrowEvent(event.get_attributes(), events.signals[signal_ref])

        raise ValueError(f"cannot parse boundary event {event}")

    def _parse_call_activity(self, element: XMLElement):
        def parse_mappings(e: XMLElement):
            mappings = []
            mappings.extend([VariableMapping(x["source"], x["target"]) for x in e.get_tags("xy:variable")])
            mappings.extend([ExpressionMapping(x["source"], x["target"]) for x in e.get_tags("xy:expression")])
            return mappings

        incoming_state = []
        outgoing_state = []

        extensions = element.get_tags("bpmn:extensionElements")
        for extension in extensions:
            for state_mapping in extension.get_tags("xy:incomingState"):
                incoming_state.extend(parse_mappings(state_mapping))
            for state_mapping in extension.get_tags("xy:outgoingState"):
                outgoing_state.extend(parse_mappings(state_mapping))

        return CallActivity(element.get_attributes(), incoming_state, outgoing_state)
