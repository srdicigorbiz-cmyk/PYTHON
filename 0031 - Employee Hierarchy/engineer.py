# TODO: Import the Employee class from employee.py
# Use format: from employee import Employee
from employee import Employee

class Engineer(Employee):
    def __init__(self, name, age, employee_id, salary, programming_language):
        # TODO: Call the parent class constructor with name, age, employee_id, and salary
        # TODO: Store programming_language as an instance attribute
        super().__init__(name, age, employee_id, salary)
        self.programming_language = programming_language
    
    def code(self):
        # TODO: Return a string about coding in the programming language
        # TODO: Format: "Coding in [programming_language]."
        return f"Coding in {self.programming_language}."