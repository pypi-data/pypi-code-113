from abc import ABC
from dataclasses import dataclass


@dataclass
class Event(ABC):
    group: str
