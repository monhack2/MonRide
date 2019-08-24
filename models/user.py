from monride import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    first_name = db.Column(db.String, unique=True, nullable=True)
    last_name = db.Column(db.String, unique=True, nullable=True)
    driver = db.Column(db.Boolean)
    rating = db.Column(db.Float)

