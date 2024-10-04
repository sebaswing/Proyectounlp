from flask import render_template
from flask import Blueprint
from flask import session
from flask import abort
from src.core import auth  
from src.web.handlers.auth import is_authenticated

bp = Blueprint("users",__name__,url_prefix="/usuarios")

@bp.get("/")
def index():

    if not is_authenticated(session):
        return abort(401)
    users=auth.list_users()

    #raise Exception ("Error de prueba") levantar una excepcion.

    return render_template("users/index.html", users=users)

