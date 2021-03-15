import uuid
from datetime import datetime, time

from click.testing import CliRunner

from tests.data import constants
from application.cli.app import tt
from application.cli.app import clock_in
from tt.domain.time_entry import TimeEntry


def test_cli__return__instructions__when_pass_h_or_help_as_argument_to_check_function(capsys):
    runner = CliRunner()
    result = runner.invoke(tt, ['--help'])
    assert result.exit_code == 0
    assert result.output == constants.HELP


def test_cli__set_time_tracker_start__when_calling_clock_in_function():
    runner = CliRunner()
    result = runner.invoke(clock_in)
    assert result.exit_code == 0
    assert result.output == f"You start a time entry at {str(datetime.now()).split('.', 1)[0]}\n"
