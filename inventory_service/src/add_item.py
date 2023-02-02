def add_item(cursor,container_name,item):
    try:
        insert_cursor = cursor.execute('insert into inventory (container_name, item) values (?,?)', (container_name,item))
        return 'item added successfully'
    except Exception as e:
      raise Exception('Error: ', e)
