# Flask stuff
from flask import (
    render_template,
    redirect,
    flash,
    url_for
)

from flask_login import (
    login_user,
    login_required,
    logout_user
)

# Algorithm to encrypt and unencrypt passwords.
from werkzeug.security import generate_password_hash, check_password_hash

# Forms
from .forms import (
    LoginForm,
    RegistrationForm
)

from apps.db_service import get_user, insert_user
from apps.models import UserModel, User

# Blueprint
from . import auth


@auth.route('/login', methods=['GET', 'POST'])
def login():
    """
    # Login

    Path for authenticate the user in order to have access to its respective module in the app
    """
    # We send the form info in the context
    form = LoginForm()
    context = {
        'form': form,
    }
    # Then we validate if the form is sent
    if form.validate_on_submit():
        username: str = form.username.data
        password: str = form.password.data

        # Query for the user in the db
        user: User = get_user(username)

        if user:
            # If user exists validate password
            password_from_db: str = user.password
            if check_password_hash(password_from_db, password):  # Compares (password,hash)
                if user.status == 'A':
                    user_data = UserModel(user)

                    # Flask login method
                    login_user(user_data)
                    flash('Bienvenido!')
                    if user.rol == 1:
                        return redirect(url_for('admin.index'))
                    if user.rol == 2:
                        return redirect(url_for('customers.index'))
                    else:
                        # There are 2 different kind of approvers
                        return redirect(url_for('approvers.index'))
                else:
                    flash('El usuario se encuentra inactivo')
            else:
                flash('La contraseña no coincide')
        else:
            flash('El nombre de usuario no existe')

    return render_template('login.html', **context)


# Method to validate the register form
@auth.route('/register', methods=['GET', 'POST'])
def register():
    """
    Register

    Path for register a customer user in the app
    """
    form = RegistrationForm()
    context = {
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
                2,  # Number of the client rol, only they can register an account
                form.email.data,
                generate_password_hash(form.password.data),
                'A'  # The status is active by default
            )
            insert_user(user_data)
            flash('Usuario Registrado!')

            user = UserModel(user_data)

            # Flask login method
            login_user(user)

            return redirect(url_for('customers.index'))
    return render_template('register.html', **context)


@auth.route('/logout')
@login_required
def logout():
    """
    # Logout

    This path closes the current session and request the login again.
    """
    # Flask login method
    logout_user()
    flash('Vuelve pronto!')
    return redirect(url_for('auth.login'))
