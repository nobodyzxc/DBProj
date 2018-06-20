from flask import Blueprint, render_template, request, redirect, flash, url_for, Response
from flask_login import login_required, current_user, login_user, LoginManager, logout_user

from module.security import hash_password, check_password
from app import app, users, db_name
from urllib.parse import urlencode, quote_plus
from module.db import va_query, va_alter

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
    signup_error_info = "exist username"

    if not current_user.is_anonymous:
        return redirect(url_for('manage_pages.manage'))

    next_href = request.args.get("next", default = None)

    relog_href = '/login'
    if next_href:
        relog_href = '/login?' + urlencode(
                {'next':request.args["next"]},
                quote_via=quote_plus)

    info = request.args.get("info", default = None)
    print(info, request.form.get("sign", None))
    if info == signup_error_info:
        return render_template('login.html',
                info = info,
                relog_href = relog_href)

    if request.method == 'POST':
        sign = request.form['sign']
        username = request.form.get('username', default=None)
        password = request.form.get('password', default=None)
        blogname = request.form.get('blogname', default=None)
        user = users.get_user(username)
        if sign == 'up':
            if user == None and username and password and blogname:
                users.save_user(db_name , username, hash_password(password))
                login_user(users.get_user(username))
                va_alter(db_name, """
                    insert into blog values(?, ?, '0000000', 'muse');
                """, blogname, username)
                return redirect(url_for('manage_pages.manage'))
            else:
                return redirect(url_for('login_pages.login') + "?info=exist%20username#signup")
        elif sign == 'in':
            if user != None and check_password(user.hashedpw, password):
                login_user(user)

                print(next_href)
                if next_href:
                    return redirect(next_href)
                else:
                    return redirect(url_for('manage_pages.manage'))
            else:
                return render_template('login.html',
                        info = 'signin failed',
                        relog_href = relog_href)
        else:
            Response("Invalid signin/signup form")
    else:
        return render_template('login.html',
                info = "", # no post data
                relog_href = relog_href)

# -> provide logout function
@login_pages.route('/logout')
def logout():
    logout_user()
    return redirect("/")

@login_pages.route('/users')
def user_list():
    print(users.users)
    return render_template('users.html', user_list = users.users)
