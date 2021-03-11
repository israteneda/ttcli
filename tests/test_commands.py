from tests.data import constants
from tt.instructions import check


def test_instructions__return__instructions__when_pass_h_or_help_as_argument_to_check_function(capsys):
    check("-h")
    captured = capsys.readouterr()
    assert captured.out == (constants.banner + '\n' +
                            constants.usage + '\n' +
                            constants.options + '\n' +
                            constants.examples + '\n')
