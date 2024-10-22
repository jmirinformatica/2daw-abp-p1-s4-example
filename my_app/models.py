from . import db_manager as db
from flask_login import UserMixin
from .mixins import SerializableMixin, BaseMixin
from datetime import timedelta, timezone, datetime
import secrets
from werkzeug.security import check_password_hash

# Taula items
class Item(db.Model, SerializableMixin, BaseMixin):
    __tablename__ = "items"
    id = db.Column(db.Integer, primary_key=True)
    store_id = db.Column(db.Integer, db.ForeignKey("stores.id"), nullable=False)
    nom = db.Column(db.String, nullable=False)
    unitats = db.Column(db.Integer, nullable=False)

    store = db.relationship("Store", back_populates="items", lazy="joined")

# Taula stores
class Store(db.Model, SerializableMixin, BaseMixin):
    __tablename__ = "stores"
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String, nullable=False)

    items = db.relationship("Item", back_populates="store", lazy="select")

# Taula users
class User(UserMixin, db.Model, SerializableMixin, BaseMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    role = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    auth_token = db.Column(db.String, nullable=True)
    auth_token_expiration = db.Column(db.DateTime, nullable=True)

    # Class variable from SerializableMixin
    exclude_attr = ['password', 'auth_token', 'auth_token_expiration']

    # la identificació de l'usuari es basa en el seu email
    def get_id(self):
        return self.email
    
    def check_password(self, plain_text_password):
        return check_password_hash(self.password, plain_text_password)
    
    def get_auth_token(self, expires_in=3600):
        now = datetime.now(timezone.utc)
        if self.auth_token and self.auth_token_expiration.replace(tzinfo=timezone.utc) > now + timedelta(seconds=60):
            return self.auth_token
        self.auth_token = secrets.token_hex(16)
        self.auth_token_expiration = now + timedelta(seconds=expires_in)
        self.save()
        return self.auth_token

    def revoke_auth_token(self):
        self.auth_token_expiration = None
        self.auth_token = None
        self.save()
        
    @staticmethod
    def check_auth_token(some_token):
        user = db.session.query(User).filter(User.auth_token == some_token).one_or_none()
        if user is None or user.auth_token_expiration is None or user.auth_token is None:
            # no token
            return None
        elif user.auth_token_expiration.replace(tzinfo=timezone.utc) < datetime.now(timezone.utc):
            # expired token
            return None
        return user