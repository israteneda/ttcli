import pytest
from tests.data.constants import TIME_ENTRIES
from tt.domain.time_entry import TimeEntry
from tt.repository.memrepo import MemRepo


@pytest.fixture
def time_entries_dict():
    return TIME_ENTRIES


def test_repository_memrepo__return_a_time_entry_list__when_call_repo_list_without_parameters(
    time_entries_dict,
):
    repo = MemRepo(time_entries_dict)

    time_entries = [TimeEntry.from_dict(time_entry) for time_entry in time_entries_dict]

    assert repo.list() == time_entries


def test_repository_memrepo__return_a_time_entry__when_call_repo_list_with_code_equal_filter(
    time_entries_dict,
):
    repo = MemRepo(time_entries_dict)

    time_entries = repo.list(
        filters={"code__eq": "0d3cf93b-c443-4949-adf8-06828a92f404"}
    )

    assert len(time_entries) == 1
    assert time_entries[0].code == "0d3cf93b-c443-4949-adf8-06828a92f404"


def test_repository_memrepo__return_a_time_entry__when_call_repo_list_with_project_equal_filter(
    time_entries_dict,
):
    repo = MemRepo(time_entries_dict)

    time_entries = repo.list(filters={"project__eq": "ioet Inc. - ioet-internal"})

    assert len(time_entries) == 4
    assert time_entries[0].code == "0d3cf93b-c443-4949-adf8-06828a92f404"


def test_repository_memrepo__return_a_time_entry_list__when_call_repo_list_with_start_date_less_than_filter(
    time_entries_dict,
):
    repo = MemRepo(time_entries_dict)

    time_entries = repo.list(filters={"start_date__lt": "10:00:00"})

    assert len(time_entries) == 1
    assert time_entries[0].code == "0d3cf93b-c443-4949-adf8-06828a92f404"


def test_repository_memrepo__return_a_time_entry_list__when_call_repo_list_with_start_date_grater_than_filter(
    time_entries_dict,
):
    repo = MemRepo(time_entries_dict)

    time_entries = repo.list(filters={"start_date__gt": "09:00:00"})

    assert len(time_entries) == 3
    assert set([time_entry.code for time_entry in time_entries]) == {
        "ab7a8a9a-6c0e-4a86-935b-9f3e377471cd",
        "acf285db-e378-43a7-8ddd-c18c4fe1d693",
        "e025b74f-ae25-45a0-b082-0fde2cb56fc6",
    }


def test_repository_memrepo__return_a_time_entry_list__when_call_repo_list_with_start_date_between_filter(
    time_entries_dict,
):
    repo = MemRepo(time_entries_dict)

    time_entries = repo.list(
        filters={"start_date__lt": "12:00:00", "start_date__gt": "09:00:00"}
    )

    assert len(time_entries) == 2
    assert time_entries[0].code == "ab7a8a9a-6c0e-4a86-935b-9f3e377471cd"


def test_repository_memrepo__return_an_error__when_call_repo_list_with_start_date_as_int(
    time_entries_dict,
):
    repo = MemRepo(time_entries_dict)

    repo.list(filters={"start_date__eq": 10})
    repo.list(filters={"start_date__lt": 10})
    repo.list(filters={"start_date__gt": 10})
