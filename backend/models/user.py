from models.database import db
from datetime import datetime
from flask import url_for
import secrets


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.now, onupdate=datetime.now)
    invite_code = db.Column(db.String(128), unique=True)

    @classmethod
    def create_invite(cls, name, email):
        code = cls.generate_invite_code()
        return User(name=name, email=email, invite_code=code)

    @classmethod
    def generate_invite_code(cls):
        return secrets.token_hex(nbytes=8)

    @property
    def invite_url(self):
        # TODO: tmp path
        return url_for('/', code=self.invite_code)
