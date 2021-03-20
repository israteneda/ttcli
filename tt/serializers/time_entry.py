import json


class TimeEntryJsonEncoder(json.JSONEncoder):
    def default(self, o):
        try:
            to_serialize = {
                "code": str(o.code),
                "project": str(o.project),
                "start_date": str(o.start_date).split(".", 1)[0],
                "end_date": str(o.end_date).split(".", 1)[0],
                "description": str(o.description),
            }
            return to_serialize
        except AttributeError:  # pragma: no cover
            return super().default(o)
