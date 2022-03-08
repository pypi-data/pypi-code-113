from arrow_bpmn.__spi__ import State, NodeRef
from arrow_bpmn.engine.abstract_engine import ProcessRef
from arrow_bpmn.model.process import Process


class ProcessStore:

    def write_process(self, group: str, process: Process):
        pass

    def read_process(self, ref: ProcessRef):
        pass

    def write_state(self, state: State):
        pass

    def read_state(self, ref: NodeRef) -> State:
        pass
