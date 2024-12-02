import csv


class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def to_row(self):
        return [self.name, self.price]

    def __str__(self):
        return f"{self.name} — {self.price}"


def save_to_csv(filename, products):
    with open(filename, "w", newline='', encoding='cp1251') as f:
        csv_writer = csv.writer(f)
        for product in products:
            csv_writer.writerow(product.to_row())


def load_from_csv(filename):
    products = []
    with open(filename, "r", newline='', encoding='cp1251') as f:
        csv_reader = csv.reader(f)
        for row in csv_reader:
            products.append(Product(row[0], float(row[1])))
    return products


if __name__ == '__main__':
    filename = "files/products.csv"
    products = [
        Product("Product_1", 32),
        Product("Product_2", 50),
        Product("Product_3", 41),
    ]

    # Сохранение продуктов в CSV
    save_to_csv(filename, products)

    # Загрузка продуктов из CSV
    products = load_from_csv(filename)

    # Получение минимальной цены от пользователя
    try:
        min_price = float(input("Введите минимальную цену для фильтрации товаров: "))
    except ValueError:
        print("Ошибка: введите корректное число.")
        exit(1)

    # Фильтрация продуктов по минимальной цене
    filtered_products = [product for product in products if product.price >= min_price]

    # Вывод отфильтрованных результатов
    print("Отфильтрованные товары:")
    for product in filtered_products:
        print(product)
