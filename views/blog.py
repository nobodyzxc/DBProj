from flask import Blueprint, render_template, request, redirect, flash, url_for, abort
from flask_login import current_user
from app import app, users, db_name
from module.db import query
import markdown2

blog_pages = Blueprint('blog_pages', __name__,
                        template_folder='templates')

# user blog render
@blog_pages.route('/blog/<string:user>')
def home_page(user):
    if not users.exist(user):
        return abort(404)
    posts = query(db_name,
            """
            select title, postdate from post
                where owner = """ + "'" + user + "'")
    blogname, theme = get_blog_theme(user)
    return render_template('next_' + theme + '.html',
            user_name = user,
            posts = posts,
            blog_name = blogname,
            post_wedge = '\n')


    if not users.exist(user):
        return abort(404)
    return render_template('home_page.html', blog_name , blog_href)

@blog_pages.route('/blog/<string:user>/<string:title>')
def user_post(user, title):
    if not users.exist(user):
        return abort(404)
    post = query(db_name,
            """
            select title, postdate, content from post
                where owner = '%s' and
                      title = '%s'
                      """ % (user, title))

    if post == []:
        return abort(404)

    mkd = markdown2.markdown(post[0][2], extras=["header-ids", "fenced-code-blocks"])

    blogname, theme = get_blog_theme(user)

    return render_template(
            'next_' + theme + '_post.html',
            user_name = user,
            post_title = post[0][0],
            post_href = '/blog/' + user + '/' + title,
            post_time = post[0][1],
            post_content = mkd,
            blog_name = blogname,
            post_wedge = '\n')

def get_blog_theme(user):
    return query(db_name,
            """
            select blogname, layoutname from blog
                where owner = '%s'
                """ % (user))[0]

#### FOR TEST ####

@blog_pages.route('/ex/<string:theme>/<string:user>')
def theme_home_page(theme, user):
    if theme not in ['mist', 'muse', 'gemini', 'pisces']:
        return abort(404)
    if not users.exist(user):
        return abort(404)
    posts = query(db_name,
            """
            select title, postdate from post
                where owner = """ + "'" + user + "'")
    return render_template('next_' + theme + '.html',
            user_name = user,
            posts = posts,
            blog_name = get_blog_theme(user)[0],
            post_wedge = '\n')

@blog_pages.route('/ex/<string:theme>/<string:user>/<string:title>')
def theme_user_post(theme, user, title):
    if theme not in ['mist', 'muse', 'gemini', 'pisces']:
        return abort(404)
    if not users.exist(user):
        return abort(404)
    post = query(db_name,
            """
            select title, postdate, content from post
                where owner = '%s' and
                      title = '%s'
                      """ % (user, title))

    if post == []:
        return abort(404)

    mkd = markdown2.markdown(post[0][2], extras=["header-ids", "fenced-code-blocks"])

    return render_template(
            'next_' + theme + '_post.html',
            user_name = user,
            post_title = post[0][0],
            post_href = '/blog/' + user + '/' + title,
            post_time = post[0][1],
            post_content = mkd,
            blog_name = get_blog_theme(user)[0],
            post_wedge = '\n')

