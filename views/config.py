from flask import Blueprint, render_template, request, redirect, flash, url_for
from flask_login import login_required, current_user
from app import app, users, db_name
from module.db import query, alter

config_pages = Blueprint('config_pages', __name__,
                        template_folder='templates')
title = ["title1","title2","title3","title4"]
allLayout = [["aaa","bbb","ccc"],["aa","bb"]]

# layout and extension market here
@config_pages.route('/config', methods=['GET' , 'POST'])
@login_required
def config():
    selectlist = []
    
    selectlist.append(request.form.getlist('allLayout'))
    listToStr = ','.join(letters(str(r)) for v in selectlist for r in v)
    print(listToStr)
    allLayout[0] = getLayoutName(db_name,"LAYOUTNAME")
    return render_template('config.html',allLayout=allLayout,LayoutTitle = title)

def getLayoutName(db,layout):
    return query(db, """
            SELECT LAYOUTNAME FROM LAYOUT
                """.format(LAYOUTNAME = layout))
def letters(input):
    return ''.join([str(c) for c in input if (c.isalpha())])