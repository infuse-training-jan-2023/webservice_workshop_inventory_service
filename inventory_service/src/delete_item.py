def delete_item(cursor,item_id):
    try:
        result = cursor.execute('DELETE FROM inventory WHERE id=?',(item_id))
        return "deletion successful"
    except Exception as e:
        return e

