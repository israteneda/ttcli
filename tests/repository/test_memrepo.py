import pytest

from tests.data.constants import TIME_ENTRIES
from tt.domain.time_entry import TimeEntry
from tt.repository.memrepo import MemRepo


@pytest.fixture
def time_entries_dict():
    return TIME_ENTRIES


def test_repository__return_a_time_entry_list__when_call_repo_list_without_parameters(time_entries_dict):
    repo = MemRepo(time_entries_dict)

    time_entries = [TimeEntry.from_dict(time_entry) for time_entry in time_entries_dict]

    assert repo.list() == time_entries
