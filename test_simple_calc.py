# This file will have our tests
from simple_calc import SimpleCalc
import unittest
import pytest

# Write a class to write our tests
class CalcTest(unittest.TestCase):
    # Create an object
    calc = SimpleCalc()

### IMPORTANT - Must use the 'test' word in our methods
    def test_add(self):
        # We are asking python to test if 2 + 4 = 6
        self.assertEqual(self.calc.add(2, 4), 6)

    # Test if 4 - 2 =2
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(4, 2), 2)

    # Test if 2 x 2 = 4
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 2), 4)

    # Test if 6 / 3 = 2
    def test_divide(self):
        self.assertEqual(self.calc.divide(6, 3), 2)
        