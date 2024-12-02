# Создание кортежа
arr = ('C++', 'C#', 'Python', 'Java', 'Javascript')

# Вывод второго элемента
print(arr[1])  # Вывод: C#

# Проверка на наличие "Python"
if 'Python' in arr:
    print("Строка 'Python' содержится в кортеже.")
else:
    print("Строка 'Python' не содержится в кортеже.")

# Вывод индекса "Python"
print(arr.index('Python'))  # Вывод: 2
