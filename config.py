from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'), override=True)

class Config:
    SECRET_KEY = environ.get('SECRET_KEY')

    SQLITE_FILE_RELATIVE_PATH = environ.get('SQLITE_FILE_RELATIVE_PATH')

    SQLALCHEMY_ECHO = environ.get('SQLALCHEMY_ECHO')

    LOGGING_LEVEL = environ.get('LOGGING_LEVEL')
    LOGGING_FORMAT = environ.get('LOGGING_FORMAT')
    LOGGING_FILE = environ.get('LOGGING_FILE', '') # si no hi ha cap valor, retorna un string buit
