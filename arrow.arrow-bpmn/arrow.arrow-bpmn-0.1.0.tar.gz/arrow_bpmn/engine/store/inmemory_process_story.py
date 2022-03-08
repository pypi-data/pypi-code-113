from typing import Dict

from arrow_bpmn.__spi__ import State, NodeRef
from arrow_bpmn.engine.registry.abstract_event_registry import ProcessRef
from arrow_bpmn.engine.store.abstract_process_store import ProcessStore
from arrow_bpmn.model.process import Process


class InMemoryProcessStore(ProcessStore):
    process_cache: Dict[str, Process] = {}
    state_cache: Dict[str, State] = {}

    def write_process(self, group: str, process: Process):
        self.process_cache[group + ":" + process.id] = process

    def read_process(self, ref: ProcessRef):
        return self.process_cache[ref.group + ":" + ref.process_id]

    def write_state(self, state: State):
        self.state_cache[str(state.reference)] = state

    def read_state(self, ref: NodeRef) -> State:
        return self.state_cache[str(ref)]
