from student import Student
from studentregistry import StudentRegistry
import time
import random

student1 = Student(1001, "Alice Smith")
student2 = Student(1002, "Bob Johnson")
student3 = Student(1003, "Charlie Brown")

# Add grades
student1.add_grade("Math", 90)
student1.add_grade("Science", 85)
student1.add_grade("English", 92)

student2.add_grade("Math", 78)
student2.add_grade("Science", 80)
student2.add_grade("English", 85)

student3.add_grade("Math", 95)
student3.add_grade("Science", 91)
student3.add_grade("English", 89)

print(student1.display_record())

