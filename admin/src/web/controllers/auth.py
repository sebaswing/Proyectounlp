from flask import Blueprint
from flask import render_template
from flask import request
from flask import flash
from flask import redirect
from flask import url_for
from flask import session
from src.core import auth


bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.get("/")
def login():
    return render_template("auth/login.html")

@bp.post("/authenticate")
def authenticate():
    params= request.form

    #user = auth.find_user_by_email_and_password(params["email"],params["password"])
    user= auth.check_user(params["email"],params["password"])

    if not user:
        flash("Usuario o Contraseña incorrecta", "error")

        return redirect(url_for("auth.login"))
    
    session["user"]=user.email
    flash ("Inicio de sesión iniciado correctamente","success")
    return redirect(url_for("issues.index"))

@bp.get("/logout")
def logout():
    pass