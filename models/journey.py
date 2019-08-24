from monride import db
from .user import User
from .destination import Destination

class Journey(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.relationship('User', backref=db.backref('journey', lazy=True))
