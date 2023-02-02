from item_repository import ItemRepository

class ItemAction:
    def __init__(self):
        self.item_repo = ItemRepository()
    def display_items_actions(self):
        try:
            items = self.item_repo.display_items_repository()
            res = []
            for item in items:
                res.append({
                    'id':item[0],
                    'container_name':item[1],
                    'item':item[2]})
            return res
        except Exception as e:
            print(e)
            return {}


    def add_item_action(self,container_name , item):
        try:
            item = self.item_repo.add_item_repository(container_name , item)
            return item
        except Exception as e:
            print(e)
            return {}

    def delete_container_action(self,container_name):
        try:
            print(container_name)
            item = self.item_repo.delete_container_repository(container_name)
            return item
        except Exception as e:
            print(e)
            return {}

    def update_item_action(self,data):
        item_id = data['item_id']
        new_item = data['new_item']
        return self.item_repo.update_item_repository(item_id,new_item)
    def update_item_container_action(self,data):
        item_id = data['item_id']
        new_container = data['new_container']
        return self.item_repo.update_item_container_repository(item_id,new_container)
    def delete_item_action(self,item_id):
        return self.item_repo.delete_item_respository(item_id)
