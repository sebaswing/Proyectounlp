from flask import Flask
from flask import render_template
from src.web.controllers.issues import bp as issues_bp
from src.web.handlers import error

def create_app(env="development", static_folder="../../static"):
    app = Flask(__name__,static_folder = static_folder)

    @app.route("/")
    def home():
        return  render_template("home.html") #"Hola Mundo!" se levanta la app.
    
    @app.route("/about")
    def about():
        return render_template("about.html")

    app.register_blueprint(issues_bp)

    app.register_error_handler(404, error.error_not_found)
    
    return app
