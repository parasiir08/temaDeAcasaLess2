import json

def load_employee_data(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def get_all_employees(employee_data):
    employees = [employee['name'] for employee in employee_data]
    return employees

def get_unique_positions(employee_data):
    positions = set(employee['position'] for employee in employee_data)
    return positions

def calculate_total_salary(employee_data):
    total_salary = sum(float(employee['salary']) for employee in employee_data)
    return total_salary

def calculate_total_tax(employee_data, tax_rate):
    total_tax = sum(float(employee['salary']) * tax_rate for employee in employee_data)
    return total_tax

def get_top_paid_employees(employee_data, num_employees):
    sorted_employees = sorted(employee_data, key=lambda employee: float(employee['salary']), reverse=True)
    top_paid_employees = sorted_employees[:num_employees]
    return top_paid_employees

def get_longest_serving_employees(employee_data, num_employees):
    sorted_employees = sorted(employee_data, key=lambda employee: employee['employment_start_date'])
    longest_serving_employees = sorted_employees[-num_employees:]
    return longest_serving_employees

# Exemplu de utilizare
file_path = input("Introduceți calea către fișierul JSON: ")
employee_data = load_employee_data(file_path)

# Lista de toți lucrătorii
all_employees = get_all_employees(employee_data)
print("Lista de toți lucrătorii:")
for employee in all_employees:
    print(employee)

# Lista de toate pozițiile unice din companie
unique_positions = get_unique_positions(employee_data)
print("\nLista de toate pozițiile unice din companie:")
for position in unique_positions:
    print(position)

# Suma totală pe care compania o are de achitat lucrătorilor
total_salary = calculate_total_salary(employee_data)
print("\nSuma totală pe care compania o are de achitat lucrătorilor:", total_salary)

# Calcularea sumei totale de impozite pe care compania o are de achitat într-o lună
tax_rate = float(input("\nIntroduceți valoarea impozitului (%): ")) / 100
total_tax = calculate_total_tax(employee_data, tax_rate)
print("Suma totală de impozite pe care compania o are de achitat într-o lună:", total_tax)

# Informații despre cei mai bine plătiți 10 lucrători
num_top_paid_employees = 10
top_paid_employees = get_top_paid_employees(employee_data, num_top_paid_employees)
print("\nInformații despre cei mai bine plătiți 10 lucrători:")
for employee in top_paid_employees:
    print(f"Name: {employee['name']}, Position: {employee['position']}, Salary: {employee['salary']}, Employment Start Date: {employee['employment_start_date']}")

# Informații despre cei cu cel mai mult timp în companie
num_longest_serving_employees = 10
longest_serving_employees = get_longest_serving_employees(employee_data, num_longest_serving_employees)
print("\nInformații despre cei cu cel mai mult timp în companie:")
for employee in longest_serving_employees:
    print(f"Name: {employee['name']}, Position: {employee['position']}, Salary: {employee['salary']}, Employment Start Date: {employee['employment_start_date']}")
