import sqlite3
connection = sqlite3.connect('todo.db')
with open('DB/schema.sql') as f:
    connection.executescript(f.read())

cursor  = connection.cursor()
cursor.execute('INSERT INTO items(item, status, reminder) VALUES(?,?,?)',
('go to meseum','not started', True)
)
cursor  = connection.cursor()
cursor.execute('INSERT INTO items(item, status, reminder) VALUES(?,?,?)',
('complete assignments','in progress', True)
)
connection.commit()
connection.close()



