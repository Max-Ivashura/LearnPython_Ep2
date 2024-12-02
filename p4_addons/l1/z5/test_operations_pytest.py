import pytest
from operations import divide

def test_divide_by_zero():
    """Проверяет, что деление на ноль вызывает исключение ZeroDivisionError."""
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)
