import requests
from app.config import API_KEY,BASE_URL


def get_weather_data(city:str):
    params ={
        "q":city,
        "appid":API_KEY,
        "units":"metric"
    }

    response= requests.get(BASE_URL,params=params)
    data = response.json()

    if data.get("cod")!= 200:
        return None

    return {
        "city":city,
        "temperature":data["main"]["temp"],
        "feels_like":data["main"]["feels_like"],
        "weather":data["weather"][0]["description"]
    }