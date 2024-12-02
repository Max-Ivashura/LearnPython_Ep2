"""
Задание 8: Создайте функцию calculate_area, которая принимает два параметра: width и height.
Функция должна возвращать площадь прямоугольника. Вызовите функцию и выведите результат на экран.
"""


def calculate_area(width, height):
    if isinstance(width, (int, float)) and isinstance(height, (int, float)):
        return width * height
    else:
        print("Ошибка: оба параметра должны быть числами.")
        return None


# Вызов функции и вывод результата на экран
area = calculate_area(100, 50)
if area is not None:
    print(f"Площадь прямоугольника: {area}")

print(calculate_area(20, 30))  # Ожидается 600
print(calculate_area(15.5, 10))  # Ожидается 155.0
print(calculate_area("10", 5))  # Ошибка
print(calculate_area(10, "20"))  # Ошибка
print(calculate_area(0, 50))  # Ожидается 0
