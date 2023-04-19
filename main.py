# fish
# virtualenv venv
# source venv/bin/activate.fish
# pip install requests
# pip install python-dotenv
# pip freeze > requirements.txt
# переключить интерпритатор

# from pprint import pprint

import requests
from datetime import datetime
from os import getenv, system
from dotenv import load_dotenv
load_dotenv()



WEATHER_API = getenv("WEATHER_API")

def WeatherServise(get_city="Almaty", WEATHER_API = WEATHER_API):
    """Ваш бот-метеоролог мгновенно показывает погоду в любом городе, 
    предоставляя актуальную информацию о температуре воздуха, 
    влажности и вероятности дождя. 
    Это помогает планировать дела эффективнее и быть в курсе погодных событий в режиме реального времени.

    get_city = "Almaty"
    WEATHER_API = WEATHER_API

    WeatherServise(get_city, str, WEATHER_API, StrApikey) -> str
    """

    url = f"https://api.openweathermap.org/data/2.5/weather?q={get_city}&appid={WEATHER_API}&units=metric"

    response = requests.get(url)
    data = response.json()

    pr_day = datetime.fromtimestamp(data["sys"]["sunset"]) - datetime.fromtimestamp(data["sys"]["sunrise"])
    information = f"""Погода - Allabergen
    Страна: {data["sys"]["country"]}
    Город: {data ["name"]} - {data["weather"][0]["description"]} {data["clouds"]["all"]}%
    Температура: {data["main"]["temp"]}
    Ощущаеттся как: {data["main"]["feels_like"]}C
    Влажность: {data["main"]["humidity"]}
    Давление воздуха: {data["main"]["pressure"]}
    Скорость ветра: {data["wind"]["speed"]} м/с
    Направление ветра: {data["wind"]["deg"]}°
    Восход солнца: {datetime.fromtimestamp(data["sys"]["sunrise"])}
    Продолжительность дня: {pr_day}
    Закат солнца: {datetime.fromtimestamp(data["sys"]["sunset"])}
    """
    system("clear")
    return information

city = input("Ввелите название города: ")
print(WeatherServise(city))

# pprint(data)
# print(information)

