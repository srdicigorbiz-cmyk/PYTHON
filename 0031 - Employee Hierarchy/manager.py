# TODO: Import the Employee class from employee.py
# Use format: from employee import Employee
from employee import Employee

class Manager(Employee):
    def __init__(self, name, age, employee_id, salary, department):
        # TODO: Call the parent class constructor with name, age, employee_id, and salary
        # TODO: Store department as an instance attribute
        super().__init__(name, age, employee_id, salary)
        self.department = department
    
    def calculate_paycheck(self):
        # TODO: Override calculate_paycheck to include a 20% bonus
        # TODO: Return monthly salary with bonus: (salary * 1.2 / 12)
        return self.salary * 1.2 / 12
    
    def manage_team(self):
        # TODO: Return a string about managing the department
        # TODO: Format: "Managing the [department] department."
        return f"Managing the {self.department} department."