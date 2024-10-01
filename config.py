from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

class Config:

    # clau secreta per a les sessions guardades a les cookies
    SECRET_KEY = environ.get('SECRET_KEY')

    MAIL_SENDER_NAME = environ.get('MAIL_SENDER_NAME')
    MAIL_SENDER_ADDR = environ.get('MAIL_SENDER_ADDR')
    MAIL_SENDER_PASSWORD = environ.get('MAIL_SENDER_PASSWORD')
    MAIL_SMTP_SERVER = environ.get('MAIL_SMTP_SERVER')
    MAIL_SMTP_PORT = int(environ.get('MAIL_SMTP_PORT'))

    CONTACT_ADDR = environ.get('CONTACT_ADDR')

    EXTERNAL_URL = environ.get('EXTERNAL_URL')