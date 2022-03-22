# Flask stuff
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager

# User model for the log in
from apps.models import UserModel

# Configuration object
from .config import Config

# Blueprints
from .auth import auth
from .approvers import approvers
from .customers import customers

# Database connection
from .db import db


# Login manager verifies if the user is logged
login_manager = LoginManager()
login_manager.login_view = 'auth.login'  # Login view


@login_manager.user_loader  # Request the user before start the app
def load_user(email):
    return UserModel.query(email)


def create_app():
    app = Flask(__name__)

    # Set the config
    app.config.from_object(Config)

    # Bootstrap for the templates
    bootstrap = Bootstrap(app)

    # Db connection
    db.init_app(app)

    # Request the login
    login_manager.init_app(app)

    # Blueprints
    app.register_blueprint(auth)
    app.register_blueprint(approvers)
    app.register_blueprint(customers)

    yield app
