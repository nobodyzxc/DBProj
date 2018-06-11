from flask import abort, Blueprint, render_template, request, redirect, flash, url_for
from flask_login import login_required, current_user
from app import app, users, db_name
from module.db import query, alter

editor_pages = Blueprint('editor_pages', __name__,
                        template_folder='templates')

# markdown editor
@editor_pages.route('/editor')
@login_required
def editor():
    name = current_user.get_username()
    mkd = query(db_name, """
    select content from post
        where owner = '%s'
    """ % (name))[0][0]
    return render_template('editor.html',mkd = mkd)

