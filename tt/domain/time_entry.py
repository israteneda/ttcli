from datetime import datetime


class TimeEntry:
    start: datetime = None
    end: datetime = None

    def get_time_entry(self):
        return self.end - self.start
