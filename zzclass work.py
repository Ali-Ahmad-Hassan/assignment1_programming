class Person:
    def __init__(self, first_name, last_name, date_of_birth, gender, emirates_id):
        """This class represents an Emirati person"""
        self._first_name = first_name
        self._last_name = last_name
        self._date_of_birth = date_of_birth
        self._gender = gender
        self._emirates_id = emirates_id

    def __str__(self):
        return (f"Name: {self._first_name} {self._last_name}\n"
                f"Date of Birth: {self._date_of_birth}\n"
                f"Gender: {self._gender}\n"
                f"Emirates ID: {self._emirates_id}")


from enum import Enum


# Enum for Employee type
class EmpType(Enum):
    STAFF = "Staff"
    FACULTY = "Faculty"
    ADJUNCT_FACULTY = "Adjunct Faculty"
    CONTRACT_STAFF = "Contract Staff"


class Student(Person):
    def __init__(self, first_name, last_name, date_of_birth, gender, emirates_id, student_id, email_id, gpa, major,
                 concentration):
        # Initialize the parent class (Person)
        super().__init__(first_name, last_name, date_of_birth, gender, emirates_id)

        # Initialize the additional properties for Student
        self.student_id = student_id
        self.email_id = email_id
        self.gpa = gpa
        self.major = major
        self.concentration = concentration

    def __str__(self):
        # Call the __str__ method from the Person class and add Student-specific information
        return (super().__str__() +
                f"\nStudent ID: {self.student_id}\n"
                f"Email ID: {self.email_id}\n"
                f"GPA: {self.gpa}\n"
                f"Major: {self.major}\n"
                f"Concentration: {self.concentration}")


# Example of creating a Student object
student = Student("Ahmed", "Al Mansoori", "1992-05-10", "Male", "784-1234-5678900-1",
                  "S123456", "ahmed.mansoori@example.com", 3.8, "Computer Science", "Artificial Intelligence")

# Print the details of the student
print(student)

# Enum for Employee type
class EmpType(Enum):
    STAFF = "Staff"
    FACULTY = "Faculty"
    ADJUNCT_FACULTY = "Adjunct Faculty"
    CONTRACT_STAFF = "Contract Staff"


class Employee(Person):
    def __init__(self, first_name, last_name, date_of_birth, gender, emirates_id, emp_id, emp_type, emp_date_of_joining,
                 emp_salary):
        # Initialize the parent class (Person)
        super().__init__(first_name, last_name, date_of_birth, gender, emirates_id)

        # Initialize the additional properties for Employee
        self.emp_id = emp_id
        self.emp_type = emp_type  # This should be of type EmpType
        self.emp_date_of_joining = emp_date_of_joining  # string or date format 'YYYY-MM-DD'
        self.emp_salary = emp_salary  # float or integer depending on the context

    def __str__(self):
        # Call the __str__ method from the Person class and add Employee-specific information
        return (super().__str__() +
                f"\nEmployee ID: {self.emp_id}\n"
                f"Employee Type: {self.emp_type.value}\n"
                f"Date of Joining: {self.emp_date_of_joining}\n"
                f"Salary: {self.emp_salary}")

        def calculate_age(self):
            # Calculate the employee's age based on the date_of_birth
            birth_date = datetime.strptime(self._date_of_birth, '%Y-%m-%d')
            today = datetime.today()
            age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
            return age

        def add_bonus(self):
            # Add 5% to the salary if all conditions are met
            if (self._gender == "Female" and
                    self.emp_type == EmpType.FACULTY and
                    25 <= self.calculate_age() <= 45):
                self.emp_salary += self.emp_salary * 0.05
                print("Bonus added!")
            else:
                print("Bonus not applicable.")

        def __str__(self):
            # Call the __str__ method from the Person class and add Employee-specific information
            return (super().__str__() +
                    f"\nEmployee ID: {self.emp_id}\n"
                    f"Employee Type: {self.emp_type.value}\n"
                    f"Date of Joining: {self.emp_date_of_joining}\n"
                    f"Salary: {self.emp_salary}")

    # Example of creating an Employee object
    employee = Employee("Fatima", "Al Rashid", "1985-07-20", "Female", "784-5678-9012345-1",
                        "E12345", EmpType.FACULTY, "2020-09-01", 150000)

    # Print the details of the employee before applying bonus
    print(employee)

    # Apply bonus
    employee.add_bonus()

    # Print the details of the employee after applying bonus
    print(employee)


# Example of creating an Employee object
employee = Employee("Sarah", "Mohammed", "1985-07-20", "Female", "784-5678-9012345-1",
                    "E12345", EmpType.FACULTY, "2020-09-01", 150000)

# Print the details of the employee
print(employee)

from enum import Enum
from datetime import datetime


# Enum for Employee type
class EmpType(Enum):
    STAFF = "Staff"
    FACULTY = "Faculty"
    ADJUNCT_FACULTY = "Adjunct Faculty"
    CONTRACT_STAFF = "Contract Staff"




