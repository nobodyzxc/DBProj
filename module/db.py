import os
import sqlite3

database = 'test.db'

def tupleStr(*t):
    return '(' + ','.join(["'" + x + "'" for x in t]) + ')'

#def execute_cmd(command, cursor):
#    cursor.execute(command)

def get_users(db):
    return query(db, """
            SELECT * FROM USER""")

def save_user(db, name, hpw):
    alter(db, 'INSERT INTO USER VALUES' +
            tupleStr(name, hpw) + ';')

def get_messages(db, post_id):
    query(db, """
            SELECT * FROM MESSAGE
                WHERE POSTID = """ + post_id)

def get_posts(db, blog):
    return query(db, """
                SELECT * FROM POST
                    WHERE BLOGNAME = """ + blog)

def get_layout(db, blog):
    return query(db, """
            SELECT * FROM LAYOUT
                WHERE BLOGNAME = """ + blog)

def alter(db_name, alter_str):
    if(os.path.isfile(db_name)):
        conn = sqlite3.connect(db_name)
        conn.cursor().execute(alter_str)
        conn.commit()
        conn.close()
    else:
        print("no such db : " + db_name)
        exit(0)

def query(db_name, query_str):
    if(os.path.isfile(db_name)):
        conn = sqlite3.connect(db_name)
        cur = conn.cursor()
        cur.execute(query_str)
        ret = cur.fetchall()
        conn.close()
        return ret
    else:
        print("no such db : " + db_name)
        exit(0)
