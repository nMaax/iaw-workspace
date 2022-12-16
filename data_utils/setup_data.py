import sqlite3
import DATA_CONSTANTS as CONST

DB_PATH = CONST.DB_PATH
ERR_MSG = CONST.ERR_MSG

ADMINS = CONST.ADMINS
NON_ADMINS = CONST.NON_ADMINS
POSTS = CONST.POSTS
COMMENTS = CONST.COMMENTS

# Sql management
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Inserting admind
# Se provo a rompere un vincolo del database questo scatena un eccezione e il comando è annulato
try:
    sql = "INSERT INTO users(username, name, surname, propic, description, motto) VALUES (?, ?, ?, ?, ?, ?)"
    for admin in ADMINS:
        # TODO: gestire months-ago update
        data = (admin.get('username'), admin.get('name'), admin.get('surname'), admin.get('propic'), admin.get('description'), admin.get('motto'))
        cursor.execute(sql, data)
        #TODO: Is it the same if i commmit just one time?
        conn.commit()
except:
    print(ERR_MSG+" - setup_data.py")        
    conn.rollback()

# Inserting standard users
#try:
#    sql = "INSERT INTO users(username, name, surname, propic) VALUES (?, ?, ?, ?)"
#    for user in NON_ADMINS:
#        data = (user.get('username'), user.get('name'), user.get('surname'), user.get('propic'))
#        cursor.execute(sql, data)
#        conn.commit()
#except:
#    print(ERR_MSG+" - setup_data.py")
#    conn.rollback()

# Inserting posts
try:
    sql = "INSERT INTO posts(text, img, date, user_id) VALUES (?, ?, ?, ?)"
    for post in POSTS:
        #TODO: Do python convert integers/string to their respective types into the DB?
        data = (post.get('text'), post.get('img'), post.get('date'), post.get('user'))
        cursor.execute(sql, data)
        conn.commit()
except:
    print(ERR_MSG+" - setup_data.py")
    conn.rollback()

# Insering comments
try:
    sql = "INSERT INTO comments(text, date, user_id, post_id) VALUES (?, ?, ?, ?)"
    for comment in COMMENTS:
        #TODO: Do python convert integers/string to their respective types into the DB?
        data = (comment.get('text'), comment.get('date'), comment.get('user'), comment.get('post'))
        cursor.execute(sql, data)
        conn.commit()
except:
    print(ERR_MSG+" - setup_data.py")
    conn.rollback()

cursor.close()
conn.close()