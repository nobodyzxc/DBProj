from flask import abort, Blueprint, render_template, request, redirect, flash, url_for
from flask_login import login_required, current_user
from app import app, users, db_name
from module.db import query, alter, va_query, va_alter

editor_pages = Blueprint('editor_pages', __name__,
                        template_folder='templates')
global postId
# markdown editor
@editor_pages.route('/editor')
@login_required
def editor():

    postid = request.args.get('postid', default = None)

    if not postid:
        return abort(404)

    name = current_user.get_username()

    posts = va_query(db_name, """
    select content , title, owner from post
        where postid = ?
    """, postid)

    if not posts:
        return abort(404)
    else:
        mkd, title, owner = posts[0]

    if name != owner:
        return abort(403)

    return render_template('editor.html',
            mkd = mkd, title = title, postid = postid)

@editor_pages.route('/editor/update_post', methods=['GET', 'POST'])
def update_post():
    mkd = request.form.get('mkd')
    postid = request.form.get('postid')
    name = current_user.get_username()

    posts = va_query(db_name, """
    select owner from post
        where postid = ?
    """, postid)

    if not posts:
        return abort(404)

    owner = posts[0][0]

    if owner != name:
        return abort(403)

    va_alter(db_name, """update post
                   set content = ?
                   where postid = ?
                   """, mkd, postid)
    return("success")

# @editor_pages.route('/editor/update_all', methods=['GET', 'POST'])
# def update_all():
#     mkd = request.form.get('mkd')
#     postid = request.form.get('postid')
#     title = request.form.get('postid')
#     name = current_user.get_username()
#     alter(db_name, """update post
#                    set content = '%s' , title = '%s'
#                    where owner = '%s' and postid = %s
#                    """% (mkd, title, name, postid))
#     return("success")



# alter(db_name, """update post
#                   set content = '%s',title = '%s'
#                   where owner = '%s' and postid = '%s'
#                   """% (mkd, title, name, postid))

