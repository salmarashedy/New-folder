import unittest

import lll


class TestLll(unittest.TestCase):
    def test_add(self):
        self.assertEqual(lll.add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(lll.subtract(5, 2), 3)

    def test_multiply(self):
        self.assertEqual(lll.multiply(4, 3), 12)

    def test_divide(self):
        self.assertEqual(lll.divide(10, 2), 5)

    def test_divide_by_zero(self):
        self.assertEqual(lll.divide(5, 0), "Error: Cannot divide by zero")


if __name__ == '__main__':
    unittest.main()
