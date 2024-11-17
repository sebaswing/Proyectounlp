import logging
from flask import Flask
from flask_session import Session
from src.core.bcrypt import bcrypt
from src.core.config import config
from src.web import routes,helpers
from src.web.handlers.auth import  is_authenticated
from src.web.handlers.auth import  check_permissions
from src.web.handlers import error
from src.web import commands
from src.core import database
from src.web.storage import storage
from dotenv import load_dotenv
from flask_cors import CORS
import os

load_dotenv()
session = Session()

# logging.basicConfig()
# logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)

def create_app(env="development", static_folder="../../static"):
    app = Flask(__name__,static_folder = static_folder)
    #load config
    app.config.from_object(config[env])
    #print(app.config)
    #Init database
    database.init_app(app)
    #init session
    session.init_app(app)
    #init bcrypt
    bcrypt.init_app(app)    
    #---- se procede a retirar esta sección de rutas para llevarlo a routes
    routes.register(app)
    #------
    #registra el obeto stortage de minIO
    storage.init_app(app)

    #register CORS
    CORS(app)

    #register error handlers
    app.register_error_handler(404, error.error_not_found)
    app.register_error_handler(401, error.unauthorized)
    app.register_error_handler(403, error.Forbidden)

    #register functions on jinja
    app.jinja_env.globals.update(is_authenticated = is_authenticated)
    app.jinja_env.globals.update(check_permissions = check_permissions)
    app.jinja_env.globals.update(avatar_url = helpers.avatar_url)
    #se remueven los comandos para pasarlos a commands.py 
    commands.register (app)   
    
    return app
