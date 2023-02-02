import sqlite3
from add_item import add_item
from display_items import display_all
from delete_container import delete_container

class ItemRepository:
    DBPATH = './inventory.db'

    @staticmethod
    def connect_db():

        return sqlite3.connect(ItemRepository.DBPATH)

    @staticmethod
    def display_items_repository():
        conn = ItemRepository.connect_db()
        cursor = conn.cursor()
        return  display_all(cursor)
        


    @staticmethod
    def add_item_repository(container_name,item ):
        conn = ItemRepository.connect_db()
        cursor = conn.cursor()
        data= add_item(cursor, container_name ,item)
        conn.commit()
        return data

    @staticmethod
    def delete_container_repository(container_name):
        conn = ItemRepository.connect_db()
        cursor = conn.cursor()
        data= delete_container(cursor, container_name )
        conn.commit()
        return data

        