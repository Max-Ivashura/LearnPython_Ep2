import pandas as pd

# Загружаем данные из CSV файла с кодировкой cp1251
df = pd.read_csv('files/sales_data.csv', encoding='cp1251')

# Убедимся, что столбец 'Дата' является типом данных datetime
df['Дата'] = pd.to_datetime(df['Дата'], errors='coerce')  # 'errors=coerce' чтобы игнорировать ошибки

# Сбрасываем строки с неверными датами (если они есть)
df = df.dropna(subset=['Дата'])

# Группируем по месяцу и суммируем продажи
monthly_sales = df.resample('ME', on='Дата')['Сумма'].sum()

# Выводим общую сумму продаж за каждый месяц
print("Общая сумма продаж за каждый месяц:\n", monthly_sales)
