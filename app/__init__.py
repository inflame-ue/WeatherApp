# imports
from flask import Flask
from flask_bootstrap import Bootstrap
from config import config

# create an instance of each extension class, but remember to initialize it in the application factory
bootstrap = Bootstrap()


# application factory
def create_app(config_name):
    # init the application
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # init extensions
    bootstrap.init_app(app)

    # register blueprints
    from app.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
