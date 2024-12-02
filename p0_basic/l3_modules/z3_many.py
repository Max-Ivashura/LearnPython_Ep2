import json
import math
import random
import requests

key = '21e04b545c5dfca6923117c0a4b1007f'
city = 'Dmitrov'

pi = math.pi
print(f'{pi:.2f}')

rand = random.random()
print(rand)

try:
    url = (f'https://api.openweathermap.org/data/2.5/'
           f'weather?q={city}&units=metric&lang=ru&appid={key}')
    weather_data = requests.get(url).json()
    weather_data_structure = json.dumps(weather_data, indent=2)

    # получаем данные о температуре и о том, как она ощущается
    temperature = round(weather_data['main']['temp'])
    temperature_feels = round(weather_data['main']['feels_like'])

    # выводим значения на экран
    print('Сейчас в городе', city, str(temperature), '°C')
    print('Ощущается как', str(temperature_feels), '°C')
except Exception as e:
    print('Ошибка:', e)

