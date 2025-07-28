from sqlalchemy.orm import validates, relationship
from sqlalchemy.ext.hybrid import hybrid_property
from config import db, bcrypt
from datetime import datetime

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String, unique=True, nullable=True)
    _password_hash = db.Column(db.String, nullable=True)
    role = db.Column(db.String, default="user")

    items_reported = relationship('Item', backref='reporter',
        foreign_keys='Item.reporter_id', cascade='all, delete-orphan')
    comments = relationship('Comment', backref='user', cascade='all, delete-orphan')
    images = relationship('Image', backref='uploader', cascade='all, delete-orphan')

    def __repr__(self):
        return f"<User #{self.id} - {self.username} ({self.role})>"
