import json
import uuid
from datetime import time

from tt.serializers.time_entry import TimeEntryJsonEncoder
from tt.domain.time_entry import TimeEntry


def test_serializers__return_time_entry_serialized__when_call_time_entry_json_encoder():
    code = uuid.uuid4()

    time_entry = TimeEntry(
        code=code,
        project="ioet Inc. - ioet-internal",
        date_in=time.fromisoformat("09:00:00"),
        date_out=time.fromisoformat("10:00:00"),
        description="Time Tracker CLI developments"
    )

    expected_json = f"""
        {{
            "code": "{code}",
            "project": "ioet Inc. - ioet-internal",
            "date_in": "09:00:00",
            "date_out": "10:00:00",
            "description": "Time Tracker CLI developments"
        }}
    """

    json_time_entry = json.dumps(time_entry, cls=TimeEntryJsonEncoder)

    assert json.loads(json_time_entry) == json.loads(expected_json)
