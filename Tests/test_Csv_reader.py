import unittest

from Calculator.Calculator import Calculator
from CsvReader.Read_answer_list import read_answer_list
from CsvReader.Read_population import read_population


class MyTestCase(unittest.TestCase):
    calculator = Calculator()

    def test_csv_reader(self):
        my_population = read_population("population.csv")
        expected_output = read_answer_list("answer_csv_reader.csv")
        try:
            self.assertListEqual(my_population, expected_output)  # positive test
            self.assertNotEqual(my_population,(list(map(lambda x: x + 1, expected_output))))  # negative test
        except AssertionError as e:
            print("Csv Reader has Assertion Error:", e)
            assert 0

if __name__ == '__main__':
    unittest.main()