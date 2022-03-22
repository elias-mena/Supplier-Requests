from flask import Blueprint

customers = Blueprint('customers', __name__, url_prefix='/customers')

from . import views

"""
The module for the costumer contains the paths than can create a new requests, see the state of the requests
it has made, and see the reports of the requests in different range of dates.
"""