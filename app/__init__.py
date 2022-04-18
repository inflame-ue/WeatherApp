# imports
from flask import Flask
from config import config


# application factory
def create_app(config_name):
    # init the application
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # init extensions

    # register blueprints

    return app
