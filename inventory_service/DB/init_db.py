import sqlite3
connection = sqlite3.connect('inventory.db')
with open('DB/schema.sql') as f:
    connection.executescript(f.read())

cursor  = connection.cursor()
cursor.execute('INSERT INTO inventory(container_name, item) VALUES(?,?)',
('electronics','phone')
)
connection.commit()
connection.close()






