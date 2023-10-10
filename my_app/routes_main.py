from flask import Blueprint, redirect, url_for, render_template, request
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

@main_bp.route('/items/update/<int:item_id>',methods = ['POST', 'GET'])
def items_update(item_id):
    # select amb 1 resultat
    item = db.session.query(Item).filter(Item.id == item_id).one()
    
    if request.method == 'GET':
        # select que retorna una llista de resultats
        stores = db.session.query(Store).order_by(Store.id.asc()).all()
        return render_template('items_update.html', item = item, stores = stores)
    else: # POST
        nom = request.form['nom']
        unitats = int(request.form['unitats']) # es text, el passo a enter
        store_id = int(request.form['store_id']) # es text, el passo a enter

        # actualitzo els valors de l'item
        item.nom = nom
        item.unitats = unitats
        item.store_id = store_id

        # update!
        db.session.add(item)
        db.session.commit()

        # https://en.wikipedia.org/wiki/Post/Redirect/Get
        return redirect(url_for('main_bp.items_read', item_id = item_id))

@main_bp.route('/items/create', methods = ['POST', 'GET'])
def items_create(): 
    if request.method == 'GET':
        # select que retorna una llista de resultats
        stores = db.session.query(Store).order_by(Store.id.asc()).all()
        return render_template('items_create.html', stores = stores)
    else: # POST
        nom = request.form['nom']
        unitats = int(request.form['unitats']) # es text, el passo a enter
        store_id = int(request.form['store_id']) # es text, el passo a enter

        # he de crear un nou item
        nou_item = Item()
        nou_item.nom  = nom
        nou_item.unitats  = unitats
        nou_item.store_id = store_id

        # insert!
        db.session.add(nou_item)
        db.session.commit()

        # https://en.wikipedia.org/wiki/Post/Redirect/Get
        return redirect(url_for('main_bp.items_list'))

@main_bp.route('/items/read/<int:item_id>')
def items_read(item_id):
    # select amb join i 1 resultat
    (item, store) = db.session.query(Item, Store).join(Store).filter(Item.id == item_id).one()
    
    return render_template('items_read.html', item = item, store = store)

@main_bp.route('/items/delete/<int:item_id>',methods = ['GET', 'POST'])
def items_delete(item_id):
    # select amb 1 resultat
    item = db.session.query(Item).filter(Item.id == item_id).one()

    if request.method == 'GET':
        return render_template('items_delete.html', item = item)
    else: # POST
        # delete!
        db.session.delete(item)
        db.session.commit()

        return redirect(url_for('main_bp.items_list'))