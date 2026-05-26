# TODO: Import the Course class
# from course import Course
from course import Course

class Student:
    def __init__(self, name, email):
        # TODO: Initialize instance attributes:
        # - name: student's name
        # - email: student's email
        # - enrolled_courses: empty list to track courses the student is enrolled in
        # - completed_courses: empty list to track courses the student has completed
        self.name = name
        self.email = email
        self.enrolled_courses = []
        self.completed_courses = []
    
    def enroll(self, course):
        # TODO: Enroll the student in a course
        # - Return False if the student is already enrolled in the course (course in self.enrolled_courses)
        # - Use course.add_student(self) to attempt to add the student to the course
        # - If course.add_student returns True, add the course to self.enrolled_courses and return True
        # - Otherwise, return False
        if course in self.enrolled_courses:
            return False
        else:
            if course.add_student(self):
                self.enrolled_courses.append(course)
                return True
            else:
                return False
    
    def unenroll(self, course):
        # TODO: Unenroll the student from a course
        # - Return False if the student is not enrolled in the course (course not in self.enrolled_courses)
        # - Use course.remove_student(self) to attempt to remove the student from the course
        # - If course.remove_student returns True, remove the course from self.enrolled_courses and return True
        # - Otherwise, return False
        if course in self.enrolled_courses:
            if course.remove_student(self):
                self.enrolled_courses.remove(course)
                return True
            else:
                return False
        else:
            return False
    
    def complete_course(self, course):
        # TODO: Mark a course as completed for the student
        # - Return False if the student is not enrolled in the course (course not in self.enrolled_courses)
        # - Use course.mark_completed(self) to attempt to mark the course as completed
        # - If course.mark_completed returns True:
        #   - Remove the course from self.enrolled_courses
        #   - Add the course to self.completed_courses
        #   - Return True
        # - Otherwise, return False
        if course in self.enrolled_courses:
            if course.mark_completed(self):
                self.enrolled_courses.remove(course)
                self.completed_courses.append(course)
                return True
            else:
                return False
        else:
            return False