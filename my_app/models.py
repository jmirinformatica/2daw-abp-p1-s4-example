from . import db_manager as db
from flask_login import UserMixin
from .mixins import SerializableMixin, BaseMixin

# Taula items
class Item(db.Model, SerializableMixin, BaseMixin):
    __tablename__ = "items"
    id = db.Column(db.Integer, primary_key=True)
    store_id = db.Column(db.Integer, db.ForeignKey("stores.id"), nullable=False)
    nom = db.Column(db.String, nullable=False)
    unitats = db.Column(db.Integer, nullable=False)

# Taula stores
class Store(db.Model, SerializableMixin, BaseMixin):
    __tablename__ = "stores"
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String, nullable=False)

# Taula users
class User(UserMixin, db.Model, SerializableMixin, BaseMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    role = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)

    # Class variable from SerializableMixin
    exclude_attr = ['password']

    # la identificació de l'usuari es basa en el seu email
    def get_id(self):
        return self.email