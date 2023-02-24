def update_record(cursor,data):
    try:
        new_data = data['new_data']
        field = data['field']
        id = data['id']
        if(field=='container'):
            cursor.execute("UPDATE inventory SET container_name =? WHERE id =?",(new_data,id))
            return "container updated successfully"

        cursor.execute("UPDATE inventory SET item =? WHERE id =?",(new_data,id))
        return "item updated successfully"
    except Exception as e:
        return e



