def delete_container(cursor, container_name):
    try:
        cursor.execute('DELETE FROM inventory WHERE container_name=?',(container_name,))
        return "container deleted successfully"
    except Exception as e:
      raise Exception('Error: ', e)
      
