import json
import uuid
from datetime import datetime

from flask import Blueprint, Response

from tests.data.constants import TIME_ENTRIES
from tt.domain.time_entry import TimeEntry
from tt.repository.memrepo import MemRepo
from tt.use_cases.time_entry_list import time_entry_list_use_case
from tt.serializers.time_entry import TimeEntryJsonEncoder

blueprint = Blueprint("time_entry", __name__)

time_entries = TIME_ENTRIES


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
        project="ioet Inc. - ioet-internal",
        date_in=datetime.now(),
        date_out=None,
        description="Time Tracker CLI developments"
    )
    return f"You start a time entry at {time_entry.date_in}"
