import matplotlib.pyplot as plt
import pandas as pd

# Загрузите данные
df = pd.read_csv('files/temperature_data.csv')
df['Date'] = pd.to_datetime(df['Date'])

# Построение графика
plt.plot(df['Date'], df['Temperature'], label='Температура')  # Линия графика
plt.scatter(df['Date'], df['Temperature'], color='red')  # Точки

# Добавление даты к каждой точке
for i in range(len(df)):
    plt.annotate(df['Date'][i].strftime('%Y-%m-%d'),
                 (df['Date'][i], df['Temperature'][i]),
                 textcoords="offset points",  # Смещение текста
                 xytext=(0,10),  # Смещение по X и Y
                 ha='center',
                 fontsize=8)

# Добавление заголовка и подписей осей
plt.title('Изменение температуры')
plt.xlabel('День')
plt.ylabel('Температура')
plt.xticks(rotation=45)  # Поворот меток дат для лучшего отображения
plt.grid()  # Добавление сетки
plt.legend()  # Добавление легенды

# Отображение графика
plt.tight_layout()  # Оптимизация отображения
plt.show()
