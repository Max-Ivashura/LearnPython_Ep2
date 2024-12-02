class Calculator:
    """Класс для выполнения основных арифметических операций."""

    @staticmethod
    def add(a, b):
        """Возвращает результат сложения двух чисел."""
        return a + b

    @staticmethod
    def sub(a, b):
        """Возвращает результат вычитания двух чисел."""
        return a - b

    @staticmethod
    def multiply(a, b):
        """Возвращает результат произведения двух чисел."""
        return a * b

    @staticmethod
    def divide(a, b):
        """Возвращает результат деления a на b."""
        if b == 0:
            raise ValueError("Деление на ноль невозможно!")
        return a / b
