from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

@app.route('/')
def hello_world():
    return render_template('index.html', current='home')


@app.route('/book')
def book():
    return render_template('book.html', current='book')
