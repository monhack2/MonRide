from monride import db



class Destination(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)
    postcode = db.Column(db.Intger, nullable=False)