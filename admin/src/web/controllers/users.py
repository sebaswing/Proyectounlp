from flask import render_template
from flask import current_app
from flask import Blueprint
from src.core import auth  
from src.web.handlers.auth import login_required, check #check_permissions
from flask import session,abort


bp = Blueprint("users",__name__,url_prefix="/usuarios")

@bp.get("/")
@login_required # es importante el orden de ubicación 
@check("user_index")# es importante el orden de ubicación 
def index():

    #if not is_authenticated(session): se elimina por el decorator login_required
    #    return abort(401)
    users=auth.list_users()

    # #raise Exception ("Error de prueba") levantar una excepcion.
    # if not check_permissions(session,"user_index"):
    #     return abort(403)
    
    
    return render_template("users/index.html", users=users)

