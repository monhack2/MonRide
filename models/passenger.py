from monride import db
from .user import User

class Passenger(User):
    __tablename__ = 'passenger'
    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)