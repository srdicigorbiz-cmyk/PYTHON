# TODO: Import the Student class
# from student import Student

from student import Student

class StudentRegistry:
    def __init__(self):
        # TODO: Initialize a private __students attribute as an empty dictionary
        # This will store student objects with their IDs as keys
        self.__students = {}
        
    
    def add_student(self, student):
        # TODO: Add a student to the registry by using student.id as the key
        # TODO: Store the student object as the value in the __students dictionary
        self.__students[student.id]=student
    
    def remove_student(self, student_id):
        # TODO: Check if student_id exists in the __students dictionary
        # TODO: If it exists, remove the student from the dictionary using del
        if student_id in self.__students:
            del self.__students[student_id]

    
    def get_student(self, student_id):
        # TODO: Return the student with the given student_id from the __students dictionary
        # TODO: Use the .get() method to safely retrieve the student (returns None if not found)
        return self.__students.get(student_id)
    
    def get_top_student(self):
        # TODO: Check if the __students dictionary is empty, return None if it is
        # TODO: Use max() with a key function to find the student with the highest grade_average
        # TODO: The key function should be a lambda that returns student.grade_average
        if len(self.__students) == 0:
            return None
        else:
            return max(self.__students.values(), key=lambda student: student.grade_average)

    
    def display_all(self):
        # TODO: Loop through all student_id, student pairs in the __students dictionary
        # TODO: For each student, print a formatted string with ID, name, and grade average
        # TODO: Format: "ID: {student_id}, Name: {student.name}, Average: {student.grade_average:.2f}"
        for student_id, student in self.__students.items():
            print(f"ID: {student_id}, Name: {student.name}, Average: {student.grade_average:.2f}")