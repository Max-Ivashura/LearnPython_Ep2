import math

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented

    def length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

# Пример использования
v1 = Vector(2, 3)
v2 = Vector(4, 5)

v3 = v1 + v2  # Использование перегрузки оператора +
print(v3)     # Вывод: Vector(6, 8)
print(f"Длина вектора v3: {v3.length()}")  # Вывод длины вектора v3
