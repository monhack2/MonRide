from monride import db


class Available(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, backref=db.backref('users', lazy=True))
