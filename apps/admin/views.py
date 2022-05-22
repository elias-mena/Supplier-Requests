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





