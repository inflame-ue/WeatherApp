# imports
import dotenv
import os

# load .env file from local system
dotenv.load_dotenv("C://EnvironmentalVariables//.env")


class BaseConfig:
    """Base Config for the application. Every other config inherits from it."""
    SECRET_KEY = os.environ.get("WEATHER_APP_SECRET_KEY") or "hard_to_guess_string"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(BaseConfig):
    """Config that will be used during development. So, debugging is enabled."""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("DEV_DATABASE_URI") or "sqlite:///dev-data.db"


class TestingConfig(BaseConfig):
    """Config for unit testing."""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("TEST_DATABASE_URI") or "sqlite:///test-data.db"


class ProductionConfig(BaseConfig):
    """Config for final production."""
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URI") or "sqlite:///data.db"


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig,
}
