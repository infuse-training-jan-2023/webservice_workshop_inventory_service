from flask import Flask,Response,request
from item_actions import ItemAction
import json

app = Flask(__name__)
actions = ItemAction()

@app.route('/update/item', methods=['GET','POST'])
def update_item_inventory():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json_data = request.json

        return actions.update_item_action(json_data)
    else:
        return 'Content-Type not supported!'
@app.route('/update/container', methods=['GET','POST'])
def udpate_item_container_inventory():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json_data = request.json
        return actions.update_item_container_action(json_data)
    else:
        return 'Content-Type not supported!'
@app.route('/delete/<item_id>', methods=['GET','POST'])
def delete_item_inventory(item_id):
    return actions.delete_item_action(item_id)

@app.route('/display',methods = ['GET'])
def diaplay_all_items():
    items = actions.display_items_actions()
    return Response(json.dumps(items),mimetype='application/json', status=200)

@app.route('/add/item', methods=['POST'])
def add_item():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json_data = request.json
        return actions.add_item_action(json_data)
    else:
        return 'Content-Type not supported!'

@app.route('/delete/container/<container_name>',methods = ['POST','GET'])
def delete_container(container_name):
    items = actions.delete_container_action(container_name)
    return items
if __name__ == '__main__':
    app.run(debug=True,host = '127.0.0.1',port = 4000)
