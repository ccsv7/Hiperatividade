import sqlite3

conn = sqlite3.connect('users.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
id INTEgER PRIMARY KEY AUTOINCREMENT,
nome TEXT NOT NULL,
email TEXT NOT NULL UNIQUe,
senha TEXT NOT NULL
)
''')

conn.commit ()
conn.close()

print("Banco de dados criado com sucesso")