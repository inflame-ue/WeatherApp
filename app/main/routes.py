# imports
from flask import render_template, redirect, url_for
from app.main import main
from app.main.forms import SearchForm


# routes are created with main blueprint, otherwise it won't work
@main.route("/")
@main.route("/home")
@main.route("/index")
def home():
    form = SearchForm()

    if form.validate_on_submit():
        return redirect(url_for('main.home'))

    return render_template("index.html", form=form), 200
