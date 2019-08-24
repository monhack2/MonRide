from monride import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    driver = db.Column(db.Boolean)
    rating = db.Column(db.Float)
    first_name = db.Column(db.String, unique=True, nullable=False)
    last_name = db.Column(db.String, unique=True, nullable=False)


