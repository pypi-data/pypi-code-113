from dataclasses import dataclass

from origin.bus import Message
from origin.models.common import DateTimeRange
from origin.models.measurements import Measurement


@dataclass
class MeasurementUpdate(Message):
    """A new Measurement has been added to the system."""

    measurement: Measurement


@dataclass
class MeasurementRemoved(Message):
    """A Measurement has been removed from the system."""

    id: str


@dataclass
class ImportMeasurements(Message):
    """A Measurement has been imported to the system.

    begin.from_ is INCLUDED.
    begin.to_ is EXCLUDED.
    """

    gsrn: str
    begin: DateTimeRange
