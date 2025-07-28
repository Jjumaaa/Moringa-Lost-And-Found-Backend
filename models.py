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

    @validates('email')
    def validate_email(self, key, email):
        if email and ('@' not in email or '.' not in email):
            raise ValueError("Please provide a suitable email address")
        return email

    @hybrid_property
    def password_hash(self):
        raise AttributeError("Password hashes are write-only.")

    @password_hash.setter
    def password_hash(self, password):
        self._password_hash = bcrypt.generate_password_hash(password.encode()).decode()

    def authenticate(self, password):
        return self._password_hash and bcrypt.check_password_hash(self._password_hash, password.encode())

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "role": self.role
        }