import sqlite3

from tabulate import tabulate


def table_exists(cursor, table_name: str) -> bool:
    """Проверяет, существует ли таблица в базе данных."""
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table_name,))
    return cursor.fetchone() is not None


def create(cursor) -> None:
    """Создаёт таблицу книг."""
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            published_year INTEGER NOT NULL
        )
    ''')


def insert(cursor, books: list) -> None:
    """Вставляет записи о книгах"""
    cursor.executemany('''
        INSERT INTO books (title, author, published_year) 
        VALUES (?, ?, ?)
    ''', books)


def select(cursor) -> list:
    """Запрашивает все записи о книгах"""
    cursor.execute('SELECT * FROM books')
    return cursor.fetchall()


def initial_db(cursor):
    """Инициализирует базу данных, создаёт таблицу и вставляет данные, если таблицы не существует."""
    if not table_exists(cursor, 'books'):
        create(cursor)
        books_for_insert = [
            ('1984', 'George Orwell', 1949),
            ('To Kill a Mockingbird', 'Harper Lee', 1960),
            ('The Great Gatsby', 'F. Scott Fitzgerald', 1925),
            ('Moby Dick', 'Herman Melville', 1851),
            ('Pride and Prejudice', 'Jane Austen', 1813),
            ('War and Peace', 'Leo Tolstoy', 1869),
            ('The Catcher in the Rye', 'J.D. Salinger', 1951),
            ('Brave New World', 'Aldous Huxley', 1932),
            ('The Hobbit', 'J.R.R. Tolkien', 1937),
            ('Fahrenheit 451', 'Ray Bradbury', 1953)
        ]
        insert(cursor, books_for_insert)
    else:
        print("Таблица 'books' уже существует. Вставка данных пропущена.")


def print_db(cursor):
    headers = ['ID', 'Title', 'Author', 'Published Year']
    data = select(cursor)
    print("Книги в базе данных:")
    print(tabulate(data, headers=headers, tablefmt='psql'))


if __name__ == '__main__':
    conn = None
    try:
        conn = sqlite3.connect('books.db')
        cursor = conn.cursor()

        initial_db(cursor)
        print_db(cursor)
    except sqlite3.Error as e:
        print(f"Ошибка при работе с базой данных: {e}")
    finally:
        if conn:
            conn.close()
