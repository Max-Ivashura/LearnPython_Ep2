import json


class Product:
    def __init__(self, name: str, category: str, price: float):
        self.name = name
        self.category = category
        self.price = price

    def update_price(self, price: float):
        self.price = price

    def to_dict(self):
        return {
            "name": self.name,
            "category": self.category,
            "price": self.price
        }


def load_from_json(filename: str):
    try:
        with open(filename, "r", encoding='cp1251') as f:
            data = json.load(f)
            return [Product(**item) for item in data]  # Используем распаковку словарей
    except FileNotFoundError:
        print(f"Файл {filename} не найден.")
        return []
    except json.JSONDecodeError:
        print("Ошибка чтения JSON файла.")
        return []


def save_to_json(filename: str, products: list[Product]):
    with open(filename, "w", encoding='cp1251') as f:
        json.dump([product.to_dict() for product in products], f, indent=4, ensure_ascii=False)


def main():
    filename = "files/inventory.json"
    products = load_from_json(filename)

    if not products:
        print("Список товаров пуст.")
        return

    name_to_reprice = input("Введите название товара для обновления цены: ")

    # Проверка наличия введенного продукта в списке
    product_found = False
    for product in products:
        if product.name == name_to_reprice:
            new_price = float(input("Введите новую цену для товара: "))  # Преобразуем ввод в float
            print(f"Обновление цены: {product.price} на {new_price}")
            product.update_price(new_price)
            product_found = True
            break

    if not product_found:
        print("Товар не найден.")
        return

    save_to_json(filename, products)
    print("Изменения сохранены.")


if __name__ == '__main__':
    main()
