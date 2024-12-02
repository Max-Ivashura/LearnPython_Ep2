import pytest
from person import Person


def test_greet():
    """Проверяет, что метод greet возвращает корректное сообщение."""
    person = Person("Иван", 30)
    assert person.greet() == "Здравствуйте, меня зовут Иван, мне 30 лет."

    person = Person("Алексей", 25)
    assert person.greet() == "Здравствуйте, меня зовут Алексей, мне 25 лет."


def test_negative_age():
    """Проверяет, что передача отрицательного возраста вызывает исключение ValueError."""
    with pytest.raises(ValueError):
        Person("Анастасия", -1)
