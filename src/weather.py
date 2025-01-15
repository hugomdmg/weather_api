from flask import Blueprint, jsonify
import requests


API_KEY = 'e977d82fb6541dc8c4fbf8ada061c5ee'


coordinates = [
    {"lat": 40.7128, "lon": -74.0060},  # Nueva York
    {"lat": 34.0522, "lon": -118.2437}, # Los Ángeles
    {"lat": 51.5074, "lon": -0.1278},   # Londres
    {"lat": -33.8688, "lon": 151.2093},  # Sídney
    {"lat": 41.0000, "lon": -3.0000}  # Madrid
]

weather_blueprint = Blueprint('weather', __name__)

@weather_blueprint.route('/weather', methods=['GET'])
def get_weather():
    weather_data = []
    
    for coord in coordinates:
        url = f"http://api.openweathermap.org/data/2.5/weather?lat={coord['lat']}&lon={coord['lon']}&appid={API_KEY}&units=metric"
        
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            weather_data.append({
                'city': data['name'],
                'temperature': f"{data['main']['temp']}°C",
                'weather': data['weather'][0]['description'],
                'coordinates': coord
            })
        else:
            weather_data.append({
                'error': 'No se pudo obtener el clima para esta ubicación.',
                'coordinates': coord
            })
    
    return jsonify(weather_data)



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
