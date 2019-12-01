import unittest

from Calculator.Calculator import Calculator
from CsvReader.Read_answer import read_answer
from CsvReader.Read_population import read_population


class MyTestCase(unittest.TestCase):
    calculator = Calculator()

    def test_variance_sample_proportion(self):
        my_population = read_population("population.csv")
        # expected_output = read_answer("answer_variance_sample_proportion.csv")
        try:
            self.assertEqual(self.calculator.variance_sample_proportion(my_population),read_answer("answer_variance_sample_proportion.csv"))  # positive test
            self.assertNotEqual(self.calculator.variance_sample_proportion(my_population),(read_answer("answer_variance_sample_proportion.csv") + 1))  # negative test
        except AssertionError as e:
            print("Variance of Sample Proportion has Assertion Error:", e)
            assert 0

if __name__ == '__main__':
    unittest.main()