from monride import db

class Journey(db.Model):
    __tablename__ = 'journey'
    id = db.Column(db.Integer, primary_key=True)
    passengers_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    passengers = db.relationship('User', backref=db.backref('journey', lazy=True))
