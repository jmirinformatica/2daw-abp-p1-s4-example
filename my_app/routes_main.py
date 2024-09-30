from flask import Blueprint, redirect, url_for, render_template
from .models import Item, Store
from . import db_manager as db

# Blueprint
main_bp = Blueprint(
    "main_bp", __name__, template_folder="templates", static_folder="static"
)

@main_bp.route('/')
def init():
    return redirect(url_for('main_bp.items_list'))

@main_bp.route('/items/list')
def items_list():
    # select amb join que retorna una llista dwe resultats
    items_with_stores = db.session.query(Item, Store).join(Store).order_by(Item.id.asc()).all()
    return render_template('items_list.html', items_with_stores = items_with_stores)

@main_bp.route('/items/read/<int:item_id>')
def items_read(item_id):
    # select amb join i 1 resultat
    (item, store) = db.session.query(Item, Store).join(Store).filter(Item.id == item_id).one()
    
    return render_template('items_read.html', item = item, store = store)
