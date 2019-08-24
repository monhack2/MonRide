from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html', current='home')


@app.route('/book')
def book():
    return render_template('book.html', current='book')
