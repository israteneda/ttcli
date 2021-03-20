import uuid
from datetime import datetime

import click

from tests.data.constants import TIME_ENTRIES
from tt.domain.time_entry import TimeEntry
from tt.repository.memrepo import MemRepo
from tt.use_cases.time_entry_list import time_entry_list_use_case

time_entries = TIME_ENTRIES

repo = MemRepo(time_entries)


@click.group()
def tt():
    """Time Tracker CLI

    App to register time entries
    """


@tt.group()
def clock():
    """Clock in and clock out"""


@clock.command("in")
def clock_in():
    """Clock in a time entry"""
    code = uuid.uuid4()
    time_entry: TimeEntry = TimeEntry(
        code,
        project="ioet Inc. - ioet-internal",
        start_date=datetime.now(),
        end_date=None,
        description="Time Tracker CLI developments"
    )
    click.echo(f"You start a time entry at {str(time_entry.start_date).split('.', 1)[0]}")


@tt.group()
def ls():
    """List time entries"""


@ls.command("time-entries")
def list_time_entries():
    click.echo([TimeEntry.to_dict(time_entry) for time_entry in time_entry_list_use_case(repo)])
