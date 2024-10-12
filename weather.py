import requests
from  dotenv import load_dotenv
from pprint import pprint
import os

load_dotenv()

def get_weather(city="Jessore"):

    request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric'

    weather = requests.get(request_url).json()

    return weather

if __name__ == "__main__":
    city = input("Enter City: ")    
    if not bool(city.strip()):
        city="London"
    pprint(get_weather(city))