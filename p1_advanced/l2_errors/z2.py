while True:
    try:
        v1 = float(input("Введите делимое: "))
        v2 = float(input("Введите делитель: "))
        result = v1 / v2
        print("Результат деления:", result)
        break  # Выходим из цикла, если всё прошло успешно
    except ZeroDivisionError:
        print("На ноль делить нельзя! Пожалуйста, введите делитель снова.")
    except ValueError:
        print("Вы ввели не число! Пожалуйста, введите числовые значения.")
