import uuid
from datetime import time

import pytest
from tt.domain.time_entry import TimeEntry
from tt.request.time_entry_list_request import build_time_entry_list_request
from tt.responses.response import ResponseTypes
from tt.use_cases.time_entry_list import time_entry_list_use_case


@pytest.fixture
def domain_time_entries():
    return [
        TimeEntry(
            code=uuid.uuid4(),
            project="ioet Inc. - ioet-internal",
            date_in=time.fromisoformat("09:00:00"),
            date_out=time.fromisoformat("10:00:00"),
            description="Time Tracker CLI developments",
        ),
        TimeEntry(
            code=uuid.uuid4(),
            project="ioet Inc. - ioet-internal",
            date_in=time.fromisoformat("10:00:00"),
            date_out=time.fromisoformat("11:00:00"),
            description="Time Tracker CLI developments",
        ),
        TimeEntry(
            code=uuid.uuid4(),
            project="ioet Inc. - ioet-internal",
            date_in=time.fromisoformat("11:00:00"),
            date_out=time.fromisoformat("12:00:00"),
            description="Time Tracker CLI developments",
        ),
        TimeEntry(
            code=uuid.uuid4(),
            project="ioet Inc. - ioet-internal",
            date_in=time.fromisoformat("12:00:00"),
            date_out=time.fromisoformat("13:00:00"),
            description="Time Tracker CLI developments",
        ),
    ]


def test_use_cases_time_entry_list__return_all_time_entries__when_call_time_entry_list_use_case_without_parameters(
    mocker, domain_time_entries
):
    repo = mocker.Mock()
    repo.list.return_value = domain_time_entries

    request = build_time_entry_list_request()

    response = time_entry_list_use_case(repo, request)

    assert bool(response) is True
    repo.list.assert_called_with(filters=None)
    assert response.value == domain_time_entries


def test_use_cases_time_entry_list__return_a_generic_error__when_call_time_entry_list_use_case_without_filters(
    mocker,
):
    repo = mocker.Mock()
    repo.list.side_effect = Exception("Just an error message")

    request = build_time_entry_list_request(filters={})

    response = time_entry_list_use_case(repo, request)

    assert bool(response) is False
    assert response.value == {
        "type": ResponseTypes.SYSTEM_ERROR,
        "message": "Exception: Just an error message",
    }


def test_use_cases_time_entry_list__return_a_generic_error__when_call_time_entry_list_use_case_with_bad_request(
    mocker,
):
    repo = mocker.Mock()

    request = build_time_entry_list_request(filters=5)

    response = time_entry_list_use_case(repo, request)

    assert bool(response) is False
    assert response.value == {
        "type": ResponseTypes.PARAMETERS_ERROR,
        "message": "filters: Is not iterable",
    }
