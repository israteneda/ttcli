import json


class TimeEntryJsonEncoder(json.JSONEncoder):
    def default(self, o):
        try:
            to_serialize = {
                "code": str(o.code),
                "start": str(o.start).split('.', 1)[0],
                "end": str(o.end).split('.', 1)[0]
            }
            return to_serialize
        except AttributeError:  # pragma: no cover
            return super().default(o)
