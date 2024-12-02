import requests
import json

BASE_URL = 'https://jsonplaceholder.typicode.com/'

# Отправляем GET-запрос к API
response = requests.get(BASE_URL)

# Выводим статус-код ответа
print('Статус:', response.status_code)

# Преобразуем заголовки в читаемый формат и выводим их
formatted_headers = json.dumps(dict(response.headers), indent=4, ensure_ascii=False)
print('Заголовки:\n', formatted_headers)
