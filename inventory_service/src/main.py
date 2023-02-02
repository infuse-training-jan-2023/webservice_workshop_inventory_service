from flask import Flask,Response,request
from item_actions import ItemAction
import json

app = Flask(__name__)
actions = ItemAction()
@app.route('/items',methods = ['GET'])
def  get_all_items():
    items = actions.get_all_items()
    return Response(json.dumps(items),mimetype='application/json', status=200)
from flask import Flask, request

@app.route('/post_item', methods=['POST'])
def process_json():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json_data = request.json
        actions.add_item(json_data)
        return "added"
    else:
        return 'Content-Type not supported!'

if __name__ == '__main__':
    app.run(debug=True,host = '127.0.0.1',port = 4000)
