import random

arr = [random.randint(1, 100) for _ in range(10)]  # Генерация списка из 10 случайных чисел
arr.sort()
print(arr)
print(sum(arr))
