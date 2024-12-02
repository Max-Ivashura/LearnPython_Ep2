class Animal():
    def __init__(self, name):
        self.name = name

    def speak(self):
        print('Sound!')

    def info(self):
        print('Info about Animal')


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        print(f'{self.name} произносит: Гав!')

    def info(self):
        print(f'Это собака! Её кличка: {self.name}')


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        print(f'{self.name} произносит: Мяу!')

    def info(self):
        print(f'Это кот! Его кличка: {self.name}')


# Создание объектов
dog = Dog('Шарик')
cat = Cat('Рыжик')

# Вызов методов
dog.speak()
dog.info()
cat.speak()
cat.info()
