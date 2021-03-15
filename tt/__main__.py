import os

from application.cli.app import cli
from application.rest.app import app


class InvalidEnviroment(Exception):
    pass


if __name__ == '__main__':
    tt_env = os.environ['TT_ENV']
    if tt_env == 'cli':
        cli()
    elif tt_env == 'rest':
        app.run()
    else:
        raise (InvalidEnviroment("TT_ENV has an invalid value."))
