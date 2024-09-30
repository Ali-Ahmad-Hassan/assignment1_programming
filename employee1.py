# Create an Employee object with the name Will Smith
employee = Employee(employee_id=1001, employee_name="Will Smith", employee_email="willsmith@hotel.com", e_Phone_number="555-987-6543", shift="Morning")

# View employee information
print(f"Employee ID: {employee.get_employee_id()}")
print(f"Employee Name: {employee.get_employee_name()}")
print(f"Employee Email: {employee.get_employee_email()}")
print(f"Employee Phone Number: {employee.get_e_Phone_number()}")
print(f"Employee Shift: {employee.get_shift()}")
