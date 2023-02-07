import sqlite3
from update_item import update_item
from update_item_container import update_item_container
from delete_item import delete_item
from add_item import add_item
from display_items import display_all
from delete_container import delete_container


class ItemRepository:
    DBPATH = './inventory.db'

    @staticmethod
    def connect_db():
        return sqlite3.connect(ItemRepository.DBPATH)

    @staticmethod
    def update_item_repository(item_id,new_item):
        conn = ItemRepository.connect_db()
        cursor = conn.cursor()
        result = update_item(cursor,item_id,new_item)
        conn.commit()
        return result
        
    @staticmethod
    def update_item_container_repository(item_id,new_container):
        conn = ItemRepository.connect_db()
        cursor = conn.cursor()
        result =  update_item_container(cursor,item_id,new_container)
        conn.commit()
        return result

    @staticmethod
    def delete_item_respository(item_id):
        conn = ItemRepository.connect_db()
        cursor = conn.cursor()
        result = delete_item(cursor,item_id)
        conn.commit()
        return result

    @staticmethod
    def display_items_repository():
        conn = ItemRepository.connect_db()
        cursor = conn.cursor()
        return  display_all(cursor)

    @staticmethod
    def add_item_repository(container_name,item):
        conn = ItemRepository.connect_db()
        cursor = conn.cursor()
        data= add_item(cursor,container_name,item)
        conn.commit()
        return data

    @staticmethod
    def delete_container_repository(container_name):
        conn = ItemRepository.connect_db()
        cursor = conn.cursor()
        data= delete_container(cursor, container_name )
        conn.commit()
        return data

