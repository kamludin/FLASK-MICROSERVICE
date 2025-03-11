from flask import Flask, jsonify, request

app = Flask(__name__)

items = []

# Root route
@app.route('/')
def home():
    return "Welcome to the Flask API!"

@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

@app.route('/items', methods=['POST'])
def add_item():
    item = request.json
    items.append(item)
    return jsonify(item), 201
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
