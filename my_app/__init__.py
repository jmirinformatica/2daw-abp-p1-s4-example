from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
import logging
db_manager = SQLAlchemy()

def configure_logging(app):
    # treu tots els handlers
    del app.logger.handlers[:]
    # https://docs.python.org/3/library/logging.html#logging.Logger.propagate
    app.logger.propagate = False

    log_level = app.config["LOGGING_LEVEL"]
    #https://stackoverflow.com/a/55490202
    loggers = [logging.getLogger(name) for name in logging.root.manager.loggerDict]
    for logger in loggers:
        logger.setLevel(log_level)

    log_format = app.config["LOGGING_FORMAT"]
    log_file = app.config["LOGGING_FILE"]

    # afegeixo un handler propi
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(logging.Formatter(log_format))
    app.logger.addHandler(console_handler)

    if log_file:
        file_handler = logging.FileHandler("app.log")
        file_handler.setFormatter(logging.Formatter(log_format))
        app.logger.addHandler(file_handler)

    app.logger.info("Configuració de logging aplicada")

def configure_db(app):
    # ruta absoluta d'aquesta carpeta
    basedir = os.path.abspath(os.path.dirname(__file__)) 

    # paràmetre que farà servir SQLAlchemy per a connectar-se
    sqlite_file_relative_path = app.config['SQLITE_FILE_RELATIVE_PATH']
    app.logger.info("Database: " + sqlite_file_relative_path)

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