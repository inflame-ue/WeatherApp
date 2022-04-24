# imports
from flask import render_template, redirect, url_for
from app.main import main
from app.main.forms import SearchForm


# routes are created with main blueprint, otherwise it won't work
@main.route("/", methods=["GET", "POST"])
@main.route("/home", methods=["GET", "POST"])
@main.route("/index", methods=["GET", "POST"])
def home():
    form = SearchForm()

    if form.validate_on_submit():
        return redirect(url_for('main.home'))

    return render_template("index.html", form=form), 200
