def delete_container(cursor, container_name):
    try:  
        print(type(container_name))     
        return  cursor.execute("DELETE FROM inventory WHERE container_name = ? ",(container_name,))
    except Exception as e:
      raise Exception('Error: ', e)