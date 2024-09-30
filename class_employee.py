class Employee:
    """This class represents the employees in the hotel"""

    # Employee's Attributes
    def __init__(self, employee_id, employee_name, employee_email, e_Phone_number, shift):
        self.__employee_id = employee_id  # Unique ID for the employee
        self.__employee_name = employee_name  # Employee's name
        self.__employee_email = employee_email  # Employee's email
        self.__e_Phone_number = e_Phone_number  # Employee's phone number
        self.__shift = shift  # Employee's assigned shift

    # Sets Employee ID
    def set_employee_id(self, employee_id):
        self.__employee_id = employee_id

    # Returns employee's ID
    def get_employee_id(self):
        return self.__employee_id

    # Sets Employee Name
    def set_employee_name(self, employee_name):
        self.__employee_name = employee_name

    # Returns Employee Name
    def get_employee_name(self):
        return self.__employee_name

    # Sets Employee Email
    def set_employee_email(self, employee_email):
        self.__employee_email = employee_email

    # Returns Employee Email
    def get_employee_email(self):
        return self.__employee_email

    # Sets Employee Phone Number
    def set_e_Phone_number(self, e_Phone_number):
        self.__e_Phone_number = e_Phone_number

    # Returns Employee Phone Number
    def get_e_Phone_number(self):
        return self.__e_Phone_number

    # Sets the employee's Shift
    def set_shift(self, shift):
        self.__shift = shift

    # Returns the employee's Shift
    def get_shift(self):
        return self.__shift


