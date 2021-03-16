import json

import pytest

from tt.domain.time_entry import TimeEntry

time_entry_dict = {
    "code": "db2904b5-3fc0-4780-b7a8-26d688e088a2",
    "start": "09:00:00",
    "end": "10:00:00"
}

time_entries = [TimeEntry.from_dict(time_entry_dict)]


def test_time_entry__return_time_entries__when_call_get_time_entries_method(mocker, client):
    mock_use_case = mocker.patch('application.rest.time_entry.time_entry_list_use_case')
    mock_use_case.return_value = time_entries

    http_response = client.get("/time-entries")

    assert json.loads(http_response.data.decode("UTF-8")) == [time_entry_dict]
    mock_use_case.assert_called()
    assert http_response.status_code == 200
    assert http_response.mimetype == "application/json"