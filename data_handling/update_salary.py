# Given a dictionary of employees update their salaries

def update_salary(employee_salaries: dict, name: str, adjustment: float) -> dict:
    employee_salaries[name] += employee_salaries[name] * adjustment
    return employee_salaries


employee_salaries = {"Alice": 50000, "Bob": 60000}
name = "Alice"
adjustment = 0.10

print(update_salary(employee_salaries, name, adjustment))