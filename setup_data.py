import sqlite3
# CONTSTANTS

DB_PATH = 'static/data/data.db'
ERR_MSG = "Errore nell'accesso al database"
LOREM = "LOREM, ipsum dolor sit amet consectetur adipisicing elit. Voluptatum architecto ratione vero? Non quas quisquam tenetur repellendus nam, numquam velit accusantium voluptate animi? Blanditiis voluptas consectetur, nostrum quidem mollitia velit. "

ADMINS = [
    {'username':'akai', 'name': 'Ritsuko', 'surname': 'Akagi', 'description': LOREM*6, 'motto': 'Nessuno conosce il segreto degli eva...', 'monthsago_update': 3, 'propic':'Ritsuko_Akagi.jpeg'},
    {'username':'penpen', 'name': 'Misato', 'surname': 'Katsuragi', 'description': LOREM*6, 'motto': 'Cosa mi nasconde la NERV?', 'monthsago_update': 11, 'propic':'Misato_Katsuragi.jpeg'},
    {'username':'soryuka', 'name': 'Asuka',  'surname':'Soryu Langley', 'description': LOREM*6, 'motto': 'Sono nata per pilotare gli eva', 'monthsago_update': 2, 'propic':'Asuka_Soryu.jpeg'}
]

NON_ADMINS = [
    {'username':'ikarisan', 'name': 'Shinji', 'surname': 'Ikari', 'propic':'Shinji_Ikari.jpeg'},
    {'username':'kaoruni', 'name': 'Kaoru', 'surname': 'Nagisa', 'propic':'Kaoru_Nagisa.jpeg'},
]

POSTS = [
    {'id': 1, 'user': 1, 'date': '2022-12-10', 'text': LOREM*2, 'img':'post1.jpg'},
    {'id': 2, 'user': 2, 'date': '2022-12-10', 'text': LOREM, 'img':'post2.jpg'},
    {'id': 3, 'user': 3, 'date': '2022-12-10', 'text': LOREM, 'img':'post3.jpg'},
]

COMMENTS = [
    {'text':LOREM, 'date': '2022-12-11', 'user': 1, 'post': 1},
    {'text':LOREM, 'date': '2022-12-10', 'user': 1, 'post': 1},
    {'text':LOREM, 'date': '2022-12-11', 'user': 2, 'post': 1},
    {'text':LOREM, 'date': '2022-12-09', 'user': 1, 'post': 2}
]

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
    print(ERR_MSG)        
    conn.rollback()

# Inserting standard users
try:
    sql = "INSERT INTO users(username, name, surname, propic) VALUES (?, ?, ?, ?)"
    for user in NON_ADMINS:
        data = (user.get('username'), user.get('name'), user.get('surname'), user.get('propic'))
        cursor.execute(sql, data)
        conn.commit()
except:
    print(ERR_MSG)
    conn.rollback()

# Inserting posts
try:
    sql = "INSERT INTO posts(text, img, date, user_id) VALUES (?, ?, ?, ?)"
    for post in POSTS:
        #TODO: Do python convert integers/string to their respective types into the DB?
        data = (post.get('text'), post.get('img'), post.get('date'), post.get('user'))
        cursor.execute(sql, data)
        conn.commit()
except:
    print(ERR_MSG)
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
    print(ERR_MSG)
    conn.rollback()

cursor.close()
conn.close()