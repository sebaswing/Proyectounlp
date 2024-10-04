from src.core import database
from src.core.seeds import run as run_seeds # acá lo que hago es renombrarla para que el nombre quede más entedible al leer


def register(app):
    @app.cli.command(name="reset-db")
    def reset_db():
        database.reset()

    @app.cli.command(name="seeds-db")
    def seeds_deb():
        run_seeds()