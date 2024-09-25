from flask import render_template
from flask import Blueprint
from src.core import board  

bp = Blueprint("issues",__name__,url_prefix="/consultas")

@bp.get("/")
def index():
    issues=board.list_issues()

    #raise Exception ("Error de prueba") levantar una excepcion.

    return render_template("issues/index.html", issues=issues)

