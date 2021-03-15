from datetime import datetime, timedelta, time

from tt.domain.time_entry import TimeEntry


def test_time_entry__returns_the_difference_between_start_time_and_end_time__when_calling_get_time_entry_function():
    time_entry: TimeEntry = TimeEntry()
    time_entry.start = datetime.now()
    time_entry.end = datetime.now() + timedelta(hours=1)
    assert "1:00:00" == str(time_entry.get_time_entry()).split('.', 1)[0]


def test_time_entry__set_and_get_time_entry_start_attribute__when_calling_start_setter_and_getter():
    time_entry: TimeEntry = TimeEntry()
    time_entry.start = time.fromisoformat('14:00:00')
    assert "14:00:00" == str(time_entry.start).split('.', 1)[0]


def test_time_entry__get_time_entry_start__when_callig_start_getter():
    time_entry: TimeEntry = TimeEntry()
    assert None == time_entry.start
