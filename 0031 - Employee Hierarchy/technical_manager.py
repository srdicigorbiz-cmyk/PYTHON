# TODO: Import the Manager class from manager.py
# TODO: Import the Engineer class from engineer.py
# TODO: Import the Person class from person.py
from manager import Manager
from engineer import Engineer
from person import Person

class TechnicalManager(Manager, Engineer):
    def __init__(self, name, age, employee_id, salary, department, programming_language):
        # TODO: Initialize the TechnicalManager with multiple inheritance
        # TODO: Initialize the Person part directly using Person.__init__()
        # TODO: Set all other attributes directly (employee_id, salary, department, programming_language)
        
        Person.__init__(self, name, age)
        self.employee_id = employee_id
        self.salary = salary
        self.department = department
        self.programming_language = programming_language

