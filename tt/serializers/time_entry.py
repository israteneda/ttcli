import json


class TimeEntryJsonEncoder(json.JSONEncoder):
    def default(self, o):
        try:
            to_serialize = {
                "code": str(o.code),
                "project": str(o.project),
                "date_in": str(o.date_in).split('.', 1)[0],
                "date_out": str(o.date_out).split('.', 1)[0],
                "description": str(o.description)
            }
            return to_serialize
        except AttributeError:  # pragma: no cover
            return super().default(o)
