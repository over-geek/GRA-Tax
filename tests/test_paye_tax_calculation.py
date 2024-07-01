import unittest
from utils.utils import calculate_paye_tax

class TestPayeTaxCalculation(unittest.TestCase):
  def test_paye_tax(self):

    # test with correct inputs
    chargeable_income = 10000
    expected_paye_tax = 2098.5
    paye_tax = calculate_paye_tax(chargeable_income)
    self.assertAlmostEqual(paye_tax, expected_paye_tax, places=2)

    # test with a chargeable income of 0
    chargeable_income = 0
    expected_paye_tax = 0
    paye_tax = calculate_paye_tax(chargeable_income)
    self.assertAlmostEqual(paye_tax, expected_paye_tax)


if __name__ == '__main__':
  unittest.main()