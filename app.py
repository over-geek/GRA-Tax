from flask import Flask, request, jsonify
from utils.utils import calculate_gross_salary

app = Flask(__name__)

@app.route('/calculate_gross', methods=['POST'])
def find_salary_details():
  data = request.get_json()
  net_salary = data["net_salary"]
  allowances = data["allowances"]

  gross_salary, employee_contribution, employer_contribution, tax = calculate_gross_salary(net_salary, allowances)
  basic_salary = gross_salary - allowances

  response = {
    "gross_salary": round(gross_salary, 2),
    "basic_salary": round(basic_salary, 2),
    "employee_contribution": round(employee_contribution, 2),
    "employer_contribution": round(employer_contribution, 2),
    "total_paye_tax": round(tax, 2),
}

  return jsonify(response)

if __name__ == '__main__':
  app.run(debug=True)
