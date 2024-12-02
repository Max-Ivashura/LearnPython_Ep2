import sqlite3

# Подключение к базе данных или создание новой
conn = sqlite3.connect('sales.db')
cursor = conn.cursor()

# Создание таблицы sales
cursor.execute('''
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_name TEXT NOT NULL,
    quantity INTEGER NOT NULL,
    price REAL NOT NULL
)
''')


# Функция для добавления продаж
def add_sale(product_name: str, quantity: int, price: float) -> None:
    """Добавляет запись о продаже в таблицу sales."""
    cursor.execute('''
    INSERT INTO sales (product_name, quantity, price) 
    VALUES (?, ?, ?)
    ''', (product_name, quantity, price))
    conn.commit()
    print(f"Продажа добавлена: {product_name}, Количество: {quantity}, Цена: {price}")


# Функция для получения отсортированного списка товаров
def get_sorted_sales() -> None:
    """Получает и выводит список товаров, отсортированных по количеству продаж."""
    cursor.execute('''
    SELECT product_name, SUM(quantity) as total_quantity
    FROM sales
    GROUP BY product_name
    ORDER BY total_quantity DESC
    ''')

    rows = cursor.fetchall()

    print("\nСписок товаров, отсортированных по количеству продаж:")
    for row in rows:
        print(f"{row[0]}: {row[1]}")


# Основной блок программы
if __name__ == "__main__":
    # Удаляем все данные перед запуском (для тестирования)
    cursor.execute('DELETE FROM sales')

    # Добавление данных о продажах
    add_sale("Ноутбук", 5, 800.00)
    add_sale("Смартфон", 10, 300.00)
    add_sale("Планшет", 3, 400.00)
    add_sale("Ноутбук", 2, 800.00)  # Дополнительная продажа ноутбука
    add_sale("Смартфон", 4, 300.00)  # Дополнительная продажа смартфона

    # Получение и вывод отсортированного списка продаж
    get_sorted_sales()

    # Закрытие соединения
    conn.close()
