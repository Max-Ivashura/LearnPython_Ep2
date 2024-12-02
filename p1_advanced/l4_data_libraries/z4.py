import pandas as pd
import matplotlib.pyplot as plt

# Загружаем данные из CSV файла с кодировкой cp1251
df = pd.read_csv('files/expenses.csv', encoding='cp1251')

# Убедимся, что столбцы 'Категория' и 'Сумма' существуют
if 'Категория' in df.columns and 'Сумма' in df.columns:
    # Группируем по категории и суммируем расходы
    category_expenses = df.groupby('Категория')['Сумма'].sum()

    # Строим круговую диаграмму
    plt.figure(figsize=(8,8))
    plt.pie(category_expenses, labels=category_expenses.index, autopct='%1.1f%%', startangle=140)
    plt.title('Распределение расходов по категориям')
    plt.axis('equal')  # Чтобы круговая диаграмма была круговой
    plt.show()
else:
    print("Файл должен содержать столбцы 'Категория' и 'Сумма'.")
