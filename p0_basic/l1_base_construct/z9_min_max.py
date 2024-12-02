"""
Задание 9: Напишите функцию get_min_max, которая принимает список чисел и возвращает
 минимальное и максимальное значения этого списка. Вызовите функцию с примером списка.
"""


def get_min_max(values):
    if not values:  # Проверяем, является ли список пустым
        print("Ошибка: список не должен быть пустым.")
        return None

    if not all(isinstance(x, (int, float)) for x in values):  # Проверяем, что все элементы - числа
        print("Ошибка: все элементы списка должны быть числами.")
        return None

    minv = min(values)
    maxv = max(values)
    return (minv, maxv)  # Возвращаем кортеж вместо списка


# Тестовый список
test = [1, 2, 3, -5, 200, 4, 6]
result = get_min_max(test)
if result is not None:
    print(f"Минимальное значение: {result[0]}, Максимальное значение: {result[1]}")
