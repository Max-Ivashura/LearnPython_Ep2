class InvalidAgeError(Exception):
    def __init__(self, message):
        super().__init__(message)

def validate_age(age):
    if age < 0 or age > 120:
        raise InvalidAgeError('Возраст должен быть больше 0 и меньше или равен 120')
    print('Ваш возраст:', age)

# Запрашиваем у пользователя ввод возраста
try:
    user_age = int(input("Пожалуйста, введите ваш возраст: "))
    validate_age(user_age)
except InvalidAgeError as e:
    print("Ошибка:", e)
except ValueError:
    print("Ошибка: Ввод должен быть числом.")
