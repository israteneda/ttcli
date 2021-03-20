import uuid
from datetime import datetime, time, timedelta

from tt.domain.time_entry import TimeEntry


def test_domain_time_entry__create_a_time_entry__when_model_init():
    code = uuid.uuid4()
    time_entry = TimeEntry(
        code,
        project="ioet Inc. - ioet-internal",
        start_date=time.fromisoformat("09:00:00"),
        end_date=time.fromisoformat("10:00:00"),
        description="Time Tracker CLI developments",
    )

    assert time_entry.code == code
    assert time_entry.project == "ioet Inc. - ioet-internal"
    assert str(time_entry.start_date).split(".", 1)[0] == "09:00:00"
    assert str(time_entry.end_date).split(".", 1)[0] == "10:00:00"
    assert time_entry.description == "Time Tracker CLI developments"


def test_domain_time_entry__create_a_time_entry__when_passing_a_model_as_a_dictionary():
    code = uuid.uuid4()
    init_dict = {
        "code": code,
        "project": "ioet Inc. - ioet-internal",
        "start_date": time.fromisoformat("09:00:00"),
        "end_date": time.fromisoformat("10:00:00"),
        "description": "Time Tracker CLI developments",
    }

    time_entry = TimeEntry.from_dict(init_dict)

    assert time_entry.code == code
    assert time_entry.project == "ioet Inc. - ioet-internal"
    assert str(time_entry.start_date).split(".", 1)[0] == "09:00:00"
    assert str(time_entry.end_date).split(".", 1)[0] == "10:00:00"
    assert time_entry.description == "Time Tracker CLI developments"


def test_domain_time_entry__create_a_dictionary__when_to_dict_function_is_called():
    code = uuid.uuid4()
    init_dict = {
        "code": code,
        "project": "ioet Inc. - ioet-internal",
        "start_date": time.fromisoformat("09:00:00"),
        "end_date": time.fromisoformat("10:00:00"),
        "description": "Time Tracker CLI developments",
    }

    time_entry = TimeEntry.from_dict(init_dict)

    assert time_entry.to_dict() == init_dict


def test_domain_time_entry__return_true__when_two_equal_models_are_compared():
    code = uuid.uuid4()
    init_dict = {
        "code": code,
        "project": "ioet Inc. - ioet-internal",
        "start_date": time.fromisoformat("09:00:00"),
        "end_date": time.fromisoformat("10:00:00"),
        "description": "Time Tracker CLI developments",
    }

    first_time_entry = TimeEntry.from_dict(init_dict)
    second_time_entry = TimeEntry.from_dict(init_dict)

    assert first_time_entry == second_time_entry


def test_domain_time_entry__returns_the_difference_between_start_date_and_end_date__when_calling_get_time_entry_function():
    code = uuid.uuid4()
    time_entry: TimeEntry = TimeEntry(
        code,
        project="ioet Inc. - ioet-internal",
        start_date=datetime.now(),
        end_date=datetime.now() + timedelta(hours=1),
        description="Time Tracker CLI developments",
    )
    assert "1:00:00" == str(time_entry.get_time_entry()).split(".", 1)[0]


def test_domain_time_entry__set_and_get_time_entry_start_date_attribute__when_calling_start_date_setter_and_getter():
    code = uuid.uuid4()
    time_entry: TimeEntry = TimeEntry(
        code,
        project="ioet Inc. - ioet-internal",
        start_date=time.fromisoformat("14:00:00"),
        end_date=None,
        description="Time Tracker CLI developments",
    )
    assert "14:00:00" == str(time_entry.start_date).split(".", 1)[0]
