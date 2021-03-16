from flask import Flask

from application.rest import time_entry


def create_app(config_name):
    app = Flask(__name__)

    config_module = f"application.rest.config.{config_name.capitalize()}Config"

    app.config.from_object(config_module)

    app.register_blueprint(time_entry.blueprint)

    return app
