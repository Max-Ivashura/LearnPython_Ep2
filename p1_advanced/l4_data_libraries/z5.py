import pandas as pd

# Датафрейм с информацией о продаже
data1 = {
    'Товар': ['Товар1', 'Товар2', 'Товар3', 'Товар4', 'Товар5', 'Товар6'],
    'Стоимость': [1500, 999, 1989, 400, 2430, 1555]
}

# Датафрейм с информацией о возврате
data2 = {
    'Товар': ['Товар1', 'Товар3', 'Товар5'],
    'Стоимость': [1500, 1989, 2430]
}

# Создание датафреймов
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

# Объединим два датафрейма, добавив индикатор, чтобы увидеть, откуда пришли данные
merged_df = df1.merge(df2, on='Товар', how='outer', indicator=True)
# print(merged_df)

# Выведем только те товары, которые были проданы, но не возвращены
sold_not_returned = merged_df[merged_df['_merge'] == 'left_only']

# Удалим лишние столбцы, если они не нужны
sold_not_returned = sold_not_returned[['Товар', 'Стоимость_x']]
sold_not_returned.columns = ['Товар', 'Стоимость']  # Переименуем столбцы для удобства

# Вывод результатов
print("Товары, которые были проданы, но не возвращены:")
print(sold_not_returned)
