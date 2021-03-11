from tests.data import constants
from tt.commands import check


def test_instructions__return__instructions__when_pass_h_or_help_as_argument_to_check_function(capsys):
    check("-h")
    captured = capsys.readouterr()
    assert captured.out == (constants.BANNER+ '\n' +
                            constants.USAGE + '\n' +
                            constants.OPTIONS + '\n' +
                            constants.EXAMPLES + '\n')
