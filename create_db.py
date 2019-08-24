from monride import db
from models.user import User

db.drop_all()

db.create_all()
admin = User(username='admin', email='admin@example.com')
guest = User(username='guest', email='guest@example.com')
user1 = User(username='user1', email='user1@example.com', driver=False)
user2 = User(username='user2', email='user2@example.com', driver=True, rating=4.6)
db.session.add(admin)
db.session.add(guest)
db.session.add(user1)
db.session.commit()

