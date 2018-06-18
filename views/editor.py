from flask import abort, Blueprint, render_template, request, redirect, flash, url_for
from flask_login import login_required, current_user
from app import app, users, db_name
from module.db import query, alter

editor_pages = Blueprint('editor_pages', __name__,
                        template_folder='templates')
global postId
# markdown editor
@editor_pages.route('/editor')
@login_required
def editor():
    postId=2
    name = current_user.get_username()
    mkd = query(db_name, """
    select content from post
        where owner = '%s'
    """ % (name))[postId][0]
    title = query(db_name, """
    select title from post
        where owner = '%s'
    """ % (name))[postId][0]

    return render_template('editor.html',mkd = mkd, title = title, postid = postId )

@editor_pages.route('/editor/update_post', methods=['GET', 'POST'])
def update_post():
    mkd = request.form.get('mkd')
    postid = request.form.get('postid')
    name = current_user.get_username()
    print(name)
    print(postid)
    alter(db_name, """update post
                   set content = '%s' 
                   where owner = '%s' and postid = %s
                   """% (mkd, name, postid))
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

