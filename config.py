from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'), override=True)

class Config:

    # clau secreta per a les sessions guardades a les cookies
    SECRET_KEY = environ.get('SECRET_KEY')
    
    # ruta relativa de la base de dades
    SQLITE_FILE_RELATIVE_PATH = environ.get('SQLITE_FILE_RELATIVE_PATH')
    
    # mostra les sentències SQL generades pel log
    SQLALCHEMY_ECHO = environ.get('SQLALCHEMY_ECHO')
    
    # nivell de log (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    LOGGING_LEVEL = environ.get('LOGGING_LEVEL')