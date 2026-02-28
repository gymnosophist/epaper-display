import requests # query the api  
import os # get env variables 
from dotenv import load_dotenv # load api key, environment variables 
from datetime import datetime # parse unix timestamps 

# load api key 
load_dotenv() 

api_key = os.getenv("OPEN_WEATHER_API_KEY")
LAT = os.getenv("LAT")
LON = os.getenv('LON')

url = f'https://api.openweathermap.org/data/3.0/onecall?lat={LAT}&lon={LON}&appid={api_key}&units=imperial'

def get_weather(): 
    """
    calls the openweather api and gets current weather for specified location. 
    """
    response = requests.get(url)
    if response.status_code == 200: 
        print('success')
        return response.json()
    else:
        print(f'Error {response.status_code}')
        return None 

def parse_forecast(raw_data):  
    """
    Parses dictionary of openweather api results. 
    Returns dict of forecast results 
    """
    parsed = {
        'current': {
            'temp': raw_data['current']['temp'],
            'icon': raw_data['current']['weather'][0]['icon'], 
            'id': raw_data['current']['weather'][0]['id'],
            'description': raw_data['current']['weather'][0]['description'].title() # title case 
        }, 
        "hourly": [ # use this to draw chart 
            {
                "dt": hour['dt'],
                "temp": hour['temp'],
                "pop": hour.get('pop', 0) # Probability of Precipitation
            } for hour in raw_data['hourly'][:24] # Next 24 hours
        ],
        'daily': [ # use this to populate forecast 
            {
                'dt': day['dt'],
                'high_temp' : round(day['temp']['max']),
                'low_temp'  : round(day['temp']['min']),
                "id": day['weather'][0]['id'],
                "icon": day['weather'][0]['icon']
                } 
                for day in raw_data['daily']
            ]
            } 
    return parsed 

def get_icon_from_weather(condition_id, icon_code):
    """
    Gets current conditions from forecast, grabs icon from `assets` foler. 
    :param condition_id: The 3-digit ID (e.g., 800)
    :param icon_code: The 3-char code (e.g., '01n')
    :return: String filename (e.g., 'wi-night-clear.png')
    """



    return None 



# mapping function for openweather icons 
# removing this for the time being 
# def get_weather_style(weather_id):
#     """
#     Returns (icon_filename, color_tuple) based on OWM Weather ID
#     """
#     # Thunderstorm
#     if 200 <= weather_id <= 232:
#         return ("wi-thunderstorm.png", (255, 0, 0)) # Red
#     # Drizzle / Rain
#     elif 300 <= weather_id <= 531:
#         return ("wi-rain.png", (0, 0, 255)) # Blue
#     # Snow
#     elif 600 <= weather_id <= 622:
#         return ("wi-snow.png", (255, 255, 255)) # White (with black border)
#     # Clear
#     elif weather_id == 800:
#         return ("wi-day-sunny.png", (255, 165, 0)) # Orange
#     # Clouds
#     elif 801 <= weather_id <= 804:
#         return ("wi-cloudy.png", (128, 128, 128)) # Gray
    
#     return ("wi-na.png", (0, 0, 0)) # Default/Fallback