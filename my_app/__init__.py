from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os

db_manager = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    # Construct the core app object
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "Valor aleatori molt llarg i super secret"

    # ruta absoluta d'aquesta carpeta
    basedir = os.path.abspath(os.path.dirname(__file__)) 

    # paràmetre que farà servir SQLAlchemy per a connectar-se
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + basedir + "/../database.db"
    # mostre als logs les ordres SQL que s'executen
    app.config["SQLALCHEMY_ECHO"] = True

    # Inicialitza els plugins
    login_manager.init_app(app)
    db_manager.init_app(app)

    with app.app_context():
        from . import routes_main, routes_auth

        # Registra els blueprints
        app.register_blueprint(routes_main.main_bp)
        app.register_blueprint(routes_auth.auth_bp)

    app.logger.info("Aplicació iniciada")

    return app