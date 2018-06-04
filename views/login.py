from flask import Blueprint, render_template, request, redirect, flash, url_for
from flask_login import login_required, current_user, login_user, LoginManager

from module.security import hash_password, check_password
from app import app, users, db_name

login_manager = LoginManager()

login_pages = Blueprint('login_pages', __name__,
                        template_folder='templates')

# callback to reload the user object
@login_manager.user_loader
def load_user(userid):
    return users.get_user(userid)

# -> provide login function
@login_pages.route('/login', methods=['GET' , 'POST'])
def login():
    if request.method == 'POST':
        sign = request.form['sign']
        username = request.form['username']
        password = request.form['password']
        user = users.get_user(username)
        if sign == 'up':
            if user == None:
                users.save_user(db_name , username, hash_password(password))
                login_user(users.get_user(username))
                return redirect(url_for('manage_pages.manage'))
            else:
                return render_template('login.html', info = 'existed username')
        elif sign == 'in':
            if user != None and check_password(user.hashedpw, password):
                login_user(user)
                print(user.username + "loggined")
                return redirect(url_for('manage_pages.manage'))
            else:
                return render_template('login.html', info = 'signin failed')
        else:
            Response("Invalid signin/signup form")
    else:
        return render_template('login.html', info = "no post data")

# -> provide logout function
@login_pages.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('/'))

@login_pages.route('/users')
def user_list():
    print(users.users)
    return render_template('users.html', user_list = users.users)
