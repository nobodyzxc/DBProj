from flask import Blueprint, render_template, request, redirect, flash, url_for, abort, Response
from flask_login import login_required, current_user
from app import app, users, db_name
from module.db import query, alter, va_query, va_alter
import re
import json

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

    blogname = va_query(db_name,
            """
            select blogname from blog
                where owner = ?
                """, current_user.username)[0][0]

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
    return render_template('manage.html',
            blog = blogname,
            name = current_user.username,
            title = title, postid = postid,
            date = date, length = length)

@manage_pages.route('/manage/delete_post', methods=['GET', 'POST'])
def delete_post():
    if request.method == 'POST':
        postid = request.form.getlist("postid")
        for pid in postid:
            alter(db_name, """delete from post
                            where postid = {} and owner= {}""".format(pid,
                                                            "'"+current_user.username+"'"))

    return redirect(url_for('manage_pages.manage'))

@manage_pages.route('/manage/update_title',methods=['POST', 'GET'])
@login_required
def update_title():
    postid = request.form.get("postid", None)
    newtitle = request.form.get("newtitle", None)
    print(request.form)
    if postid and newtitle:
        posts = va_query(db_name, """
            select owner from post
                where postid = ?""", postid)
        if posts:
            owner = posts[0][0]
            if owner == current_user.username:
                va_alter(db_name, """
                    update post set
                        title = ?
                        where postid = ?""",
                        newtitle, postid)

                return Response(
                        json.dumps({
                            "status": "success",
                            "href": ("/blog/%s/%s"
                                % (owner, newtitle)),
                            "text": newtitle,
                            "postid": postid
                            }),
                        mimetype = 'application/json')

    return Response(json.dumps({"status" : "failed"}), mimetype = 'application/json')
