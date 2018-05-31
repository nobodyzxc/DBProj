from flask import Flask, jsonify, render_template, request, redirect, flash
from flask_login import login_required, current_user
import sqlite3


app = Flask(__name__)

# -> login, and blog available
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

# => editor & config, show posts here
@app.route('/<string:user>/console')
@login_required
def console(user):
    return render_template('console.html')

# layout and extension market here
@app.route('/<string:user>/config')
@login_required
def config(user):
    return render_template('config.html')

# markdown editor
@app.route('/<string:user>/editor')
@login_required
def mkd_editor(user):
    return render_template('editor.html')

# user blog render
@app.route('/blog/<string:user>')
def home_page(user):
    return render_template('home_page.html')

@app.route('/blog/<string:user>/<string:post>')
def home_page(user, post):
    return 'impl here'

if __name__=='__main__':
    app.run(debug=True)
