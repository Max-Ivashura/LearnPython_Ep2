import pandas as pd
import numpy as np

# Загрузка данных из CSV файла
df = pd.read_csv('files/test_scores.csv', encoding='cp1251')

# Вычисление статистических характеристик
med = df['Оценка'].median()  # Медиана
st = df['Оценка'].std()  # Стандартное отклонение
avg = np.mean(df['Оценка'])  # Среднее значение
rng = np.ptp(df['Оценка'])  # Диапазон

# Вывод результатов
print("Медиана: ", med)
print("Стандартное отклонение: ", st)
print("Среднее значение: ", avg)
print("Диапазон: ", rng)
