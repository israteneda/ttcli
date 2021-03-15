import uuid
from datetime import datetime

import click

from tt.domain.time_entry import TimeEntry


@click.group()
def tt():
    """Time Tracker CLI

    App to register time entries
    """


@tt.group()
def clock():
    """Manage time entries"""


@clock.command("in")
def clock_in():
    """Clock in a time entry"""
    code = uuid.uuid4()
    time_entry: TimeEntry = TimeEntry(
        code,
        start=datetime.now()
    )
    click.echo(f"You start a time entry at {str(time_entry.start).split('.', 1)[0]}")
