import sqlite3
import data_utils.DATA_CONSTANTS as CONST

DB_PATH = CONST.DB_PATH
ERR_MSG = CONST.ERR_MSG

# Sql management
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Insering comments
try:
    sql = "DELETE FROM users"
    cursor.execute(sql)
    conn.commit()

    sql = "DELETE FROM posts"
    cursor.execute(sql)
    conn.commit()

    sql = "DELETE FROM comments"
    cursor.execute(sql)
    conn.commit()

    sql = "DELETE FROM sqlite_sequence"
    cursor.execute(sql)
    conn.commit()
except:
    print(ERR_MSG+" - clean_data.py")
    conn.rollback()

cursor.close()
conn.close()