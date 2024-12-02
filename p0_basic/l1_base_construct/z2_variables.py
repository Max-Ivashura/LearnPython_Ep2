'''
Задание 1: Создайте переменные различных типов и выведите их типы на экран.
- Создайте переменные для:
  - Целого числа (например, age)
  - Числа с плавающей запятой (например, height)
  - Строки (например, name)
  - Списка (например, fruits — список фруктов)
  - Кортежа (например, coordinates — кортеж с координатами)
  - Множества (например, unique_numbers — множество чисел)
  - Словаря (например, person — словарь с информацией о человеке)
'''

age = 23  # int
height = 180.5  # float
name = 'Max'  # string
fruits = ['banana', 'coconut', 'apple']  # list
coords = (185.5, 164.3, 194.78)  # tuple
unique_numbers = {1, 2, 3, 4, 5}  # set
person = {'age': 18, 0: 'error', (1, 2, 3): 'test'}  # dict

print(type(age))
print(type(height))
print(type(name))
print(type(fruits))
print(type(coords))
print(type(unique_numbers))
print(type(person))

