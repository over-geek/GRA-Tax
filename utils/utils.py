tax_rates = [
  {"Taxable Income": 490, "Tax Rate": 0},
  {"Taxable Income": 110, "Tax Rate": 0.05},
  {"Taxable Income": 130, "Tax Rate": 0.10},
  {"Taxable Income": 3166.67, "Tax Rate": 0.175},
  {"Taxable Income": 16000, "Tax Rate": 0.25},
  {"Taxable Income": 30520, "Tax Rate": 0.30},
  {"Taxable Income": float('inf'), "Tax Rate": 0.35}
]

pension_tiers = {
  "Tier 1": {"Employee Contribution": 0, "Employer Contribution": 0.13},
  "Tier 2": {"Employee Contribution": 0.055, "Employer Contribution": 0},
  "Tier 3": {"Employee Contribution": 0.05, "Employer Contribution": 0.05}
}

def calculate_paye_tax(chargeable_income):
  tax = 0
  remaining_income = chargeable_income

  for rate in tax_rates:
    if remaining_income > rate["Taxable Income"]:
      tax += rate["Taxable Income"] * rate["Tax Rate"]
      remaining_income -= rate["Taxable Income"]
    else:
      tax += remaining_income * rate["Tax Rate"]
      break
  return tax

def calculate_pensions(gross_salary):
  tier = "Tier 2"
  employee_contribution = gross_salary * pension_tiers[tier]["Employee Contribution"]
  employer_contribution = gross_salary * pension_tiers[tier]["Employer Contribution"]
  total_employee_contributions = employee_contribution + employer_contribution
  return total_employee_contributions, employer_contribution, employee_contribution

def calculate_taxable_income(gross_salary):
  total_employee_contributions, employer_contribution, employee_contribution = calculate_pensions(gross_salary)
  taxable_income = gross_salary - total_employee_contributions
  return taxable_income, total_employee_contributions, employer_contribution, employee_contribution

def calculate_gross_salary(net_salary, allowances):
  if not (isinstance(net_salary, (int, float)) and isinstance(allowances, (int, float))):
    raise TypeError("Net salary and allowances must be numeric")

  if net_salary < 0 or allowances < 0:
    raise ValueError("Net Salary and Allowances must be non-negative")
  
  # Initial guess for gross_salary
  gross_salary = net_salary + allowances

  # Adjusting the gross_salary until the calculated net salary is close to the actual net salary
  while True:
    taxable_income, total_employee_contributions, employer_contribution, employee_contribution = calculate_taxable_income(gross_salary)
    tax = calculate_paye_tax(taxable_income)
    calculate_net_salary = gross_salary - tax - total_employee_contributions

    if abs(calculate_net_salary - net_salary) < 0.01:
      break
    gross_salary += (net_salary - calculate_net_salary) / 2

  return gross_salary, employee_contribution, employer_contribution, tax