from functools import wraps
from flask import session, abort

def is_authenticated(session):
    return session.get("user") is not None

def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not is_authenticated(session):
            return abort(401)
        return func(*args, **kwargs)  # Aquí llamamos a la función original
    return wrapper
