import requests
from requests import Response, RequestException


def get_request(url: str) -> Response:
    """Отправляет GET-запрос по указанному URL и возвращает ответ.

    :param url: URL, к которому будет отправлен запрос.
    :return: Response объект или None в случае ошибки.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Поднимает исключение для ошибок HTTP
        return response
    except RequestException as e:
        print(f"Ошибка при выполнении GET-запроса: {e}")
        return None


def main() -> None:
    """Основная функция для выполнения программы."""
    url = 'https://random.ru/api'  # Некорректный URL (например, неправильный протокол или отсутствующий сервис)

    response = get_request(url)
    if response:
        print("Запрос выполнен успешно!")
        print("Ответ:", response.text)
    else:
        print("Запрос не удался.")


if __name__ == '__main__':
    main()
