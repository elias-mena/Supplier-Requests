from typing import List

# Flask stuff
from flask import (
    render_template,
    flash,
    redirect,
    url_for
)

from flask_login import login_required, current_user

# Models
from models import (
    Request,
    RequestHistory,
    FullRequestInfo
)

# Db Methods
from db_service import (
    get_approver_pending_requests,
    get_approver_requests,
    get_request,
    get_requests_by_month,
    get_requests_by_status,
    update_request_status,
    get_user_mail,
    update_first_approval_info,
    update_second_approval_info,
    insert_request_history
)

from ..mail_service import send_mail

# Blueprint
from . import approvers


@approvers.route('/', methods=['GET', 'POST'])
@login_required
def index():
    """
    Approvers index

    This is the view of the main page for the approvers, where they can accept or decline requests.
    """
    requests = get_approver_pending_requests(current_user.rol)
    context = {
        'user': current_user,
        'requests': requests
    }
    return render_template('approvers.html', **context)


@approvers.route('accept/<int:request_id>/', methods=['GET', 'POST'])
@login_required
def accept_request(request_id: int):
    """
    Accepts a request
    """
    pass


@approvers.route('decline/<int:request_id>/', methods=['GET', 'POST'])
@login_required
def decline_request(request_id: int):
    """"
    Declines a request
    """
    pass


@approvers.route('/reports', methods=['GET', 'POST'])
@login_required
def reports():
    """Reports"""
    pass


@approvers.route('/reports/<int:months>', methods=['GET', 'POST'])
@login_required
def reports_by_months(months: int):
    pass


@approvers.route('/reports/<string:status>', methods=['GET', 'POST'])
@login_required
def reports_by_status(status: str):
    """Reports by requests status"""
    pass
