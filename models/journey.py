from monride import db
from .user import User
from .destination import Destination

class Journey(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    driver = db.Column()
    user = db.relationship('User', backref=db.backref('users', lazy=True))