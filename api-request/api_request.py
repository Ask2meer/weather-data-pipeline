import os
from dotenv import load_dotenv
import requests 

# Load variables from .env
load_dotenv()


api_key = os.getenv("WEATHERSTACK_API_KEY")
api_url = f"http://api.weatherstack.com/current?access_key={api_key}&query=New York"

def fetch_data():
    print("Fetching Weather Data From Weatherstack API ")
    try:
        response = requests.api.get(api_url)
        response.raise_for_status()
        print("API response recieved succesfully...")
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An Error Occured: {e}")
        raise




#def mock_data_fetch():
    #return {'request': {'type': 'City', 'query': 'New York, United States of America', 'language': 'en', 'unit': 'm'}, 'location': {'name': 'New York', 'country': 'United States of America', 'region': 'New York', 'lat': '40.714', 'lon': '-74.006', 'timezone_id': 'America/New_York', 'localtime': '2025-11-05 03:49', 'localtime_epoch': 1762314540, 'utc_offset': '-5.0'}, 'current': {'observation_time': '08:49 AM', 'temperature': 8, 'weather_code': 116, 'weather_icons': ['https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0004_black_low_cloud.png'], 'weather_descriptions': ['Partly cloudy'], 'astro': {'sunrise': '06:31 AM', 'sunset': '04:47 PM', 'moonrise': '04:34 PM', 'moonset': '06:40 AM', 'moon_phase': 'Full Moon', 'moon_illumination': 99}, 'air_quality': {'co': '338.85', 'no2': '47.75', 'o3': '9', 'so2': '7.85', 'pm2_5': '13.25', 'pm10': '13.75', 'us-epa-index': '1', 'gb-defra-index': '1'}, 'wind_speed': 12, 'wind_degree': 268, 'wind_dir': 'W', 'pressure': 1021, 'precip': 0, 'humidity': 47, 'cloudcover': 75, 'feelslike': 6, 'uv_index': 0, 'visibility': 16, 'is_day': 'no'}}
