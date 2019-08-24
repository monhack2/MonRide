from monride import db
from .user import User

class Driver(User):
    __tablename__ = 'driver'
    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)

