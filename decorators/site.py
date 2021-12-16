from flask import Flask

app = Flask(__name__)


@app.route('/')
def homepage():
    return "Homepage"


@app.route('/contacts')
def contacts():
    return "My contacts"


app.run()
