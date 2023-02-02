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

