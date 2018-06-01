from flask import Blueprint, render_template, request, redirect, flash, url_for
from flask_login import login_required
from app import app, users

config_pages = Blueprint('config_pages', __name__,
                        template_folder='templates')

# layout and extension market here
@config_pages.route('/config')
@login_required
def config():
    return render_template('config.html')

