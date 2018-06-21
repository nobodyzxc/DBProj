from flask import Blueprint, render_template, request, redirect, flash, url_for
from flask_login import login_required, current_user
from app import app, users, db_name
from module.db import query, alter, va_query

config_pages = Blueprint('config_pages', __name__,
                        template_folder='templates')
allLayout = []
currlatout = ""
# layout and extension market here
@config_pages.route('/config', methods=['GET' , 'POST'])
@login_required
def config():

    blogname = va_query(db_name,
            """
            select blogname from blog
                where owner = ?
                """, current_user.username)[0][0]

    selectlist = []

    selectlist.append(request.form.getlist('allLayout'))
    listToStr = ','.join(letters(str(r)) for v in selectlist for r in v)
    print(listToStr)

    if listToStr.strip():
        storeLayout(db_name,listToStr,current_user.get_username())
        return redirect(url_for('manage_pages.manage'))

    currlatout = getCurrentLayout(db_name, current_user.get_username())

    allLayout = getLayoutName(db_name,"LAYOUTNAME")
    return render_template('config.html',
            blog = blogname,
            allLayout = allLayout,
            currentLay = currlatout,
            user = current_user.get_username())

def getLayoutName(db,layout):
    return query(db, """
            SELECT {LAYOUTNAME} FROM LAYOUT
                """.format(LAYOUTNAME = layout))
def letters(input):
    return ''.join([str(c) for c in input if (c.isalpha())])

def storeLayout(db,layout,user):
    return alter(db,"""
            UPDATE BLOG SET LAYOUTNAME = {Layout} WHERE OWNER = {own}
            """.format(Layout =  "'" +layout+"'",own = "'" +user+"'"))

def getCurrentLayout(db,user):
    return query(db,
                 """SELECT LAYOUTNAME FROM BLOG WHERE OWNER = {own};""".format(own = "'" +user+"'"))[0][0]
