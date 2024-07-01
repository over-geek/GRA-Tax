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
