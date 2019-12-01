import unittest

from Calculator.Calculator import Calculator
from CsvReader.Read_answer import read_answer
from CsvReader.Read_population import read_population


class MyTestCase(unittest.TestCase):
    calculator = Calculator()
    def test_mean(self):
        my_population=read_population("population.csv")
        expected_output=read_answer("answer_mean.csv")
        try:
            self.assertEqual(self.calculator.mean(my_population),expected_output) #positive test
            self.assertNotEqual(self.calculator.mean(my_population),(expected_output+1)) #negative test
        except AssertionError as e:
            print("Mean has Assertion Error:", e)
            assert 0

if __name__ == '__main__':
    unittest.main()