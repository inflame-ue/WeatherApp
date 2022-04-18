# imports
from app import create_app
import dotenv
import os

# load .env file from local system
dotenv.load_dotenv("C://EnvironmentalVariables//.env")  # your absolute path may differ

# create an app from the application factory
app = create_app(os.environ.get("APP_CONFIG") or "default")

# run config
if __name__ == "__main__":
    app.run()
