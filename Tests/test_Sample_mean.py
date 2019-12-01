import unittest

from Calculator.Calculator import Calculator
from CsvReader.Read_answer import read_answer
from CsvReader.Read_population import read_population


class MyTestCase(unittest.TestCase):
    calculator = Calculator()

    def test_sample_mean(self):
        my_population = read_population("population.csv")
        try:
            self.assertEqual(self.calculator.sample_mean(my_population),read_answer("answer_sample_mean.csv"))  # positive test
            self.assertNotEqual(self.calculator.sample_mean(my_population),(read_answer("answer_sample_mean.csv") + 1))  # negative test
        except AssertionError as e:
            print("Sample Mean has Assertion Error:", e)
            assert 0
if __name__ == '__main__':
    unittest.main()