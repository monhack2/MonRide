from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from flask import request


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)


from models.user import User

@app.route('/')
def hello_world():
    doge = User.query.filter_by(username=request.args.get('user', 'doge')).first()
    return render_template('index.html', current='home', user=doge)


@app.route('/book')
def book():
    user = User.query.filter_by(username='user2').first()
    return render_template('book.html', current='book', user=user)


@app.route('/calendar')
def calendar():
    return render_template('calendar.html', current='calendar')

