import sqlite3
from os import listdir
from os.path import isfile, join

conn = sqlite3.connect('test.db')
cursor = conn.cursor()

mypath = 'mkds'
mkds = [f for f in listdir(mypath) if isfile(join(mypath, f))]

bu = [('Where is the admin?', 'admin'),
        ('bdmin is here!', 'bdmin'),
        ('cdmin is foo~', 'cdmin'),
        ('dd the root directory!', 'ddmin')]

for mkd in mkds:
    f = open(mypath + '/' + mkd, 'r')
    post = f.read()
    for blog,user in bu:
        cursor.execute("INSERT INTO POST (TITLE, CONTENT, POSTDATE, BLOGNAME, OWNER) VALUES (?,?, '2018-01-01 10:00:00', ?,?);", (mkd, post, blog,user))

conn.commit()
conn.close()
