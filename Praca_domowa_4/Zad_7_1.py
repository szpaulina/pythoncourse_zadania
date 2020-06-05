"""
Napisz program wyświetlający pogodę dla wskazanej przez użytkownika lokalizacji.
Skorzystaj z modułu urllib.request, json oraz API MetaWeather.
"""

import json
import urllib.request
from urllib.request import Request

lokalizacja = input("Podaj lokalizację: ")

url = f"https://www.metaweather.com/api/location/search/?query={lokalizacja}"

zapytanie = Request(url)
with urllib.request.urlopen(zapytanie) as req:
    wynik = json.loads(req.read())
    woeid = wynik[0]['woeid']

url2 = f"https://www.metaweather.com/api/location/{woeid}/"

zapytanie2 = Request(url2)
with urllib.request.urlopen(zapytanie2) as req2:
    wynik2 = json.loads(req2.read())
    data = wynik2["consolidated_weather"][0]["applicable_date"]
    pogoda = wynik2["consolidated_weather"][0]["weather_state_name"]
    print(f"Date: {data}")
    print(f"Weather: {pogoda}")