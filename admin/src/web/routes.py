from flask import render_template
from src.web.controllers.issues import bp as issues_bp
from src.web.controllers.auth import bp as auth_bp
from src.web.controllers.users import bp as users_bp
from src.web.api.issues import bp as issues_api_bp

def register(app):
#register routes
    @app.route("/")
    def home():
        return  render_template("home.html") #"Hola Mundo!" se levanta la app.
    
    @app.route("/about")
    def about():
        return render_template("about.html")

    #Controllers
    app.register_blueprint(issues_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(users_bp)

    #Api
    app.register_blueprint(issues_api_bp)
