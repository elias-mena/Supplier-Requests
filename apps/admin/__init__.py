from flask import Blueprint

admin = Blueprint('admin', __name__, url_prefix='/admin')

from . import views

"""
This admin module is for create users, change its state and its rol in the app.
"""