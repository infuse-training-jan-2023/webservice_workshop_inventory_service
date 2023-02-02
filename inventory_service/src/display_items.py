def display_all(cursor):
    try:
      rows = cursor.execute('select * from inventory')
      return rows
    except Exception as e:
      raise Exception('Error: ', e)