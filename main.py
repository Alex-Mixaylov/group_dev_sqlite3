# import sqlite3
#
# conn = sqlite3.connect('example.db')
# cur = conn.cursor()
#
# cur.execute('''
#     CREATE TABLE IF NOT EXISTS users
#     (id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL,
#     age INTEGER NOT NULL)
#         ''')
# conn.commit()
#
# cur.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("John", 25))
# cur.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Jane", 20))
# conn.commit()
#
# conn.close()

import sqlite3

conn = sqlite3.connect('example.db')
cur = conn.cursor()

cur.execute("SELECT * FROM users")
rows = cur.fetchall()
for row in rows:
    print(row)

conn.commit()


