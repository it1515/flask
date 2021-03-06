# project/server/models.py


import datetime

from project.server import app, db, bcrypt


class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)
    admin = db.Column(db.Boolean, nullable=False, default=False)

    def __init__(self, email, password, admin=False):
        self.email = email
        self.password = bcrypt.generate_password_hash(
            password, app.config.get('BCRYPT_LOG_ROUNDS')
        ).decode('utf-8')
        self.registered_on = datetime.datetime.now()
        self.admin = admin

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    def __repr__(self):
        return '<User {0}>'.format(self.email)

class Krava(db.Model):

    __tablename__ = "pocitadlo_krav"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    pocet_krav = db.Column(db.Integer, unique=False, nullable=False)
    datumvlozeni = db.Column(db.DateTime, nullable=False)

    def __init__(self,pocet_krav):
        self.datumvlozeni = datetime.datetime.now()
        self.pocet_krav=pocet_krav

    def get_id(self):
        return self.id

