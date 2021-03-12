from datetime import datetime

import click

from tt.domain.time_entry import TimeEntry


@click.group()
def cli():
    """Time Tracker CLI

    App to register time entries
    """


@cli.group()
def clock():
    """Manage time entries"""


@clock.command("in")
def clock_in():
    """Clock in a time entry"""

    time_entry: TimeEntry = TimeEntry()
    time_entry.start = datetime.now()
    click.echo(f"You start a time entry at {time_entry.start}")
