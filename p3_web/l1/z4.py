import json
import os
from typing import Dict, Any


def get_user_data() -> Dict[str, Any]:
    """Запрашивает данные пользователя и возвращает словарь с этими данными."""
    name = input("Введите имя: ")
    age = input("Введите возраст: ")
    email = input("Введите email: ")
    return {"name": name, "age": age, "email": email}


def save_to_json(filename: str, data: Dict[str, Any]) -> None:
    """Сохраняет данные в JSON файл.

    :param filename: Имя файла, в который будут сохранены данные.
    :param data: Данные, которые нужно сохранить в формате JSON.
    """
    with open(filename, 'w') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def load_from_json(filename: str) -> Dict[str, Any]:
    """Загружает данные из JSON файла.

    :param filename: Имя файла, откуда будут загружены данные.
    :return: Загруженные данные в виде словаря.
    """
    with open(filename, 'r') as f:
        return json.load(f)


def main() -> None:
    """Основная функция для выполнения программы."""
    filename = 'user.json'
    user_data = get_user_data()
    if not os.path.exists(filename):
        print("Файл не найден, создаю новый.")
    save_to_json(filename, user_data)
    loaded_data = load_from_json(filename)
    print("Загруженные данные:", loaded_data)


if __name__ == '__main__':
    main()
