# TODO: Create form for searching information about the desired weather

# imports
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class SearchForm(FlaskForm):
    """This form implements the search form for the application"""
    city = StringField("", validators=[DataRequired()])
    search = SubmitField("Search")
