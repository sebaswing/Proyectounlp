from os import fstat
from flask import flash, redirect, render_template, request, url_for
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

@bp.get("/<int:id>/edit")
def edit(id):
    user = auth.get_user(id)

    return render_template("users/edit.html", user=user)
        

@bp.post("/<int:id>/update")
def update(id):
    params= request.form.copy()

    if "avatar" in request.files:
        file = request.files["avatar"]
        client = current_app.storage.client
        size = fstat(file.fileno()).st_size
        # ulid= u.new() -> para generar una clave unica y sumarselo al filename, asi no se pisa el archivo anterior

        client.put_object(
            "grupo00",
            file.filename,  
            file,
            size,
            content_type=file.content_type
        )

        params["avatar"]=file.filename
        # print(avatar)

    auth.update_user(id,**params)
    flash("Usuario actualizado correctamente","success")

    return redirect(url_for("users.index"))