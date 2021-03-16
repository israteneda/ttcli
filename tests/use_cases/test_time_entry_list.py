from datetime import time

import pytest
import uuid

from tt.domain.time_entry import TimeEntry
from tt.use_cases.time_entry_list import time_entry_list_use_case


@pytest.fixture
def domain_time_entries():
    time_entry_1 = TimeEntry(
        code=uuid.uuid4(),
        start=time.fromisoformat('09:00:00'),
        end=time.fromisoformat('10:00:00')
    )

    time_entry_2 = TimeEntry(
        code=uuid.uuid4(),
        start=time.fromisoformat('10:00:00'),
        end=time.fromisoformat('11:00:00')
    )

    time_entry_3 = TimeEntry(
        code=uuid.uuid4(),
        start=time.fromisoformat('11:00:00'),
        end=time.fromisoformat('12:00:00')
    )

    time_entry_4 = TimeEntry(
        code=uuid.uuid4(),
        start=time.fromisoformat('12:00:00'),
        end=time.fromisoformat('13:00:00')
    )

    return [time_entry_1, time_entry_2, time_entry_3, time_entry_4]


def test_time_entry_list__return_all_time_entries__when_call_time_entry_list_use_case_without_parameters(mocker):
    repo = mocker.Mock()
    repo.list.return_value = domain_time_entries

    result = time_entry_list_use_case(repo)

    repo.list.assert_called_with()
    assert result == domain_time_entries
