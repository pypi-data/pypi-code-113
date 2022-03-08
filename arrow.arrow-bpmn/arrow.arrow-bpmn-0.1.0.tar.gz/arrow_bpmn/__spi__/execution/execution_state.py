from dataclasses import dataclass
from typing import Optional

from arrow_bpmn.__spi__.registry import NodeRef


@dataclass
class State:
    """
    This class holds all relevant information about a bpmn process run.
    The variables are immutable.
    """
    properties: dict
    reference: NodeRef
    is_reentry: bool = False
    parent_reference: Optional[NodeRef] = None

    def with_is_reentry(self, is_reentry: bool):
        return State(self.properties, self.reference, is_reentry, self.parent_reference)

    def with_parent_reference(self, parent_reference: Optional[NodeRef]):
        return State(self.properties, self.reference, self.is_reentry, parent_reference)

    def with_reference(self, reference: NodeRef):
        return State(self.properties, reference, self.is_reentry, self.parent_reference)

    def __setitem__(self, key, value):
        self.properties[key] = value

    def __getitem__(self, item):
        return self.properties[item]
