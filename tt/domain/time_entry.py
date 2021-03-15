import dataclasses
import uuid
from dataclasses import dataclass
from datetime import datetime


@dataclass
class TimeEntry:
    code: uuid.UUID
    start: datetime = None
    end: datetime = None

    @classmethod
    def from_dict(clss, d):
        return clss(**d)

    def to_dict(self):
        return dataclasses.asdict(self)

    def get_time_entry(self):
        return self.end - self.start
