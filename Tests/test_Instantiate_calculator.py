import unittest

from Calculator.Calculator import Calculator


class MyTestCase(unittest.TestCase):
    calculator = Calculator()

    def test_instantiate_calculator(self):
        try:
            self.assertIsInstance(self.calculator, Calculator)
        except AssertionError as e:
            print("Calculator Instantiation has Assertion Error:", e)
            assert 0

if __name__ == '__main__':
    unittest.main()