import sqlite3
from os import listdir
from os.path import isfile, join

conn = sqlite3.connect('test.db')
cursor = conn.cursor()

mypath = 'mkds'
mkds = [f for f in listdir(mypath) if isfile(join(mypath, f))]

for mkd in mkds:
    f = open(mypath + '/' + mkd, 'r')
    post = f.read()
    for user in [u + 'dmin' for u in "abcd"]:
        command = "INSERT INTO POST (TITLE, CONTENT, POSTDATE, BLOGNAME) VALUES ('%s','%s', '2018-01-01 10:00:00', '%s');" % (mkd, post, user)
        cursor.execute(command)

conn.commit()
conn.close()
