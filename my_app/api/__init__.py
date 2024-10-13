from flask import Blueprint

api_bp = Blueprint('api', __name__)

# necessari per a que es carreguin les rutes
from . import helper_auth, api_items, api_stores, api_tokens, errors
