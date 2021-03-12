from datetime import datetime

from click.testing import CliRunner

from tests.data import constants
from tt.cli.app import cli
from tt.cli.app import clock_in


def test_app__return__instructions__when_pass_h_or_help_as_argument_to_check_function(capsys):
    runner = CliRunner()
    result = runner.invoke(cli, ['--help'])
    assert result.exit_code == 0
    assert result.output == constants.HELP


def test_app__set_time_tracker_start__when_calling_clock_in_function():
    runner = CliRunner()
    result = runner.invoke(clock_in)
    assert result.exit_code == 0
    assert result.output == f'You start a time entry at {datetime.now()}\n'
