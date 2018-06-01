from flask import Flask, jsonify, render_template, request, redirect, flash, url_for
from flask_login import login_required, current_user, login_user, LoginManager

from module.user import UsersRepository

import sqlite3

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'

users = UsersRepository()
users.load_db()

# handle login failed
@app.errorhandler(401)
def page_not_found(e):
    return Response('<p>Login failed</p>')

# -> login, and blog available
@app.route('/')
def index():
    return render_template('index.html')

if __name__=='__main__':
    app.users = users

    from views.login import login_pages, login_manager
    app.register_blueprint(login_pages)

    login_manager.login_view = 'login_pages.login'
    login_manager.init_app(app)

    from views.editor import editor_pages
    app.register_blueprint(editor_pages)

    from views.config import config_pages
    app.register_blueprint(config_pages)

    from views.blog import blog_pages
    app.register_blueprint(blog_pages)

    from views.manage import manage_pages
    app.register_blueprint(manage_pages)

    app.run(debug=True)
