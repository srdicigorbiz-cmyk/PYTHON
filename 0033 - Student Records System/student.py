class Student:
    def __init__(self, student_id, name, enrolled=True):
        # TODO: Initialize private attributes with double underscore prefix
        # TODO: Create __id as a private attribute and assign student_id to it
        # TODO: Create __grades as an empty dictionary to store course grades
        # TODO: Create __enrolled and assign the enrolled parameter to it
        # TODO: Use the name setter for validation by assigning name parameter to self.name
        self.__id = student_id
        self.__grades = {}
        self.__enrolled = enrolled
        self.name = name
    
    # ID property (read-only)
    @property
    def id(self):
        # TODO: Return the private __id attribute
        return self.__id
    
    # Name property with getter and setter
    @property
    def name(self):
        # TODO: Return the private __name attribute
        return self.__name
    
    @name.setter
    def name(self, value):
        # TODO: Validate that the name is at least 2 characters long
        # TODO: If validation fails, raise ValueError with message "Name must be at least 2 characters long"
        # TODO: If validation passes, assign value to the private __name attribute
        if len(value) < 2:
            raise ValueError("Name must be at least 2 characters long")
        else:
            self.__name = value
    
    # Enrolled property with getter and setter
    @property
    def enrolled(self):
        # TODO: Return the private __enrolled attribute
        return self.__enrolled
    
    @enrolled.setter
    def enrolled(self, value):
        # TODO: Validate that value is a boolean using isinstance(value, bool)
        # TODO: If validation fails, raise ValueError with message "Enrolled must be a boolean value"
        # TODO: If validation passes, assign value to the private __enrolled attribute
        if isinstance(value, bool):
            self.__enrolled = value
        else:
            raise ValueError("Enrolled must be a boolean value")
    
    # Grade average property (read-only)
    @property
    def grade_average(self):
        # TODO: Check if __grades is empty, return 0 if it is
        # TODO: Calculate and return the average of all grades in the __grades dictionary
        # TODO: Use sum(self.__grades.values()) / len(self.__grades) for the calculation
        if len(self.__grades) == 0:
            return 0
        else:
            average_grade = sum(self.__grades.values()) / len(self.__grades)
            return average_grade
    
    # Methods
    def add_grade(self, course, grade):
        # TODO: Add a grade for a course by adding a key-value pair to the __grades dictionary
        # TODO: Use course as the key and grade as the value
        self.__grades[course]=grade
    
    def display_record(self):
        # TODO: Create a string variable enrolled_status that is "Yes" if __enrolled is True, otherwise "No"
        # TODO: Print the student record in the required format:
        # TODO: Print "ID: {self.__id}"
        # TODO: Print "Name: {self.__name}"
        # TODO: Print "Enrolled: {enrolled_status}"
        # TODO: Print "Courses: {len(self.__grades)}"
        # TODO: Print "Grade Average: {self.grade_average:.2f}" (formatted to 2 decimal places)
        if self.__enrolled:
            enrolled_status = "Yes"
        else:
            enrolled_status = "No"
        print(f"ID: {self.__id}")
        print(f"Name: {self.__name}")
        print(f"Enrolled: {enrolled_status}")
        print(f"Courses: {len(self.__grades)}")
        print(f"Grade Average: {self.grade_average:.2f}")