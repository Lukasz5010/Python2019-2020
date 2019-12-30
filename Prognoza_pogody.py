import json
import urllib.request
from urllib.request import Request
miasto=input('Nasza pogoda przewiduje prognoze dla jednego z podanych miast: Warszawa, Berlin, Londyn, San Francisco. Podaj miasto w którym chcesz sprawdzic jaka jest pogoda:')
if miasto.lower()=='warszawa':
    url = f'https://www.metaweather.com/api/location/523920/'
elif miasto.lower()=='berlin':
    url=f'https://www.metaweather.com/api/location/638242/'
elif miasto.lower()=='londyn':
    url=f'https://www.metaweather.com/api/location/44418/'
elif miasto.lower()=='san francisco':
    url = f'https://www.metaweather.com/api/location/2487956/'
zapytanie = Request(url)
with urllib.request.urlopen(zapytanie) as req:
    zawartosc = json.loads(req.read())
    print('Stan pogody: ',zawartosc['consolidated_weather'][0]['weather_state_name'])
    print('Jest to prognoza na dzien: ', zawartosc['consolidated_weather'][0]['applicable_date'])
    print('Teperatura minimalna: ',zawartosc['consolidated_weather'][0]['min_temp'])
    print('Temperatura maksymalna: ',zawartosc['consolidated_weather'][0]['max_temp'])
    print('Predkosc wiatru ',zawartosc['consolidated_weather'][0]['wind_speed'], 'm/s')
    print('Cisnienie mierzone w hPa: ',zawartosc['consolidated_weather'][0]['air_pressure'])
    print('Wilgotnosc ',zawartosc['consolidated_weather'][0]['humidity'], '%')
    print('Przewidywalnosc prognozy ',zawartosc['consolidated_weather'][0]['predictability'])





