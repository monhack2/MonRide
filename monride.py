from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)


from models.user import User
doge = User.query.filter_by(username='doge').first()

@app.route('/')
def hello_world():
    return render_template('index.html', current='home', username=doge.username, stars=doge.rating)


@app.route('/book')
def book():
    return render_template('book.html', current='book')
