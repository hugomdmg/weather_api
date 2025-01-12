from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    return jsonify({'message': 'hello world'})

@app.route('/api/post', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    return jsonify({'message': user_input + ' -> api'})


if __name__ == '__main__':
    app.run(debug=True, port=5000)
