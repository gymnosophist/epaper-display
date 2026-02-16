import os 
from dotenv import load_dotenv

load_dotenv() 

api_key = os.getenv('OPEN_WEATHER_API_KEY')


print(api_key)