import httpx
import os
from dotenv import load_dotenv
from httpx import HTTPError

# Загружаем переменные окружения
load_dotenv()

RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")

if not RAPIDAPI_KEY:
    raise ValueError("API ключ не найден в .env файле!")

HEADERS = {
    "x-rapidapi-key": RAPIDAPI_KEY
}

# 📌 Получение новостей Reuters
async def get_reuters_news():
    url = "https://reuters-business-and-financial-news.p.rapidapi.com/market-rics/list-rics-by-asset-and-category/1/1"
    headers = {**HEADERS, "x-rapidapi-host": "reuters-business-and-financial-news.p.rapidapi.com"}

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=headers)
            response.raise_for_status()
            return response.json()
    except HTTPError as e:
        return {"error": str(e)}

# 📌 Конвертация валют
async def convert_currency(from_currency: str, to_currency: str, amount: float):
    url = f"https://currency-converter5.p.rapidapi.com/currency/convert?format=json&from={from_currency}&to={to_currency}&amount={amount}&language=en"
    headers = {**HEADERS, "x-rapidapi-host": "currency-converter5.p.rapidapi.com"}

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=headers)
            response.raise_for_status()
            return response.json()
    except HTTPError as e:
        return {"error": str(e)}

# 📌 Получение погоды
async def get_weather(city: str):
    url = f"https://weather-api-by-any-city.p.rapidapi.com/weather/{city}"
    headers = {**HEADERS, "x-rapidapi-host": "weather-api-by-any-city.p.rapidapi.com"}

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=headers)
            response.raise_for_status()
            return response.json()
    except HTTPError as e:
        return {"error": str(e)}
