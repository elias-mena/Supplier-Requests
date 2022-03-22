class Config:
    """
    We will configure the app with this class
    """

    # Flask config
    FLASK_ENV = 'development'
    DEBUG = False
    TESTING = False
    WTF_CSRF_ENABLED = True
    SECRET_KEY = 'SUPER SECRET'
    CSRF_ENABLED = True  # Protection against *Cross-site Request Forgery (CSRF)*
    CSRF_SESSION_KEY = "SUPER SECRET"  # Secret key for signing the data.

    # Database config
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:admin@localhost/supplier-requests'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Email smtp server config
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 465
    MAIL_USERNAME = 'mail@gmail.com'
    MAIL_DEFAULT_SENDER = 'mail@gmail.com'
    MAIL_PASSWORD = 'Password'
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_SUPPRESS_SEND = False


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:password@localhost/supplier-requests"


class TestingConfig(Config):
    TESTING = True
    WTF_CSRF_ENABLED = False
    MAIL_SUPPRESS_SEND = True
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:password@localhost/supplier-requests"


class ProductionConfig(Config):
    FLASK_ENV = 'production'
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:password@localhost/supplier-requests"


