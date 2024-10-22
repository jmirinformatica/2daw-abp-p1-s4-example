from . import api_bp
from .helper_auth import basic_auth, token_auth
from .helper_json import json_response
from flask import current_app

logger = current_app.logger

@api_bp.route('/tokens', methods=['POST'])
@basic_auth.login_required
def get_token():
    user_id = basic_auth.current_user().id
    token = basic_auth.current_user().get_auth_token()
    logger.debug("Token:" + token)
    return json_response({'id': user_id, 'token': token})

@api_bp.route('/tokens', methods=['DELETE'])
@token_auth.login_required
def revoke_token():
    user_id = basic_auth.current_user().id
    token_auth.current_user().revoke_auth_token()
    return json_response({'id': user_id})