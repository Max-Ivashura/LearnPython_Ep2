import pandas as pd

# Загрузка данных из CSV файла
df = pd.read_csv('files/sales.csv', encoding='cp1251')

# Подсчет общей выручки для каждого товара
df['Итого'] = df['Количество'] * df['Цена']

# Создание нового DataFrame с результатами
result_df = df[['Товар', 'Количество', 'Цена', 'Итого']]

# Вывод результата
print(result_df)
