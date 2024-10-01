from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db_manager = SQLAlchemy()

def configure_db(app):
    # Ruta absoluta d'on està aquest fitxer __init__.py
    basedir = os.path.abspath(os.path.dirname(__file__)) 

    # TODO: llegir de la configuració
    sqlite_file_path = basedir + "/../sqlite/database.db"
    app.logger.info("Database: " + sqlite_file_path)

    # paràmetre que farà servir SQLAlchemy per a connectar-se a la base de dades
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + sqlite_file_path

    # mostre als logs les ordres SQL que s'executen
    # TODO: llegir de la configuració
    app.config["SQLALCHEMY_ECHO"] = True

    # Inicialitza SQLAlchemy
    db_manager.init_app(app)

    app.logger.info("Configuració de la base de dades aplicada")

def create_app():
    app = Flask(__name__)

    # Llegeixo la configuració del config.py de l'arrel
    app.config.from_object('config.Config')

    # Configuració de la base de dades
    configure_db(app)

    with app.app_context():
        from . import routes_main, routes_auth

        # Registra els blueprints
        app.register_blueprint(routes_main.main_bp)
        app.register_blueprint(routes_auth.auth_bp)

    app.logger.info("Aplicació iniciada")

    return app