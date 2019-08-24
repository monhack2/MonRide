from monride import db



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    driver = db.Column(db.Boolean, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    course = db.Column(db.String, nullable=False)
    music = db.Column(db.String, nullable=False)
    interests = db.Column(db.String, nullable=False)
    avatar = db.Column(db.String, nullable=False)

