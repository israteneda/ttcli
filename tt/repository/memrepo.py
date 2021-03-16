from tt.domain.time_entry import TimeEntry


class MemRepo:
    def __init__(self, data):
        self.data = data

    def list(self):
        return [TimeEntry.from_dict(time_entry) for time_entry in self.data]
