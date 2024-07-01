import unittest
from utils.utils import calculate_pensions

class TestPensionCalculation(unittest.TestCase):
  def test_pension_calculation(self):
    gross_salary = 10000
    expected_employee_contribution = 550 # 5.5% of gross salary
    expected_employer_contribution = 0 # 0% of gross salary
    _, employer_contribution, employee_contribution = calculate_pensions(gross_salary)
    self.assertAlmostEqual(employee_contribution, expected_employee_contribution, places=2)
    self.assertAlmostEqual(employer_contribution, expected_employer_contribution, places=2)

if __name__ == '__main__':
  unittest.main()