class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f'Инфо о машине: {self.make}, {self.model}, {self.year}')


# Создание объектов класса Car
car_1 = Car('Tesla', 'X', 2024)
car_2 = Car('Honda', 'Civic', 1999)
car_3 = Car('Mazda', 'CX-5', 2021)

# Вывод информации о каждой машине
car_1.display_info()
car_2.display_info()
car_3.display_info()
