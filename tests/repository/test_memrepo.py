import pytest

from tt.domain.time_entry import TimeEntry
from tt.repository.memrepo import MemRepo


@pytest.fixture
def time_entries_dict():
    return [
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


def test_repository__return_a_time_entry_list__when_call_repo_list_without_parameters(time_entries_dict):
    repo = MemRepo(time_entries_dict)

    time_entries = [TimeEntry.from_dict(time_entry) for time_entry in time_entries_dict]

    assert repo.list() == time_entries
