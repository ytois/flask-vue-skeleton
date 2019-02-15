from datetime import datetime

from flask_login import UserMixin

from models.database import db


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.now, onupdate=datetime.now)

    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    def get_id(self):
        return self.id
