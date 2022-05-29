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
    request: Request = get_request(request_id)
    history_info: RequestHistory = RequestHistory(request_id, current_user.id, "A")
    insert_request_history(history_info)
    user_email = get_user_mail(request.customer)
    approver_email = ""

    if current_user.rol == 3:
        update_first_approval_info(history_info)
        if 1 < request.amount < 100000:
            approver_email = get_user_mail("financial1")
        if 100000 < request.amount < 1000000:
            approver_email = get_user_mail("financial2")

        if 1000000 < request.amount < 10000000:
            approver_email = get_user_mail("financial3")

        message = f'Comprador: {current_user.id},\n' \
                  f'Monto: {request.amount},\n' \
                  f'Producto: {request.product},\n' \
                  f'Descripcion: {request.description} \n'

        message_data = {
            'subject': 'New request',
            'emails': [approver_email],
            'message': message
        }
        send_mail(**message_data)
        flash('Se ha aprobado la solicitud y se ha enviado un correo de notificacion '
              'al cliente y al aprovador financiero para su revisión!')

    if current_user.rol in (4, 5, 6):
        update_second_approval_info(history_info)
        request.status = "A"
        flash('Se ha aprobado la solicitud y se ha enviado un correo de notificación al cliente!')

    message = f'La solicitud con id: {request.id},\n' \
              f'Fue aprovada por el aprovador: {current_user.id},\n' \

    message_data = {
        'subject': 'Request Accepted',
        'emails': [user_email],
        'message': message
    }

    if current_user.rol > 3:
        update_second_approval_info(history_info)
        request.status = "A"
        update_request_status(request)
        flash('Se ha enviado un correo de notificación al cliente!')

    send_mail(**message_data)
    update_request_status(request)
    return redirect(url_for("approvers.index"))


@approvers.route('decline/<int:request_id>/', methods=['GET', 'POST'])
@login_required
def decline_request(request_id: int):
    """"
    Declines a request
    """
    request: Request = get_request(request_id)
    history_info: RequestHistory = RequestHistory(request_id, current_user.id, "A")
    insert_request_history(history_info)

    request.status = "D"
    update_request_status(request)

    message = f'La solicitud con id: {request.id},\n' \
              f'Fue rechazada por el aprovador: {current_user.id},\n' \

    user_email = get_user_mail(request.customer)

    message_data = {
        'subject': 'New request',
        'emails': [user_email],
        'message': message
    }
    send_mail(**message_data)
    flash('Se ha rechazado la solicitud y se ha enviado un correo de notificacion al cliente!')
    return redirect(url_for("approvers.index"))


@approvers.route('/reports', methods=['GET', 'POST'])
@login_required
def reports():
    """Reports"""
    requests = get_approver_requests(current_user.id)
    context = {
        'user': current_user,
        'requests': requests
    }
    return render_template('approver-reports.html', **context)


@approvers.route('/reports/<int:months>', methods=['GET', 'POST'])
@login_required
def reports_by_months(months: int):
    requests = get_requests_by_month(months)
    context = {
        'user': current_user,
        'requests': requests
    }
    return render_template('approver-reports.html', **context)


@approvers.route('/reports/<string:status>', methods=['GET', 'POST'])
@login_required
def reports_by_status(status: str):
    """Reports by requests status"""
    requests = get_requests_by_status(status)
    context = {
        'user': current_user,
        'requests': requests
    }
    return render_template('approver-reports.html', **context)