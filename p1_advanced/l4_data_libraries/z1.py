import numpy as np

# Создание массива из 10 случайных целых чисел от 1 до 100
arr = np.random.randint(1, 101, size=10)

print("Массив:", arr)
print("Среднее:", np.mean(arr))
print("Макс:", np.max(arr))
print("Мин:", np.min(arr))
