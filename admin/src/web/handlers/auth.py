from functools import wraps
from flask import session
from flask import abort

def is_authenticated(session):
    return session.get("user") is not None

def login_required(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        if not is_authenticated(session):
            return abort(401)
        return(*args,*kwargs)
    return wrapper