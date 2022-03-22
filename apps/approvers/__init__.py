from flask import Blueprint

approvers = Blueprint('approvers', __name__, url_prefix='/approvers')

from . import views

"""
The module for the approvers contains the paths than can accept or decline requests, and see the reports of 
the requests that the approver has manage in different range of dates.
"""