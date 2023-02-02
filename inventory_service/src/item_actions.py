from item_repository import ItemRepository

class ItemAction:
    def __init__(self):
        self.item_repo = ItemRepository()



































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
