from flask import Flask, request, jsonify
import requests
from src.weather import weather_blueprint


app = Flask(__name__)
app.register_blueprint(weather_blueprint)


API_KEY = 'e977d82fb6541dc8c4fbf8ada061c5ee'
CITY = "London"


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


@app.route('/data', methods=['GET'])
def data():
    url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        
        weather_description = data['weather'][0]['description']
        temperature = data['main']['temp']
        
        return jsonify({
            'message': 'hello world',
            'city': CITY,
            'temperature': f"{temperature}°C",
            'weather': weather_description
        })
    else:
        return jsonify({
            'error': 'No se pudo obtener el clima. Verifica la clave API o la ciudad.'
        })

# coordinates = [
#     {"lat": 40.7128, "lon": -74.0060},  # Nueva York
#     {"lat": 34.0522, "lon": -118.2437}, # Los Ángeles
#     {"lat": 51.5074, "lon": -0.1278},   # Londres
#     {"lat": -33.8688, "lon": 151.2093},  # Sídney
#     {"lat": 41.0000, "lon": -3.0000}  # Madrid
# ]

# @app.route('/weather', methods=['GET'])
# def get_weather():
#     weather_data = []
    
#     for coord in coordinates:
#         url = f"http://api.openweathermap.org/data/2.5/weather?lat={coord['lat']}&lon={coord['lon']}&appid={API_KEY}&units=metric"
        
#         response = requests.get(url)
        
#         if response.status_code == 200:
#             data = response.json()
#             weather_data.append({
#                 'city': data['name'],
#                 'temperature': f"{data['main']['temp']}°C",
#                 'weather': data['weather'][0]['description'],
#                 'coordinates': coord
#             })
#         else:
#             weather_data.append({
#                 'error': 'No se pudo obtener el clima para esta ubicación.',
#                 'coordinates': coord
#             })
    
#     return jsonify(weather_data)



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
