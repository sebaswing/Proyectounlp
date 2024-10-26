from flask import render_template
from flask import Blueprint
from src.web.handlers.auth import login_required, check #check_permissions
from flask import session,abort
from src.core import board  

bp = Blueprint("issues",__name__,url_prefix="/consultas")

@bp.get("/")
@login_required # es importante el orden de ubicación
@check("issue_index") # es importante el orden de ubicación
def index():

    # if not check_permissions(session,"issue_index"):
    #     return abort(403) se eliminan por el decorator check_permissions
    
    issues=board.list_issues()

    #raise Exception ("Error de prueba") levantar una excepcion.

    return render_template("issues/index.html", issues=issues)

