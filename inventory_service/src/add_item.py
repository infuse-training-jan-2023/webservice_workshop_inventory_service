
def add_item(cursor, container_name , item):
    try:       
        insert_cursor = cursor.execute('insert into inventory(container_name, item) values(?,?)', (container_name, item ))
       
        return {
            'id': insert_cursor.lastrowid,
            'container_name':container_name,
            'item': item
        }
    except Exception as e:
      raise Exception('Error: ', e)