from abc import ABC, abstractmethod
from typing import List

from arrow_bpmn.__spi__.execution import State
from arrow_bpmn.parser.xml.xml_element import XMLElement


class BpmnEdge(ABC):

    def __init__(self, element: XMLElement):
        self.__dict__ = element.get_attributes()

    @property
    def source_ref(self) -> str:
        """
        Returns the id of the bpmn source element.
        :return: str
        """
        return self.__dict__["sourceRef"]

    @property
    def target_ref(self):
        """
        Returns the id of the bpmn target element.
        :return: str
        """
        return self.__dict__["targetRef"]

    @property
    def name(self) -> str:
        """
        Returns the name of the edge.
        :return: str
        """
        return self.__dict__["name"]

    @property
    def id(self) -> str:
        """
        Returns the id of the edge. Creates a synthetic id based on the source_ref and target_ref if no explicit
        id attribute is present.
        :return: str
        """
        if "id" not in self.__dict__:
            return "flow_" + str(hash(self.source_ref + ":" + self.target_ref))

        return self.__dict__["id"]

    @abstractmethod
    def evaluate(self, state: State) -> bool:
        pass


class IncomingEdgeAware(ABC):

    @abstractmethod
    def get_incoming_edges(self) -> List[str]:
        pass


class OutgoingEdgeAware(ABC):

    @abstractmethod
    def get_outgoing_edges(self) -> List[str]:
        pass
