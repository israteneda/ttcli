import json
import uuid
from datetime import datetime

from flask import Blueprint, Response

from tt.domain.time_entry import TimeEntry
from tt.repository.memrepo import MemRepo
from tt.use_cases.time_entry_list import time_entry_list_use_case
from tt.serializers.time_entry import TimeEntryJsonEncoder

blueprint = Blueprint("time_entry", __name__)

time_entries = [
    {
        "code": "0d3cf93b-c443-4949-adf8-06828a92f404",
        "start": "09:00:00",
        "end": "10:00:00"
    },
    {
        "code": "ab7a8a9a-6c0e-4a86-935b-9f3e377471cd",
        "start": "10:00:00",
        "end": "11:00:00"
    },
    {
        "code": "acf285db-e378-43a7-8ddd-c18c4fe1d693",
        "start": "11:00:00",
        "end": "12:00:00"
    },
    {
        "code": "e025b74f-ae25-45a0-b082-0fde2cb56fc6",
        "start": "12:00:00",
        "end": "13:00:00"
    }
]


@blueprint.route("/time-entries", methods=["GET"])
def time_entry_list():
    repo = MemRepo(time_entries)
    result = time_entry_list_use_case(repo)

    return Response(
        json.dumps(result, cls=TimeEntryJsonEncoder),
        mimetype="application/json",
        status=200
    )


@blueprint.route('/clock-in')
def clock_in():
    code = uuid.uuid4()
    time_entry: TimeEntry = TimeEntry(
        code,
        start=datetime.now()
    )
    return f"You start a time entry at {time_entry.start}"
