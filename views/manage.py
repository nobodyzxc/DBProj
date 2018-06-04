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
    return render_template('manage.html', name = current_user.username)
