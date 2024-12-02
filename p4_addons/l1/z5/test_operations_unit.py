import unittest
from operations import divide


class TestMathOperations(unittest.TestCase):

    def test_divide_by_zero(self):
        """Проверяет, что деление на ноль вызывает исключение ZeroDivisionError."""
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)


if __name__ == '__main__':
    unittest.main()
