from datetime import datetime, timedelta
from typing import List

from flask_login import current_user

# Database instance
from apps.db import db

# Models
from apps.models import (
    User,
    UserInfo,
    Request,
    RequestHistory,
    FullRequestInfo
)


# Inserts


def insert_user(user: User):
    """Inserts a new user into the database"""
    db.session.add(user)
    db.session.commit()


def insert_request(request: Request):
    """Inserts a new request into the database"""
    db.session.add(request)
    db.session.commit()


def insert_request_history(history: RequestHistory):
    """Inserts a new request history into the database"""
    db.session.add(history)
    db.session.commit()


def insert_full_request_info(request_history: FullRequestInfo):
    """Inserts a new request history into the database"""
    db.session.add(request_history)
    db.session.commit()


# Updates

# Users


def update_user_email(user: User):
    """Updates the user email"""
    db_user: User = get_user(user.username)
    db_user.email = user.email
    db.session.commit()


def update_user_password(user: User):
    """Updates the user password"""
    db_user: User = get_user(user.username)
    db_user.password = user.password
    db.session.commit()


def update_user_name(user: User):
    """Updates the user's name"""
    db_user: User = get_user(user.username)
    db_user.first_name = user.first_name
    db_user.last_name = user.last_name
    db.session.commit()


def update_user_birth_date(user: User):
    """Updates the user birthdate"""
    db_user: User = get_user(user.username)
    db_user.birth_date = user.birth_date
    db.session.commit()


def update_user_state(user: User):
    """Updates the user state"""
    db_user: User = get_user(user.username)
    db_user.status = user.status
    db.session.commit()


def update_user_rol(user: User):
    """Updates the user rol"""
    db_user: User = get_user(user.username)
    db_user.rol = user.rol
    db.session.commit()

    # Requests


def update_request_status(request: Request):
    """Updates the request status (Pending, Accepted, Declined)"""
    db_request: Request = Request.query.get(request.id)
    db_request.status = request.status

    db_info: FullRequestInfo = FullRequestInfo.query.get(request.id)
    # Convert the request in a JSON
    info = db_request.as_dict()
    # # Cast the date to string for the JSON format
    info["created_at"] = str(info["created_at"])
    db_info.info = info
    db.session.commit()


def update_first_approval_info(history: RequestHistory):
    """"Updates the request full info"""
    db_info: FullRequestInfo = FullRequestInfo.query.get(history.request_id)
    # Object to json
    history = history.as_dict()
    # # Cast the date to string for the JSON format
    history["date"] = history["date"].strftime('Fecha: %m/%d/%Y, Hora: %H:%M:%S')
    db_info.first_approval = history
    db.session.commit()


def update_second_approval_info(history: RequestHistory):
    """"Updates the request full info"""
    db_info: FullRequestInfo = FullRequestInfo.query.get(history.request_id)
    # Object to json
    history = history.as_dict()
    # # Cast the date to string for the JSON format
    history["date"] = history["date"].strftime('Fecha: %m/%d/%Y, Hora: %H:%M:%S')
    db_info.second_approval = history
    db.session.commit()


# Deletes


def delete_user(user: User):
    """Deletes the user with the given data"""
    db.session.delete(user)
    db.session.commit()


# Queries

# Users

def get_users() -> List[UserInfo]:
    """
    Returns a list with all the users' data:
        - username: str
        - first_name: str
        - last_name: str
        - birth_date: str
        - rol: str
        - email: str
        - status: str
    """
    return UserInfo.query.all()


def get_user(username: str) -> User:
    """
    Returns the user with the given username:
        - username: str
        - first_name: str
        - last_name: str
        - birth_date: str
        - rol: str
        - email: str
        - status: str
    """
    return User.query.filter_by(username=username).first()


def get_user_mail(username: str) -> User:
    """
    Returns the email of the given user
    """
    return User.query.filter_by(username=username).first().email


# Requests


def get_requests() -> List[Request]:
    """
    Returns a list with all the requests' data:
        - request_id: int
        - product: str
        - description: str
        - amount: int
        - customer: str
        - created_at: datetime
        - status: str
    """
    return Request.query.all()


def get_pending_requests() -> List[Request]:
    """
    Returns all the pending requests' data:
        - request_id: int
        - product: str
        - description: str
        - amount: int
        - customer: str
        - created_at: datetime
        - status: str
    """
    return Request.query.filter_by(status="P").all()


def get_accepted_requests() -> List[Request]:
    """
    Returns all the accepted requests' data:
        - request_id: int
        - product: str
        - description: str
        - amount: int
        - customer: str
        - created_at: datetime
        - status: str
    """
    return Request.query.filter_by(status="A").all()


def get_declined_requests() -> List[Request]:
    """
    Returns all the declined requests data:
        - request_id: int
        - product: str
        - description: str
        - amount: int
        - customer: str
        - created_at: datetime
        - status: str
    """
    return Request.query.filter_by(status="D").all()


def get_request(request_id: int) -> Request:
    """
    Returns the request with the given id
        - id: int
        - product: str
        - description: str
        - amount: int
        - customer: str
        - created_at: datetime
        - status: str
    """
    return Request.query.get_or_404(request_id)


# Requests Histories


def get_requests_history() -> List[RequestHistory]:
    """
    Returns a list with all the requests' histories data:
        - request_id: int
        - approver: str
        - action: str
        - date: datetime
    """
    return RequestHistory.query.all()


def get_request_history(request_id: int) -> List[RequestHistory]:
    """
    Returns a list with all the requests' histories data with the given id:
        - request_id: int
        - approver: str
        - action: str
        - date: datetime
    """
    return RequestHistory.query.filter_by(request_id=request_id).all()


def get_request_history_approver(request_id: int, approver: str) -> RequestHistory:
    """
    Returns a history of the given request if was managed for the given approver:
        - request_id: int
        - approver: str
        - action: str
        - date: datetime
    """
    return RequestHistory.query.filter_by(request_id=request_id, approver=approver).first()


# Full Requests Info

def get_client_requests(username: str) -> List[FullRequestInfo]:
    """
    Returns the full request information of all the requests made for the given client:
        - request_id: int
        - info: Request (json)
        - first_approval: RequestHistory (json)
        - second_approval: RequestHistory (json)
    """
    requests = FullRequestInfo.query.all()
    return [request for request in requests if request.info["customer"] == username]


def get_approver_requests(username: str) -> List[FullRequestInfo]:
    """
    Returns the full request information of all the requests managed for the given approver:
        - request_id: int
        - info: Request (json)
        - first_approval: RequestHistory (json)
        - second_approval: RequestHistory (json)
    """
    requests = FullRequestInfo.query.all()
    approver_requests = []
    for request in requests:
        if request.first_approval is not None and request.first_approval["approver"] == username:
            approver_requests.append(request)
        if request.second_approval is not None and request.second_approval["approver"] == username:
            approver_requests.append(request)
    return approver_requests


def get_approver_pending_requests(rol: int) -> List[FullRequestInfo]:
    """
    Returns the full request information of all the requests managed for the given approver:
        - request_id: int
        - info: Request (json)
        - first_approval: RequestHistory (json)
        - second_approval: RequestHistory (json)
    """
    pending_requests: List[Request] = get_pending_requests()
    requests_info: List[FullRequestInfo] = [get_request_info(request.id) for request in pending_requests]
    approver_requests = []

    if rol == 3:
        approver_requests = [request for request in requests_info if request.first_approval is None]
    if rol == 4:
        approver_requests = [request for request in requests_info if 1 < request.info["amount"] < 100000
                             and request.first_approval is not None]
    if rol == 5:
        approver_requests = [request for request in requests_info if 100000 < request.info["amount"] < 1000000
                             and request.first_approval is not None]
    if rol == 6:
        approver_requests = [request for request in requests_info if 1000000 < request.info["amount"] < 10000000
                             and request.first_approval is not None]
    return approver_requests


def get_request_info(request_id: int) -> FullRequestInfo:
    """
    Returns the full request information (Request info and Request History) with the given id
        - request_id: int
        - info: Request (json)
        - first_approval: RequestHistory (json)
        - second_approval: RequestHistory (json)
    """
    return FullRequestInfo.query.get(request_id)


def get_requests_by_month(months: int):
    """
    Returns the request information of all the requests within the given month
        - request_id: int
        - info: Request (json)
        - first_approval: RequestHistory (json)
        - second_approval: RequestHistory (json)
    """
    requests: List[FullRequestInfo] = get_approver_requests(current_user.id)
    today = datetime.now()
    return [request for request in requests
            if
            (today - timedelta(days=months * 30)) < datetime.strptime(request.info["created_at"], '%Y-%m-%d') < today]


def get_requests_by_status(status: str):
    """
    Returns the request information of all the requests with the given status
        - request_id: int
        - info: Request (json)
        - first_approval: RequestHistory (json)
        - second_approval: RequestHistory (json)
    """
    requests: List[FullRequestInfo] = get_approver_requests(current_user.id)
    return [request for request in requests if request.info["status"] == status]
