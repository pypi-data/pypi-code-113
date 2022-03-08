from dataclasses import dataclass


@dataclass
class ProcessRef:
    group: str
    process_id: str

    def __repr__(self):
        return f"{self.group}:{self.process_id}"
