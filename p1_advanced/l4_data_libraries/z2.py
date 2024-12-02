import pandas as pd

data = {'Имя': ['Максим', 'Никита', 'Денис'],
        'Возраст': [23, 22, 21],
        'Специальность': ['ПКС', 'ВКС', 'ИВТ'],
        'Оценка': [80, 81, 74],
        }

df = pd.DataFrame(data)
print(df, '\n')
filtered_df = df[df['Оценка'] > 75]
print(filtered_df)
