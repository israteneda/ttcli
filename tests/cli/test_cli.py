from datetime import datetime

from click.testing import CliRunner

from application.cli.app import clock_in, tt
from tests.data import constants


def test_cli__return__instructions__when_pass_h_or_help_as_argument_to_check_function():
    runner = CliRunner()
    result = runner.invoke(tt, ["--help"])
    assert result.exit_code == 0
    assert result.output == constants.HELP


def test_cli__set_time_tracker_starts__when_calling_clock_in_function():
    runner = CliRunner()
    result = runner.invoke(clock_in)
    assert result.exit_code == 0
    assert (
        result.output
        == f"You start a time entry at {str(datetime.now()).split('.', 1)[0]}\n"
    )
