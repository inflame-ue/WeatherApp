# imports
from flask import render_template, redirect, url_for
from app.main import main
from app.main.forms import SearchForm
import requests
import dotenv
import os

# load .env file from the local system
dotenv.load_dotenv("C://EnvironmentalVariables//.env")

# constants
WEATHER_API_URL = "https://api.openweathermap.org/data/2.5/weather"
GEOCODING_API_URL = "http://api.openweathermap.org/geo/1.0/direct"
API_KEY = os.environ.get("WEATHER_API_KEY")


# routes are created with main blueprint, otherwise it won't work
@main.route("/", methods=["GET", "POST"])
@main.route("/home", methods=["GET", "POST"])
@main.route("/index", methods=["GET", "POST"])
def home():
    form = SearchForm()

    if form.validate_on_submit():
        # params for geocoding api
        geocoding_params = {
            'q': form.city.data,
            'appid': API_KEY,
            'limit': 1,
        }

        # make a GET request to the Geocoding API to get the coordinates of the city that user has searched for
        response = requests.get(url=GEOCODING_API_URL, params=geocoding_params)
        response.raise_for_status()

        lat, lon = response.json()['lat'], response.json()['lon']
        print(lat, lon)

    return render_template("index.html", form=form), 200
