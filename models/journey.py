from monride import db

class Journey(db.Model):
    __tablename__ = 'journey'
    id = db.Column(db.Integer, primary_key=True)
    passengers = db.relationship('User', backref='passenger', lazy=True)
