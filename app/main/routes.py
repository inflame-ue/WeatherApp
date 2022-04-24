# imports
from flask import render_template
from app.main import main


# routes are created with main blueprint, otherwise it won't work
@main.route("/")
@main.route("/home")
@main.route("/index")
def home():
    return render_template("index.html"), 200
