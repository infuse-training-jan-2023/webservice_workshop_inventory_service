from flask import Flask,Response,request
from item_actions import ItemAction
import json

app = Flask(__name__)
actions = ItemAction()

@app.route('/display',methods = ['GET'])
def diaplay_all_items():
    items = actions.display_items_actions()
    return Response(json.dumps(items),mimetype='application/json', status=200)

@app.route('/add/electronics/<value>', methods=['POST'])
def add_item(value):
    added_item = actions.add_item_action("Electronics",value)
    if added_item == {}:
        return Response("{'error': 'Erro addding the item'}", mimetype='application/json', status=500)
    return Response(json.dumps(added_item), mimetype='application/json', status=201)

@app.route('/delete/container/<container_name>',methods = ['POST','GET'])
def delete_container(container_name):
    items = actions.delete_container_action(container_name)
    return items

































if __name__ == '__main__':
    app.run(debug=True,host = '127.0.0.1',port = 4000)
