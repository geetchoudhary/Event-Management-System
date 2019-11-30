from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from app import db, login
from flask_login import UserMixin


class Visitor(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    email = db.Column(db.String(120), index=True, unique=True)
    phone = db.Column(db.Integer, index=True, unique=True)
    checkInTime = db.Column(db.DateTime, index=True, default=datetime.utcnow())
    checkOutTime = db.Column(db.DateTime)

    def __repr__(self):
        return '<Visitor {}>'.format(self.name)


class Host(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    vis_name = db.Column(db.String(64), unique=True)

    def __repr__(self):
        return '<Host {}>'.format(self.body)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    @login.user_loader
    def load_user(id):
        return Host.query.get(int(id))
