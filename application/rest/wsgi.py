import os

from application.rest.app import create_app

app = create_app(os.environ["FLASK_CONFIG"])