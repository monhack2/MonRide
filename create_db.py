from monride import db
from models.user import User

db.drop_all()

db.create_all()
admin = User(username='admin', email='admin@example.com', driver=False, rating=5, first_name='admin', last_name='admin')
guest = User(username='guest', email='guest@example.com', driver=False, rating=1, first_name='guest', last_name='guest')
user1 = User(username='user1', email='user1@example.com', driver=False, rating=2.6, first_name='user', last_name='1')
user2 = User(username='user2', email='user2@example.com', driver=True, rating=4.6, first_name='user', last_name='2')
Dogge = User(username='doge', email='Doge@example.com', driver=False, rating=4.6, first_name='Doge', last_name='Smith')
db.session.add(admin)
db.session.add(guest)
db.session.add(user1)
db.session.add(user2)
db.session.add(Dogge)
db.session.commit()

