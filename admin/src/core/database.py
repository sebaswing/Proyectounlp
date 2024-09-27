from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_app(app):

    """
    INicia la base de datos en la aplicación de Flask
    """
    db.init_app(app)
    config(app)
    return app

def config (app):
    """
    Configuración de hooks para la base de datos.
    """

    @app.teardown_appcontext
    def close_session(exception = None):
        db.session.close()

    return app

def reset():
    """
    reset DB
    """

    print ("Eliminando Base de Datos...")
    db.drop_all()
    print("creando base nuevamente...")
    db.create_all()
    print("Proceso finalizado.")