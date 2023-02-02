def update_item_container(cursor,id,new_container):
    try:
        print(id)
        result = cursor.execute("UPDATE inventory SET container_name =? WHERE id =?",(new_container,id))
        return "container updated successfully"
    except Exception as e:
        return e

