import json
import uuid
from datetime import datetime

from flask import Blueprint, Response, request

from application.data.constants import STATUS_CODE, TIME_ENTRIES
from tt.domain.time_entry import TimeEntry
from tt.repository.memrepo import MemRepo
from tt.request.time_entry_list_request import build_time_entry_list_request
from tt.use_cases.time_entry_list import time_entry_list_use_case
from tt.serializers.time_entry import TimeEntryJsonEncoder

blueprint = Blueprint("time_entry", __name__)


time_entries = TIME_ENTRIES


@blueprint.route("/time-entries", methods=["GET"])
def time_entry_list():
    query_str_params = {
        "filters": {},
    }

    for arg, values in request.args.items():
        if arg.startswith("filter_"):
            query_str_params["filters"][arg.replace("filter_", "")] = values

    request_object = build_time_entry_list_request(filters=query_str_params["filters"])

    repo = MemRepo(time_entries)
    response = time_entry_list_use_case(repo, request_object)

    return Response(
        json.dumps(response.value, cls=TimeEntryJsonEncoder),
        mimetype="application/json",
        status=STATUS_CODE[response.type],
    )


@blueprint.route("/clock-in")
def clock_in():
    code = uuid.uuid4()
    time_entry: TimeEntry = TimeEntry(
        code,
        project="ioet Inc. - ioet-internal",
        start_date=datetime.now(),
        end_date=None,
        description="Time Tracker CLI developments",
    )
    return f"You start a time entry at {time_entry.start_date}"
