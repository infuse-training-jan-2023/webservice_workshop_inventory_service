import sqlite3
from update_record import update_record
from delete_item import delete_item
from add_item import add_item
from display_items import display_all
from delete_container import delete_container


class ItemRepository:
    DBPATH = '../inventory.db'
    connection = None

    @staticmethod
    def connect_db():
        return ItemRepository.connection if ItemRepository.connection is not None else sqlite3.connect(ItemRepository.DBPATH)

    @staticmethod
    def update_item_repository(item_id,new_item):
        conn = ItemRepository.connect_db()
        cursor = conn.cursor()
        data = {"id":item_id,"field":'item',"new_data":new_item}
        result = update_record(cursor,data)
        conn.commit()
        return result

    @staticmethod
    def update_item_container_repository(item_id,new_container):
        conn = ItemRepository.connect_db()
        cursor = conn.cursor()
        data = {"id":item_id,"field":'container',"new_data":new_container}
        result = update_record(cursor,data)
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

