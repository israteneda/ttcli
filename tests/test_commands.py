from tests.data.instructions import banner
from tt.commands import instructions
from tt.commands import check


def test_commands__returns_instructions__when_calling_the_instruction_function():
    assert instructions() == banner


def test_commands__return__instructions__when_pass_h_or_help_as_argument_to_check_function(capsys):
    check("-h")
    captured = capsys.readouterr()
    assert captured.out == banner + '\n'
