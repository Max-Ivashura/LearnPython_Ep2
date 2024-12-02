import json


class Book():
    def __init__(self, name: str, author: str, release_year: int, price: float):
        self.name = name
        self.author = author
        self.release_year = release_year
        self.price = price

    def to_dict(self):
        """Метод для преобразования объекта в словарь."""
        return {
            'name': self.name,
            'author': self.author,
            'release_year': self.release_year,
            'price': self.price
        }


def write_books_to_json(filename: str, books: list[Book]):
    """Записывает список книг в JSON файл."""
    with open(filename, "w") as f:
        json.dump([book.to_dict() for book in books], f, indent=4)


def read_books_from_json(filename: str):
    """Читает книги из JSON файла и выводит их на экран."""
    with open(filename, "r") as f:
        books = json.load(f)
        for book in books:
            print(f'Название: {book["name"]}, '
                  f'Автор: {book["author"]}, '
                  f'Год издания: {book["release_year"]}, '
                  f'Цена: {book["price"]}')


if __name__ == '__main__':
    filename = 'files/data.json'  # Имя файла, в который будем сохранять информацию
    # Создание списка книг
    books = [
        Book('1984', 'Джордж Оруэлл', 1949, 15.99),
        Book('Убить пересмешника', 'Харпер Ли', 1960, 10.99),
        Book('Гордость и предубеждение', 'Джейн Остин', 1813, 12.50),
        Book('Мастер и Маргарита', 'Михаил Булгаков', 1967, 5.99)
    ]
    write_books_to_json(filename, books)  # Запись книг в JSON файл
    read_books_from_json(filename)  # Чтение книг из JSON файла и вывод их на экран
