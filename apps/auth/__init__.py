from flask import Blueprint

auth = Blueprint('auth', __name__, url_prefix='/auth')

from . import views

"""
The auth module contains the paths for authenticate the user in the app.
"""