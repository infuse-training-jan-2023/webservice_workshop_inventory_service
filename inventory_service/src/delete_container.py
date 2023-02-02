def delete_container(cursor, container_name):
    try:  
        print(type(container_name))     
        first = container_name[0]
        print(first)
        return  cursor.execute('DELETE FROM inventory WHERE container_name like "?%"',(first))
    except Exception as e:
      raise Exception('Error: ', e)