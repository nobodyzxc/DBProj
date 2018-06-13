from flask import Blueprint, render_template, request, redirect, flash, url_for
from flask_login import login_required, current_user
from app import app, users, db_name
from module.db import query, alter

manage_pages = Blueprint('manage_pages', __name__,
                        template_folder='templates')

# => manage & config, show posts here
@manage_pages.route('/manage')
@login_required
def manage():
    posts = query(db_name,# load articles
            """
            select postid, title, postdate
            from post
            where owner = """ + "'" + current_user.username + "'")
    postid = []
    title = []
    date = []
    for pid, tit, dat in posts:
        postid.append(pid)
        title.append(tit)
        date.append(dat)
    length = list(range(len(title)))
    #posts = list(map(lambda x: x[0], posts))
    # delete function
    return render_template('manage.html', name = current_user.username,
                           title = title, postid = postid, date = date, length = length)
