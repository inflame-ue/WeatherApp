# imports
from flask import Blueprint

# init blueprint
main = Blueprint("main", __name__)

# avoid circular imports(because of that routes are imported at the end of the file)
from app.main import routes, errors
