import json
import chardet


def read_json(filename: str):
    with open(filename, 'rb') as f:
        rawdata = f.read()  # Читаем данные в бинарном режиме

    result = chardet.detect(rawdata)  # Определяем кодировку
    encoding = result['encoding']  # Получаем кодировку

    with open(filename, 'r', encoding=encoding) as f:
        data = json.load(f)  # Загружаем данные JSON
        return data


if __name__ == '__main__':  # Исправлено имя проверки
    filename = 'files/data.json'  # Путь к файлу
    all_books = read_json(filename)  # Читаем данные из файла
    min_year = int(input('Введите, с какого года вывести книги: '))  # Ввод года
    authors = set()  # Используем множество для уникальных авторов

    # Ищем авторов, у которых год издания больше или равен введенному
    for row in all_books:
        if int(row['year']) >= min_year:
            authors.add(row['author'])

    # Выводим уникальных авторов
    print("Авторы книг, изданных с ", min_year, " года:")
    print(authors)
