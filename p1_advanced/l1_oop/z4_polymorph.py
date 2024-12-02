import math


class Shape():
    def area(self):
        pass


class Rectangle(Shape):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


def calc(*shapes):
    for shape in shapes:
        print(f"Площадь: {shape.area()}")


f1 = Rectangle(5, 10)
f2 = Rectangle(2, 5)

f3 = Circle(5)
f4 = Circle(2)

calc(f1, f2, f3, f4)
