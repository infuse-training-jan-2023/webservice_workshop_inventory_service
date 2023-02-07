def update_item(cursor,id,new_item):
    try:
        print(id)
        print(new_item)
        result=cursor.execute("UPDATE inventory SET item =? WHERE id =?",(new_item,id))
        return " updated successfully"
    except Exception as e:
        return e

