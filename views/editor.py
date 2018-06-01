from flask import Blueprint, render_template, request, redirect, flash, url_for
from flask_login import login_required, current_user
from app import app, users

editor_pages = Blueprint('editor_pages', __name__,
                        template_folder='templates')

# markdown editor
@editor_pages.route('/editor')
@login_required
def editor():
    return render_template('editor.html')

