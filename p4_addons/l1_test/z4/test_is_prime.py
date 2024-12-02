import pytest
from is_prime import is_prime

# Группа тестов для простых чисел
@pytest.mark.parametrize("n", [2, 3, 5, 7])
def test_prime_numbers(n):
    """Проверяет, что простые числа определяются правильно."""
    assert is_prime(n) == True

# Группа тестов для непростых чисел
@pytest.mark.parametrize("n", [1, 4, 6, 8, 9])
def test_non_prime_numbers(n):
    """Проверяет, что непростые числа определяются правильно."""
    assert is_prime(n) == False

# Группа тестов для нуля и отрицательных чисел
@pytest.mark.parametrize("n", [0, -1, -10])
def test_zero_and_negative_numbers(n):
    """Проверяет, что нуль и отрицательные числа не являются простыми."""
    assert is_prime(n) == False

