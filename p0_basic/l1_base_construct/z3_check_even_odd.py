"""
Напишите программу, которая запрашивает у пользователя число и выводит, четное оно или нечетное.
- Используйте конструкцию if, else для проверки.
"""
try:
    num = int(input("Введите число: "))

    if (num % 2 == 0):
        print("Чётное")
    else:
        print("Нечётное")
except ValueError:
    print("Пожалуйста, введите корректное целое число.")
