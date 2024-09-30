from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
import logging

db_manager = SQLAlchemy()

def configure_logging(app):
    log_level = app.config["LOGGING_LEVEL"]
    
    # Possem el log_level a tots els loggers: https://stackoverflow.com/a/55490202
    loggers = [logging.getLogger(name) for name in logging.root.manager.loggerDict]
    for logger in loggers:
        logger.setLevel(log_level)

    app.logger.info("Configuració de logging aplicada")

def configure_db(app):
    # Ruta absoluta d'on està aquest fitxer __init__.py
    basedir = os.path.abspath(os.path.dirname(__file__)) 

    sqlite_file_relative_path = app.config['SQLITE_FILE_RELATIVE_PATH']
    app.logger.info("Database: " + sqlite_file_relative_path)

    # paràmetre que farà servir SQLAlchemy per a connectar-se a la base de dades
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + basedir + "/../" + sqlite_file_relative_path

    # Inicialitza SQLAlchemy
    db_manager.init_app(app)

    app.logger.info("Configuració de la base de dades aplicada")

def create_app():
    app = Flask(__name__)

    # Llegeixo la configuració del config.py de l'arrel
    app.config.from_object('config.Config')

    # Configuració del logging
    configure_logging(app)

    # Configuració de la base de dades
    configure_db(app)

    with app.app_context():
        from . import routes_main

        # Registra els blueprints
        app.register_blueprint(routes_main.main_bp)

    app.logger.info("Aplicació iniciada")

    return app