while True:
    try:
        v1 = int(input("Введите число: "))
        break  # Если ввод корректен, выходим из цикла
    except ValueError:
        print('Вы ввели не число! Пожалуйста, попробуйте еще раз.')
