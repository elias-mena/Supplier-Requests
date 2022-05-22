# Flask stuff
from flask import (
    Flask,
    render_template,
    flash
)

# Flask extensions
from flask_bootstrap import Bootstrap
from flask_login import LoginManager, current_user
from flask_scss import Scss  # Sass compiler

# User model for the log in
from apps.models import UserModel

# Configuration object
from .config import Config

# Blueprints
from .auth import auth
from .approvers import approvers
from .customers import customers
from .admin import admin

# Db instance
from .db import db
# Object to send emails
from .mail import mail

# Login manager verifies if the user is logged and saves the session
login_manager = LoginManager()
login_manager.login_view = 'auth.login'  # Login view
login_manager.session_protection = "strong"


@login_manager.user_loader  # Request the user before start the app
def load_user(username):
    return UserModel.query(username)


# App Factory
def create_app():
    app = Flask(__name__)

    # Set the config
    app.config.from_object(Config)

    # Register blueprints

    # Blueprints
    app.register_blueprint(auth)
    app.register_blueprint(approvers)
    app.register_blueprint(customers)
    app.register_blueprint(admin)

    # Initialize the extensions

    # Bootstrap for the templates
    Bootstrap(app)

    # Sass for the styles
    Scss(app)

    # Email object initialization
    mail.init_app(app)

    # Db initialization
    db.init_app(app)

    # Login manager
    login_manager.init_app(app)

    # Register error handlers
    register_error_handlers(app)

    app.app_context().push()

    return app


def register_error_handlers(app):
    # 400 - Bad Request
    @app.errorhandler(400)
    def bad_request(e):
        flash('Ocurrió un error ☹')
        context = {
            'user': current_user,
            'message': 'No se puede procesar la solicitud',
            'error': '400'
        }
        return render_template('error.html', **context)

    # 403 - Forbidden
    @app.errorhandler(403)
    def forbidden(e):
        flash('Ocurrió un error ☹')
        context = {
            'user': current_user,
            'message': 'No tienes permisos para acceder a esta página',
            'error': '403'
        }
        return render_template('error.html', **context)

    # 404 - Page Not Found
    @app.errorhandler(404)
    def page_not_found(e):
        flash('Ocurrió un error ☹')
        context = {
            'user': current_user,
            'message': 'La página que buscas no fue encontrada',
            'error': '404'
        }
        return render_template('error.html', **context)

    # 405 - Method Not Allowed
    @app.errorhandler(405)
    def method_not_allowed(e):
        flash('Ocurrió un error ☹')
        context = {
            'user': current_user,
            'message': 'El método que intentas usar no es válido',
            'error': '405'
        }
        return render_template('error.html', **context)

    # 500 - Internal Server Error
    @app.errorhandler(500)
    def server_error(e):
        flash('Ocurrió un error ☹')
        context = {
            'user': current_user,
            'message': 'Error en el servidor',
            'error': '500'
        }
        return render_template('error.html', **context)

