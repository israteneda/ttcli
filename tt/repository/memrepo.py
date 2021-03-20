from datetime import time

from tt.domain.time_entry import TimeEntry


class MemRepo:
    def __init__(self, data):
        self.data = data

    def list(self, filters=None):

        result = [TimeEntry.from_dict(time_entry) for time_entry in self.data]

        if filters is None:
            return result

        if "code__eq" in filters:
            result = [
                time_entry
                for time_entry in result
                if time_entry.code == filters["code__eq"]
            ]

        if "project__eq" in filters:
            result = [
                time_entry
                for time_entry in result
                if time_entry.project == filters["project__eq"]
            ]

        if "start_date__lt" in filters:
            result = [
                time_entry
                for time_entry in result
                if time.fromisoformat(time_entry.start_date)
                < time.fromisoformat(str(filters["start_date__lt"]))
            ]

        if "start_date__gt" in filters:
            result = [
                time_entry
                for time_entry in result
                if time.fromisoformat(time_entry.start_date)
                > time.fromisoformat(str(filters["start_date__gt"]))
            ]

        return result