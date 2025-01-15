from flask import Flask, request, jsonify
import requests
from src.weather import weather_blueprint, data_blueprint


app = Flask(__name__)
app.register_blueprint(weather_blueprint)
app.register_blueprint(data_blueprint)


API_KEY = 'e977d82fb6541dc8c4fbf8ada061c5ee'

@app.route('/', methods=['GET'])
def hello():
    return jsonify({'message': 'hello world'})

@app.route('/api/post', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    return jsonify({'message': user_input + ' -> api'})

@app.route('/api/delete', methods=['POST'])
def create():
    user = request.json.get('value')
    return jsonify({'value': user})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
