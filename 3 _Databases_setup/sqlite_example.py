import sqlite3

create_database = """CREATE TABLE IF NOT EXISTS accounts (
user_id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
password TEXT NOT NULL,
email TEXT UNIQUE NOT NULL,
created_at DATETIME NOT NULL,
last_login DATETIME NOT NULL
)"""

con = sqlite3.connect('escuela.db')
cur = con.cursor()
cur.execute(create_database)

accounts = cur.execute("select * from accounts")

for row in accounts.fetchall():
    print(row)
