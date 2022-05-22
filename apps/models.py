import datetime
# UserMixing implements the methods for flask login
from flask_login import UserMixin

from apps.db import db


class UserModel(UserMixin):
    """
    User model for flask login, to save the current user and its session
    """

    def __init__(self, user_data):
        """
        Builds a user model with the user info we want to save for the current session.

        # Parameter:
            - user_data: User
        """
        self.id = user_data.username
        self.first_name = user_data.first_name
        self.last_name = user_data.last_name
        self.birth_date = user_data.birth_date
        self.rol = user_data.rol
        self.email = user_data.email
        self.password = user_data.password

    @staticmethod
    def query(username):
        """
        This method is call every time flask login request the user.

        # Parameter:
            - email: str
        """
        user = db.session.query(User).filter(User.username == username).first()
        user_data = User(
            username=user.username,
            first_name=user.first_name,
            last_name=user.last_name,
            birth_date=user.birth_date,
            rol=user.rol,
            email=user.email,
            password=user.password,
            status=user.status
        )
        return UserModel(user_data)


# DATABASE MODELS


class UserRol(db.Model):
    """
    Model for the rol of the users, the app will have 3 users, admin, client and approver.
    """
    __tablename__ = 'users_rols'
    __table_args__ = {'extend_existing': True}
    rol_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), nullable=False)
    description = db.Column(db.Text, nullable=False)

    def __init__(self, name: str, description: str):
        """
        Builds a UserRol model.

        # Parameters:
            name:
                - Name of the rol.
            description:
                - Description of what does the rol do.
        """
        self.name = name
        self.description = description


class User(db.Model):
    """
    Model for the users.
    """
    # Method to create the table
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}
    username = db.Column(db.String(15), primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    birth_date = db.Column(db.Date, nullable=False)
    rol = db.Column(db.Integer, db.ForeignKey("users_rols.rol_id"), nullable=False)
    email = db.Column(db.String(40), nullable=False)
    password = db.Column(db.String(150), nullable=False)
    status = db.Column(db.String(1), nullable=False, default='A')

    def __init__(self, username: str, first_name: str, last_name: str, birth_date: datetime.date,
                 rol: int, email: str, password: str, status: str):
        """
        Builds a User model.

        # Parameters:
            username: int
                Username to be identified in the app.
            first_name: str
                - First name of the user
            last_name: str
                - Last name of the user
            birth_date: datetime
                - Date of birthday of the user
            rol: int
                - Reference for the rol of the user.
            email: str
                - Email of the user
            password: str
                - Password to access the app.
            status:
                - User status, can be Active (A), Inactive (I), is A by default.
        """
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.rol = rol
        self.email = email
        self.password = password
        self.status = status


class Request(db.Model):
    """
    Model for the Requests, the requests are done by the client user, and approved or declined by
    the approvers users.
    """
    __tablename__ = 'requests'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    product = db.Column(db.String(30), nullable=False)
    description = db.Column(db.Text, nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    customer = db.Column(db.String(15), nullable=False)
    created_at = db.Column(db.Date, default=datetime.datetime.now())
    status = db.Column(db.String(1), nullable=False, default='P')

    def __init__(self, product: str, description: str, amount: int, customer: str):
        """
        Builds the Request model.

        # Parameters:
            id: int
                - Identification number of the request.
            product: str
                - Name of the requested product.
            description:
                - Detailed description of the product requested.
            amount:
                - Cost of the product requested.
            customer:
                - Username of the client who did the request
            created_at:
                - Timestamp with the exact moment the request was made, is set by default.
            status:
                - Request status, can be Pending (P), Accepted(A) or Declined(D), is pending by default.
        """
        self.product = product
        self.description = description
        self.amount = amount
        self.customer = customer

    def as_dict(self) -> dict:
        """ Returns a dictionary with the history of the request info. """
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class RequestHistory(db.Model):
    """
    Model for the Request History, this table will save all the movements of the requests,
    when and who approved or declined them.
    """
    __tablename__ = 'requests_history'
    __table_args__ = {'extend_existing': True}
    request_id = db.Column(db.Integer, db.ForeignKey("requests.id"), primary_key=True)
    approver = db.Column(db.String(15), db.ForeignKey("users.username"), nullable=False)
    action = db.Column(db.String(1), nullable=False)
    date = db.Column(db.TIMESTAMP, default=datetime.datetime.now())

    def __init__(self, request_id: int, approver: str, action: str):
        """
        Builds a new register for a request history.

        # Parameters:
            request: int
                - Reference for the request_id
            approver:
                - Username of the approver
            action:
                - Action over the request, Accepted (A) or Declined (D)
            date:
                - Timestamp with the exact moment the action was made, is set by default.
        """
        self.request_id = request_id
        self.approver = approver
        self.action = action

    def as_dict(self) -> dict:
        """ Returns a dictionary with the history of the request info. """
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class FullRequestInfo(db.Model):
    """
    This view show us a clear info about the requests.
    """
    __tablename__ = 'full_requests_info'
    __table_args__ = {'extend_existing': True}
    request_id = db.Column(db.Integer, db.ForeignKey("requests.id"), primary_key=True)
    info = db.Column(db.JSON, nullable=False)
    first_approval = db.Column(db.JSON)
    second_approval = db.Column(db.JSON)

    def __init__(self, request_id: int, info: dict, first_approval: dict = None, second_approval: dict = None):
        """
        Builds an object with all the info about the request.

        # Parameters:
            id: int
                - Reference for the request_id
            info: dict
                - Information about the request
            first_approval: dict
                - Information about the first approval
            second_approval: dict
                - Information about the second approval
        """
        self.request_id = request_id
        self.info = info
        self.first_approval = first_approval
        self.second_approval = second_approval


# DATABASE VIEWS


class UserInfo(db.Model):
    """
    This view show us a clear info about the users.
    """
    __tablename__ = 'users_info'
    __table_args__ = {'extend_existing': True}
    username = db.Column(db.String(15), db.ForeignKey("users.username"), primary_key=True)
    first_name = db.Column(db.String(30), db.ForeignKey("users.first_name"))
    last_name = db.Column(db.String(30), db.ForeignKey("users_rols.last_name"))
    birth_date = db.Column(db.Date, db.ForeignKey("users.birth_date"))
    rol = db.Column(db.String(30), db.ForeignKey("users_rols.name"))
    email = db.Column(db.String(40), db.ForeignKey("users.email"))
    status = db.Column(db.String(1), db.ForeignKey("users.status"))
