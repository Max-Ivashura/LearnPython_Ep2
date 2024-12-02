class NegativeNumberError(Exception):
    def __init__(self, message):
        super().__init__(message)

class Calculator:
    def add(self, a, b):
        if a < 0 or b < 0:
            raise NegativeNumberError("Ошибка! Оба числа должны быть положительными.")
        return a + b

# Пример использования
calc = Calculator()

try:
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
    result = calc.add(num1, num2)
    print("Результат сложения:", result)
except NegativeNumberError as e:
    print(e)
except ValueError:
    print("Вы ввели не число!")