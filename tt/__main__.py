import os

from application.cli.app import tt
from application.rest.app import app


class InvalidEnviroment(Exception):
    pass


if __name__ == '__main__':
    tt_env = os.environ['TT_ENV']
    if tt_env == 'cli':
        tt()
    elif tt_env == 'api':
        app.run()
    else:
        raise (InvalidEnviroment("TT_ENV has an invalid value."))
