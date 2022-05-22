from typing import List

# Flask stuff
from flask import (
    render_template,
    flash
)

from flask_login import login_required, current_user

# Models
from models import (
    Request,
    FullRequestInfo,
    User
)

# Db Methods
from db_service import (
    get_client_requests,
    get_request,
    insert_request,
    insert_full_request_info
)

# Mail Service
from apps.mail_service import send_mail

# Forms
from .forms import RequestForm

# Blueprint
from . import customers


@customers.route('/', methods=['GET', 'POST'])
@login_required
def index():
    """
    Customers index

    This is the view of the main page for the customers, where they can make new requests.
    """
    form = RequestForm()
    context = {
        'user': current_user,
        'form': form
    }
    if form.validate_on_submit():
        # Create a new request
        new_request = Request(
            product=form.product.data,
            description=form.description.data,
            amount=form.amount.data,
            customer=current_user.id
        )
        insert_request(new_request)

        # Get the object with the request info as dict
        new_request_info: dict = get_request(new_request.id).as_dict()

        # Cast the date to string for the JSON format
        new_request_info['created_at'] = str(new_request_info['created_at'])

        # Insert the RequestInfo object as JSON in the full_request_info table
        full_info = FullRequestInfo(new_request.id, new_request_info, None, None)
        insert_full_request_info(full_info)

        # Notify the user and the approver about the new request

        approver_email = User.query.filter_by(username='chief').first().email

        message = f'Comprador: {current_user.id},\n' \
             f'Monto: {new_request.amount},\n' \
             f'Producto: {new_request.product},\n' \
             f'Descripcion: {new_request.description} \n'

        message_data = {
            'subject': 'New request',
            'emails': [current_user.email, approver_email],
            'message': message
        }

        send_mail(**message_data)

        flash('Se ha enviado la solicitud de compra y se ha enviado un correo al aprovador para su revisión!')
    return render_template('customers.html', **context)



