from flask import render_template
from flask import current_app
from flask import Blueprint
from src.core import auth  
from src.web.handlers.auth import login_required

bp = Blueprint("users",__name__,url_prefix="/usuarios")

@bp.get("/")
@login_required
def index():

    #if not is_authenticated(session): se elimina por el decorator login_required
    #    return abort(401)
    users=auth.list_users()

    #raise Exception ("Error de prueba") levantar una excepcion.
    if not users:
        current_app.logger.warning("La lista de usuarios está vacía o es nula")
    
    
    return render_template("users/index.html", users=users)

