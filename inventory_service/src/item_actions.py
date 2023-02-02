from item_repository import ItemRepository

class ItemAction:
    def __init__(self):
        self.item_repo = ItemRepository()

    def get_all_items(self):
        try:
            items = self.item_repo.get_all_items()
            res = []
            for item in items:
                res.append({
                    'id':item[0],
                    'item':item[1],
                    'status':item[2],
                    'reminder':item[3]})
            return res
        except Exception as e:
            print(e)
            return {}
    # def add_item(self,item):
    #     try:
    #     except Exception as e:
    #         print(e)
    #         return {}

