from monride import db
from models.user import User
from models.destination import Destination

# allCampuses = {
#     0: {
#         "name": "Clayton",
#         "address": "Wellington Rd, Clayton",
#         "postcode": 3800,
#     },
#     1: {
#         "name": "Caulfield",
#         "address": "900 Dandenong Rd, Caulfield East",
#         "postcode": 3145
#     },
#     2: {
#         "name": "Peninsula",
#         "address": "Moorooduc Hwy, Frankston",
#         "postcode": 3199
#     }
# }

db.drop_all()

db.create_all()
clayton = Destination(name='Clayton', address='Wellington Rd, Clayton', postcode=3800)
peninsula = Destination(name='Peninsula', address='Moorooduc Hwy, Frankston', postcode=3199)
caulfield = Destination(name='Caulfield', address='900 Dandenong Rd, Caulfield East', postcode=3145)
admin = User(username='admin', email='admin@example.com', driver=False, first_name='admin', last_name='admin')
guest = User(username='guest', email='guest@example.com', driver=False, first_name='guest', last_name='guest')
user1 = User(username='user1', email='user1@example.com', driver=False, first_name='user', last_name='1')
user2 = User(username='user2', email='user2@example.com', driver=True, rating=4.6, first_name='user', last_name='2')
Dogge = User(username='Dogge', email='Dogge@example.com', driver=False, first_name='Dogge', last_name='Smith')
db.session.add(admin)
db.session.add(guest)
db.session.add(user1)
db.session.commit()

