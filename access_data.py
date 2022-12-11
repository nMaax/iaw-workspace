import sqlite3

DB_PATH = 'static/data/data.db'

#TODO: metti i return come dizionari row

def get_posts():

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = dict_factory #sqlite3.Row
    cursor = conn.cursor()
    posts = False

    try:
        sql = "SELECT * FROM POSTS"
        cursor.execute(sql)
        posts = cursor.fetchall()
    except:
        print('Failed to retrive data in access_data.get_posts()')
        conn.rollback()

    cursor.close()
    conn.close()

    return posts

def get_post(post_id):
    
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = dict_factory #sqlite3.Row
    cursor = conn.cursor()
    posts = False

    try:
        sql = "SELECT * FROM POSTS WHERE id = ?"
        cursor.execute(sql, (post_id,))
        posts = cursor.fetchall()
    except:
        print('Failed to retrive data in access_data.get_post(post_id)')
        conn.rollback()

    cursor.close()
    conn.close()

    return posts

def get_comments(post_id):
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = dict_factory #sqlite3.Row
    cursor = conn.cursor()
    comments = False

    try:
        sql = "SELECT * FROM COMMENTS WHERE post_id = ?"
        cursor.execute(sql, (post_id,))
        comments = cursor.fetchall()
    except:
        print('Failed to retrive data in access_data.get_comments(post_id)')
        conn.rollback()

    cursor.close()
    conn.close()

    return comments

def get_admins():
    return get_users(True)

def get_users(admin=False):
    
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = dict_factory #sqlite3.Row
    cursor = conn.cursor()
    users = False

    try:
        if admin:
            sql = "SELECT * FROM USERS WHERE motto IS NOT NULL AND description IS NOT NULL"
        else:
            sql = "SELECT * FROM USERS"
        cursor.execute(sql)
        users = cursor.fetchall()
    except:
        print('Failed to retrive data in access_data.get_users(admin)')
        conn.rollback()

    cursor.close()
    conn.close()

    print(type(users))
    return users

def add_post(post):

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    try:
        sql = "INSERT INTO posts(text, img, date, user_id) VALUES (?, ?, ?, ?)"
        data = (post.get('text'), post.get('img'), post.get('date'), post.get('user_id'))
        cursor.execute(sql, data)
        conn.commit()
    except:
        print("Errore nell'accesso al database, non è stato possibile inserire il nuovo utente")        
        conn.rollback()

def add_comment(comment):

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    try:
        sql = "INSERT INTO comments(text, date, user_id, post_id) VALUES (?, ?, ?, ?)"
        data = (comment.get('text'), comment.get('date'), comment.get('user_id'), comment.get('post_id'))
        cursor.execute(sql, data)
        conn.commit()
    except:
        print("Errore nell'accesso al database, non è stato possibile inserire il nuovo commento")        
        conn.rollback()

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d