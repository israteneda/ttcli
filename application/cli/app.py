import uuid
from datetime import datetime

import click

from tt.domain.time_entry import TimeEntry
from tt.repository.memrepo import MemRepo
from tt.use_cases.time_entry_list import time_entry_list_use_case

time_entries = [
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
        start=datetime.now()
    )
    click.echo(f"You start a time entry at {str(time_entry.start).split('.', 1)[0]}")


@tt.group()
def ls():
    """List time entries"""


@ls.command("time-entries")
def list_time_entries():
    click.echo([TimeEntry.to_dict(time_entry) for time_entry in time_entry_list_use_case(repo)])
