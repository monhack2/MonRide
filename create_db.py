from monride import db
from models.user import User

db.drop_all()

db.create_all()
admin = User(username='admin', email='admin@example.com', first_name='admin', last_name='admin')
guest = User(username='guest', email='guest@example.com', first_name='guest', last_name='guest')
user1 = User(username='user1', email='user1@example.com', driver=False, first_name='user', last_name='1')
user2 = User(username='user2', email='user2@example.com', driver=True, rating=4.6, first_name='user', last_name='2')
db.session.add(admin)
db.session.add(guest)
db.session.add(user1)
db.session.commit()

