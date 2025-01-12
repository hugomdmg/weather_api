from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET'])
def hello():
    return jsonify({'message': 'hello world'})


@app.route('/api/post', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    return jsonify({'message': user_input+' -> api'})



if __name__ == '__main__':
    app.run(debug=True, port=5000)