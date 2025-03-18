from fastapi import APIRouter
from services import get_reuters_news, convert_currency, get_weather

router = APIRouter()

@router.get("/reuters-news")
async def reuters_news():
    return await get_reuters_news()

@router.get("/convert-currency")
async def currency_converter(from_currency: str, to_currency: str, amount: float):
    return await convert_currency(from_currency, to_currency, amount)

@router.get("/weather/{city}")
async def weather(city: str):
    return await get_weather(city)
