from fastapi import FastAPI
from app.Services.weather_service import get_weather_data


app = FastAPI()

@app.get("/weather/{city}")
def weather(city: str):
    result = get_weather_data(city)

    if not result:
        return {"error": "City not found"}

    return result
