from flask import Flask, jsonify, request

app = Flask(__name__)

items = {
    'item1': {
        'name': 'essential T-shirt ',
        'category': '1',
        'price': 20.5,
        'instock': 200
    }
}

# GET operation
@app.route('/items/<string:item_name>', methods=['GET'])
def get_item(item_name):
    if item_name in items:
        return jsonify(items[item_name])
    else:
        return jsonify({'error': 'Item not found'})

# DELETE operation
@app.route('/items/<string:item_name>', methods=['DELETE'])
def delete_item(item_name):
    if item_name in items:
        del items[item_name]
        return jsonify({'message': 'Item deleted'})
    else:
        return jsonify({'error': 'Item not found'})

# PUT operation
@app.route('/items/<string:item_name>', methods=['PUT'])
def update_item(item_name):
    if item_name in items:
        item = items[item_name]
        item['name'] = request.json['name']
        item['category'] = request.json['category']
        item['price'] = request.json['price']
        item['instock'] = request.json['instock']
        return jsonify({'message': 'Item updated'})
    else:
        return jsonify({'error': 'Item not found'})

# UPDATE operation
@app.route('/items/<string:item_name>', methods=['PATCH'])
def update_partial_item(item_name):
    if item_name in items:
        item = items[item_name]
        if 'name' in request.json:
            item['name'] = request.json['name']
        if 'category' in request.json:
            item['category'] = request.json['category']
        if 'price' in request.json:
            item['price'] = request.json['price']
        if 'instock' in request.json:
            item['instock'] = request.json['instock']
        return jsonify({'message': 'Item updated'})
    else:
        return jsonify({'error': 'Item not found'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
