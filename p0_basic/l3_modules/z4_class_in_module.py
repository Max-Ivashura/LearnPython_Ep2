# main.py
import shapes

# Запрос радиуса у пользователя
radius = float(input("Введите радиус круга: "))  # Преобразуем ввод пользователя в float
circle = shapes.Circle(radius)  # Создаем объект Circle с введенным радиусом

# Выводим на экран площадь и длину окружности
print(f'Площадь круга: {circle.area():.2f} квадратных единиц')  # Выводим площадь, округляя до 2 знаков после запятой
print(f'Длина окружности: {circle.circumference():.2f} единиц')  # Выводим длину окружности, округляя до 2 знаков после запятой
