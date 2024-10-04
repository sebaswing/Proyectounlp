from flask import Flask
from flask import render_template
from flask_session import Session
from src.core.bcrypt import bcrypt
from src.web.config import config
from src.web.controllers.issues import bp as issues_bp
from src.web.controllers.auth import bp as auth_bp
from src.web.controllers.users import bp as users_bp
from src.web.handlers.auth import is_authenticated
from src.web.handlers import error
from src.core import database
from src.core.seeds import run as run_seeds # acá lo que hago es renombrarla para que el nombre quede más entedible al leer

session = Session()

def create_app(env="development", static_folder="../../static"):
    app = Flask(__name__,static_folder = static_folder)
    app.config.from_object(config[env])
    #print(app.config)

    database.init_app(app)

    session.init_app(app)
    bcrypt.init_app(app)

    @app.route("/")
    def home():
        return  render_template("home.html") #"Hola Mundo!" se levanta la app.
    
    @app.route("/about")
    def about():
        return render_template("about.html")

    app.register_blueprint(issues_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(users_bp)

    #register error handlers
    app.register_error_handler(404, error.error_not_found)
    app.register_error_handler(401, error.unauthorized)

    #register functions on jinja
    app.jinja_env.globals.update(is_authenticated = is_authenticated)

    @app.cli.command(name="reset-db")
    def reset_db():
        database.reset()

    @app.cli.command(name="seeds-db")
    def seeds_deb():
        run_seeds()

    
    return app
