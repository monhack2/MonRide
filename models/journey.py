from monride import db

class Journey(db.Model):
    __tablename__ = 'journey'
    id = db.Column(db.Integer, primary_key=True)
    drivers_id = db.Column(db.Integer, db.ForeignKey('driver.id'), primary_key=True)
    passengers_id = db.Column(db.Integer, db.ForeignKey('passenger.id'), primary_key=True)