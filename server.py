from flask import Flask, request, jsonify
import requests
from src.weather import coord_weather_blueprint, city_weather_blueprint

app = Flask(__name__)
app.register_blueprint(coord_weather_blueprint)
app.register_blueprint(city_weather_blueprint)


@app.route('/', methods=['GET'])
def hello():
    return jsonify({'message': 'hello from weather api'})




if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
