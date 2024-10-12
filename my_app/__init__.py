from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_principal import Principal
from .helper_mail import MailManager
import os

db_manager = SQLAlchemy()
login_manager = LoginManager()
principal_manager =  Principal()
mail_manager = MailManager()

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

    # Inicialitza els plugins
    db_manager.init_app(app)
    login_manager.init_app(app)
    principal_manager.init_app(app)
    mail_manager.init_app(app)

    app.logger.info("Configuració de la base de dades aplicada")

def create_app():
    app = Flask(__name__)

    # Llegeixo la configuració del config.py de l'arrel
    app.config.from_object('config.Config')

    # Configuració de la base de dades
    configure_db(app)

    with app.app_context():
        from . import routes_main, routes_auth, routes_admin
        from .api import api_bp

        # Registra els blueprints
        app.register_blueprint(routes_main.main_bp)
        app.register_blueprint(routes_auth.auth_bp)
        app.register_blueprint(routes_admin.admin_bp)
        
        # Registra el blueprint de l'API
        app.register_blueprint(api_bp, url_prefix='/api/v1.0')

    app.logger.info("Aplicació iniciada")

    return app