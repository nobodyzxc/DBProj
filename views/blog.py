from flask import Blueprint, render_template, request, redirect, flash, url_for, abort, Response
from flask_login import current_user
from app import app, users, db_name
from module.db import va_query, va_alter
from module.user import User
import markdown2
from urllib.parse import urlencode, quote_plus
import time

blog_pages = Blueprint('blog_pages', __name__,
                        template_folder='templates')

# user blog render
@blog_pages.route('/blog/<string:user>')
def home_page(user):
    if not users.exist(user):
        return abort(404)
    posts = va_query(db_name,
            """
            select title, postdate from post
                where owner = ?
                """, user)
    blogname, theme = get_blog_theme(user)
    return render_template('next_' + theme + '.html',
            user_name = user,
            posts = posts,
            blog_name = blogname,
            post_wedge = '\n',
            cat_href = ("/" if current_user.is_anonymous else "/manage"))


    if not users.exist(user):
        return abort(404)
    return render_template('home_page.html', blog_name , blog_href)

@blog_pages.route('/blog/<string:user>/<string:title>')
def user_post(user, title):
    if not users.exist(user):
        return abort(404)
    post = va_query(db_name,
            """
            select title, postdate, content, postid from post
                where owner = ? and
                      title = ?
                      """, user, title)

    if post == []:
        return abort(404)


    mkd = markdown2.markdown(post[0][2], extras=["header-ids", "fenced-code-blocks","tables"])
    markdown_html = markdown2.markdown(post[0][2], extras=["toc","fenced-code-blocks","tables"])
    toc = markdown_html.toc_html
    
    blogname, theme = get_blog_theme(user)

    return render_template(
            'next_' + theme + '_post.html',
            user_name = user,
            post_title = post[0][0],
            post_href = '/blog/' + user + '/' + title,
            post_time = post[0][1],
            post_content = mkd,
            blog_name = blogname,
            blog_href = '/blog/' + user,
            post_id = post[0][3],
            post_wedge = '\n',
            post_tocs = toc,
            cat_href = ("/" if current_user.is_anonymous else "/manage"))

def get_blog_theme(user):
    return va_query(db_name,
            """
            select blogname, layoutname from blog
                where owner = ?
                """, user)[0]

#### FOR TEST ####

@blog_pages.route('/ex/<string:theme>/<string:user>')
def theme_home_page(theme, user):
    if theme not in ['mist', 'muse', 'gemini', 'pisces']:
        return abort(404)
    if not users.exist(user):
        return abort(404)
    posts = va_query(db_name,
            """
            select title, postdate from post
                where owner = ?
                """, user)
    return render_template('next_' + theme + '.html',
            user_name = user,
            posts = posts,
            blog_name = get_blog_theme(user)[0],
            post_wedge = '\n',
            cat_href = ("/" if current_user.is_anonymous else "/manage"))

@blog_pages.route('/ex/<string:theme>/<string:user>/<string:title>')
def theme_user_post(theme, user, title):
    if theme not in ['mist', 'muse', 'gemini', 'pisces']:
        return abort(404)
    if not users.exist(user):
        return abort(404)
    post = va_query(db_name,
            """
            select title, postdate, content,postid from post
                where owner = ? and
                      title = ?
                      """, user, title)

    if post == []:
        return abort(404)

    mkd = markdown2.markdown(post[0][2], extras=["header-ids", "fenced-code-blocks","tables"])
    markdown_html = markdown2.markdown(post[0][2], extras=["toc","fenced-code-blocks","tables"])
    toc = markdown_html.toc_html

    return render_template(
            'next_' + theme + '_post.html',
            user_name = user,
            post_title = post[0][0],
            post_href = '/blog/' + user + '/' + title,
            post_time = post[0][1],
            post_content = mkd,
            post_id = post[0][3],
            blog_name = get_blog_theme(user)[0],
            blog_href = '/blog/' + user,
            post_wedge = '\n',
            post_tocs = toc,
            cat_href = ("/" if current_user.is_anonymous else "/manage"))


@blog_pages.route('/message/<int:post_id>')
def get_post_message(post_id, methods=['GET']):
    print(post_id)
    print(current_user.is_anonymous)
    loging = not current_user.is_anonymous

    who = current_user.username if loging else ''

    msgs = va_query(db_name,
            """
            select poster, msgdate, content, msgid from message
                where postid = ?
                order by msgdate desc
                """, post_id)

    blogger = va_query(db_name,
            """
            select owner from post
                where postid = ?
            """, post_id)[0][0]

    msgs = [(a,b,markdown2.markdown(c, extras=["header-ids", "fenced-code-blocks"]), d) for (a,b,c,d) in msgs]

    next_href = '/login?' + urlencode(
            {'next':request.args["next"]},
            quote_via=quote_plus)

    return render_template('message.html',
            who = who,
            messages = msgs,
            blogger = blogger,
            logining = loging,
            post_id = post_id,
            prev_href =
            request.args.get("next", default=""),
            submit_url =
            ("/message_upload" if loging else '/login'),
            submit_btn_name =
            ("留言" if loging else "登入"),
            method =
            ("post" if loging else "get"),
            msg_count = len(msgs)
            )

@blog_pages.route('/message_upload', methods=['GET', 'POST'])
def upload_message():
    postid = request.form.get("postid", default = None)
    content = request.form.get("content", default=None)

    if current_user.is_anonymous \
            or not postid or not content:
        return abort(403)

    va_alter(db_name, """
           INSERT INTO MESSAGE
            (MSGDATE, POSTER, CONTENT, POSTID) VALUES
            (?, ?, ?, ?);
           """ , time.strftime('%Y-%m-%d %H:%M:%S'),
               current_user.get_username(),
               content, postid)
    return Response("ok")


@blog_pages.route('/message_del', methods=['GET', 'POST'])
def message_del():
    msgid = request.args.get("id", None)

    if not msgid or current_user.is_anonymous:
        return Response("not ok")

    postid, writer = va_query(db_name,"""
            select postid, poster from message
                where msgid = ?""", msgid)[0]
    owner = va_query(db_name,"""
            select owner from post
                where postid = ? """, postid)[0][0]
    
    if current_user.username == owner or \
        current_user.username == writer:
        va_alter(db_name,
                """
                delete from message
                    where msgid = ?""", msgid)
    return Response("ok")
