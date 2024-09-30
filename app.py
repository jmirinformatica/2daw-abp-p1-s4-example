from flask import Flask, redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Llegeixo la configuració del config.py de l'arrel
app.config.from_object('config.Config')

# ruta absoluta d'aquesta carpeta
basedir = os.path.abspath(os.path.dirname(__file__)) 

# paràmetre que farà servir SQLAlchemy per a connectar-se
# TODO: llegir de la configuració
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + basedir + "/sqlite/database.db"

# mostre als logs les ordres SQL que s'executen
# TODO: llegir de la configuració
app.config["SQLALCHEMY_ECHO"] = True

# Inicio SQLAlchemy
db = SQLAlchemy()
db.init_app(app)

# Taula items
class Item(db.Model):
    __tablename__ = "items"
    id = db.Column(db.Integer, primary_key=True)
    store_id = db.Column(db.Integer, db.ForeignKey("stores.id"), nullable=False)
    nom = db.Column(db.String, nullable=False)
    unitats = db.Column(db.Integer, nullable=False)

# Taula stores
class Store(db.Model):
    __tablename__ = "stores"
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String, nullable=False)

@app.route('/')
def init():
    return redirect(url_for('items_list'))

@app.route('/items/list')
def items_list():
    # select amb join que retorna una llista dwe resultats
    items_with_stores = db.session.query(Item, Store).join(Store).order_by(Item.id.asc()).all()
    return render_template('items_list.html', items_with_stores = items_with_stores)

@app.route('/items/read/<int:item_id>')
def items_read(item_id):
    # select amb join i 1 resultat
    (item, store) = db.session.query(Item, Store).join(Store).filter(Item.id == item_id).one()
    
    return render_template('items_read.html', item = item, store = store)
