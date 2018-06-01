from flask import Blueprint, render_template, request, redirect, flash, url_for
from flask_login import current_user
from app import app, users

blog_pages = Blueprint('blog_pages', __name__,
                        template_folder='templates')

# user blog render
@blog_pages.route('/blog/<string:user>')
def home_page(user):
    return render_template('home_page.html')

@blog_pages.route('/blog/<string:user>/<string:post>')
def user_post(user, post):
    return 'impl here'
