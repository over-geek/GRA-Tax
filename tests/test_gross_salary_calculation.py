import unittest
from utils.utils import calculate_gross_salary

class TestGrossSalaryCalculation(unittest.TestCase):
  def test_gross_salary(self):
    net_salary = 5000
    allowances = 2000
    expected_gross_salary = 6488.2
    gross_salary, _, _, _ = calculate_gross_salary(net_salary, allowances)
    self.assertAlmostEqual(round(gross_salary, 2), expected_gross_salary, places=2)

  def test_invalid_inputs(self):
    # testing for negaitve net salary
    with self.assertRaises(ValueError):
      calculate_gross_salary(-1000, 1000)

    # testing for non-numeric net salary
    with self.assertRaises(TypeError):
      calculate_gross_salary('dgs', 1000)

    # test for both non-numeric inputs
    with self.assertRaises(TypeError):
      calculate_gross_salary('dgs', 'dgs')

if __name__ == '__main__':
  unittest.main()