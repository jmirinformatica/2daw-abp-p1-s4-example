from . import api_bp
from .errors import not_found, bad_request
from ..models import Item, Store
from .helper_json import json_request, json_response
from flask import current_app, request
from .. import db_manager as db

# List
@api_bp.route('/items', methods=['GET'])
def get_items():
    search = request.args.get('search')
    if search:
        # Filter using query param
        my_filter = Item.nom.like('%' + search + '%')
        items = db.session.query(Item).filter(my_filter).order_by(Item.id.asc()).all()
    else:
        # No filter
        items = db.session.query(Item).order_by(Item.id.asc()).all()
    data = Item.to_dict_collection(items)
    return json_response(data)

# Read
@api_bp.route('/items/<int:id>', methods=['GET'])
def get_item(id):
    item = db.session.query(Item).filter(Item.id == id).one_or_none()
    if item:
        # Serialize data
        data = item.to_dict(max_levels=1)
        return json_response(data)
    else:
        current_app.logger.debug("Item {} not found".format(id))
        return not_found("Item not found")

# Create
@api_bp.route('/items', methods=['POST'])
def create_item():
    try:
        data = json_request(['nom', 'store_id', 'unitats'])
    except Exception as e:
        current_app.logger.debug(e)
        return bad_request(str(e))
    else:
        item = Item.create(**data)
        current_app.logger.debug("CREATED item: {}".format(item.to_dict()))
        return json_response(item.to_dict(), 201)

# Update
@api_bp.route('/items/<int:id>', methods=['PUT'])
def update_item(id):
    item = db.session.query(Item).filter(Item.id == id).one_or_none()
    if item:
        try:
            data = json_request(['nom', 'store_id', 'unitats'], False)
        except Exception as e:
            current_app.logger.debug(e)
            return bad_request(str(e))
        else:
            item.update(**data)
            current_app.logger.debug("UPDATED item: {}".format(item.to_dict()))
            return json_response(item.to_dict())
    else:
        current_app.logger.debug("Item {} not found".format(id))
        return not_found("Item not found")

# Delete
@api_bp.route('/items/<int:id>', methods=['DELETE'])
def delete_item(id):
    item = db.session.query(Item).filter(Item.id == id).one_or_none()
    if item:
        item.delete()
        current_app.logger.debug("DELETED item: {}".format(id))
        return json_response(item.to_dict())
    else:
        current_app.logger.debug("Item {} not found".format(id))
        return not_found("Item not found")