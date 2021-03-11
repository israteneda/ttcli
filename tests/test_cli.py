from tests.data import constants
from tt.cli import main


def test_cli__app_run_normally__when_the_cli_app_starts():
    pass


def test_cli__returns_the_isntructions__when_calling_the_main_function(capsys):
    main()
    captured = capsys.readouterr()
    assert captured.out == (constants.BANNER + '\n' +
                            constants.USAGE + '\n' +
                            constants.OPTIONS + '\n' +
                            constants.EXAMPLES + '\n')

