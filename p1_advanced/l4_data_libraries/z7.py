import numpy as np
from matplotlib import pyplot as plt

# Генерация массива случайных чисел
data = np.random.randint(0, 10000, 100)

# Создание гистограммы
plt.hist(data, bins=20, density=True, alpha=0.5, color='blue', edgecolor='black')

# Добавление заголовка и подписей осей
plt.title('Гистограмма случайных значений с линией тренда')
plt.xlabel('Значения')
plt.ylabel('Плотность вероятности')

# Отображение графика
plt.grid(True)  # добавляем сетку для удобства восприятия
plt.show()
