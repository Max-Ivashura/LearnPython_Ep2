class Person:
    def __init__(self, name, age):
        """Инициализация класса Person с атрибутами name и age."""
        if age < 0:
            raise ValueError("Возраст не может быть отрицательным.")
        self.name = name
        self.age = age

    def greet(self):
        """Возвращает строку с приветствием."""
        return f"Здравствуйте, меня зовут {self.name}, мне {self.age} лет."
