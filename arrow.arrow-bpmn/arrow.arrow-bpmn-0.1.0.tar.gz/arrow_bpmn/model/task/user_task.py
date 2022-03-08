from typing import Tuple

from arrow_bpmn.__spi__ import BpmnNode
from arrow_bpmn.__spi__ import CompleteAction
from arrow_bpmn.__spi__.action import ContinueAction, Actions, QueueAction
from arrow_bpmn.__spi__.execution import Environment
from arrow_bpmn.__spi__.execution import State
from arrow_bpmn.engine.registry.abstract_event_registry import UserEvent
from arrow_bpmn.parser.xml.xml_element import XMLElement


class UserTask(BpmnNode):
    """
    A User Task is used to model work that needs to be done by a human actor. When the process execution arrives at such
    a User Task, a new task is created in the task list of the user(s) or group(s) assigned to that task.
    """

    def __init__(self, element: XMLElement):
        super().__init__(element)

    # noinspection PyBroadException
    def execute(self, state: State, environment: Environment) -> Tuple[State, Actions]:
        if state.is_reentry:
            actions = [ContinueAction(node) for node in environment.get_outgoing_nodes(self.id)]
            return state, [CompleteAction(self.id)] + actions

        event = UserEvent(environment.group, environment.process_id, self.id, {})
        return state, [QueueAction(self.id, event=event)]

    def __repr__(self):
        return f"UserTask({self.id})"
