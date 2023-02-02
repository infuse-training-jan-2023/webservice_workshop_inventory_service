import sqlite3

class ItemRepository:
    DBPATH = './todo.db'

    @staticmethod
    def connect_db():

        return sqlite3.connect(ItemRepository.DBPATH)

    @staticmethod
    def get_all_items():
        try:
            conn = ItemRepository.connect_db()
            c = conn.cursor()
            rows = c.execute('SELECT * FROM items')
            return rows
        except Exception as e:
            raise Exception('Error: ',e)
    @staticmethod
    def add_item(item,reminder):
        try:
            conn = ItemRepository.connect_db()
            c = conn.cursor()
            item = c.execute('f INSERT INTO items (id,item,status,reminder) VALUES (?,?,?,?)',(item,'l','l','k'))
            item.commit()
            return {rows}
        except Exception as e:
            raise Exception('Error: ',e)

