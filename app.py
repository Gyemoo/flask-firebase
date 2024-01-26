from flask import Flask, redirect, render_template, url_for, request
from DB_handler import DBModule

app = Flask(__name__)
DB = DBModule()

@app.route('/')
def index():
    pass

@app.route('/list')
def post_list():
    pass

@app.route('/post/<int:pid>')
def post(pid):
    pass

@app.route('/login')
def login():
    pass

@app.route('/signin')
def signin():
    pass

@app.route('/user/<uid>')
def user(uid):
    pass

@app.route('/write')
def write():
    pass

@app.route('/write_done', methods=["GET"])
def write_down():
    pass

if __name__== "__main__":
    app.run(host="0.0.0.0", debug=True)


