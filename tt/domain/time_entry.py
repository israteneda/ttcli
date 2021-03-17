import dataclasses
import uuid
from dataclasses import dataclass
from datetime import datetime


@dataclass
class TimeEntry:
    code: uuid.UUID
    project: str
    date_in: datetime
    date_out: datetime
    description: str

    @classmethod
    def from_dict(cls, d):
        return cls(**d)

    def to_dict(self):
        return dataclasses.asdict(self)

    def get_time_entry(self):
        return self.date_out - self.date_in


@dataclass
class TimeEntryIoet(TimeEntry):
    activity: str
    ticket: str
    technology: str
