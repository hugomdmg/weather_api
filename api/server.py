from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def hello():
    return jsonify({'message': 'hello world'})

@app.route('/api/post', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    return jsonify({'message': user_input + ' -> api'})


def handler(request):
    with app.app_context():
        return app.full_dispatch_request()

# if __name__ == '__main__':
#     app.run(debug=True, port=5000) 