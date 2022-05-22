from typing import List

# Flask stuff
from flask import (
    render_template,
    redirect,
    flash,
    url_for
)

from flask_login import login_required, current_user

from models import UserInfo, User

from db_service import (
    get_user,
    get_users,
    update_user_state,
    update_user_rol,
    insert_user
)

from werkzeug.security import generate_password_hash

from .forms import NewUserForm


# Blueprint
from . import admin


@admin.route('/', methods=['GET', 'POST'])
@login_required
def index():
    """
    # Admin Index

    This is the path of the main page for the admins, where they can see the list of users and manage them.
    """
    users: List[UserInfo] = get_users()
    context = {
        'user': current_user,
        'users': users,
         }
    return render_template('admin.html', **context)


@admin.route('/new', methods=['GET', 'POST'])
@login_required
def new():
    """
    # New User

    This path is for create a new user in the app
    """
    form = NewUserForm()
    context = {
        'user': current_user,
        'form': form,
         }
    if form.validate_on_submit():
        if get_user(form.username.data):
            flash('Ya existe ese nombre de usuario!')

        else:
            user_data: User = User(
                form.username.data,
                form.first_name.data,
                form.last_name.data,
                form.birth_date.data,
                form.rol.data,  # Number of the client rol, only they can register an account
                form.email.data,
                generate_password_hash(form.password.data),
                'A'  # The status is active by default
            )

            insert_user(user_data)
            flash('Usuario Registrado!')

            return redirect(url_for('admin.index'))
    return render_template('new-user.html', **context)





