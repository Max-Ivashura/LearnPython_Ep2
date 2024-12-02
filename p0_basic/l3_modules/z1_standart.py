import math
import random
import datetime

# 1. Квадратный корень из 16
res_1 = math.sqrt(16)

# 2. Список из 10 случайных целых чисел от 1 до 100
res_2 = [random.randint(1, 100) for _ in range(10)]

# 3. Текущая дата и время
res_3 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# Печать результатов
print(f"Квадратный корень из 16: {res_1}")
print(f"Список случайных чисел: {res_2}")
print(f"Текущая дата и время: {res_3}")
