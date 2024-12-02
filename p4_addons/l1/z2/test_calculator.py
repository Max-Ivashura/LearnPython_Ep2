import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def test_add(self):
        test_cases = [
            (5, 10, 15),
            (15.5, 12.5, 28),
            (-3, -10, -13),
            (-12.5, -5.5, -18),
            (-5, 10, 5),
            (15.5, -12.5, 3),
            (0, 5, 5),
            (5, 0, 5),
            (0, 0, 0)
        ]
        for a, b, expected in test_cases:
            self.assertEqual(Calculator.add(a, b), expected)

    def test_sub(self):
        test_cases = [
            (5, 10, -5),
            (15.5, 12.5, 3),
            (-3, -10, 7),
            (-12.5, -5.5, -7),
            (-5, 10, -15),
            (15.5, -12.5, 28),
            (5, 0, 5),
            (0, 12.5, -12.5)
        ]
        for a, b, expected in test_cases:
            self.assertEqual(Calculator.sub(a, b), expected)

    def test_multiply(self):
        test_cases = [
            (2, 3, 6),
            (10, 5, 50),
            (-2, -3, 6),
            (-5, -10, 50),
            (-2, 3, -6),
            (5, -4, -20),
            (0, 5, 0),
            (5, 0, 0),
            (0, 0, 0)
        ]
        for a, b, expected in test_cases:
            self.assertEqual(Calculator.multiply(a, b), expected)

    def test_divide(self):
        test_cases = [
            (10, 2, 5.0),
            (15, 3, 5.0),
            (-10, -2, 5.0),
            (-15, -3, 5.0),
            (-10, 2, -5.0),
            (15, -3, -5.0)
        ]
        for a, b, expected in test_cases:
            self.assertEqual(Calculator.divide(a, b), expected)

        with self.assertRaises(ValueError):
            Calculator.divide(10, 0)

if __name__ == '__main__':
    unittest.main()
