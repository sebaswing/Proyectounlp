from functools import wraps
from flask import session, abort
from core import auth


def is_authenticated(session):
    return session.get("user") is not None

def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not is_authenticated(session):
            return abort(401)
        return func(*args, **kwargs)  # Aquí llamamos a la función original
    return wrapper

def check(permission):

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if not check_permissions(session, permission):
                return abort(403)
            return func(*args, **kwargs)
        return wrapper
    return decorator


def check_permissions(session, permission):
    user_email = session.get("user")
    user = auth.find_user_by_email_and_password(user_email)
    permissions = auth.get_permissions(user)

    return  user is not None and permission in permissions

