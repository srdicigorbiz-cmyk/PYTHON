from course import Course
from student import Student
from instructor import Instructor

# Test case handler
test_case = input()

if test_case == "course_creation":
    # Test creating courses with different capacities
    course1 = Course("Python 101", "Introduction to Python", 20)
    course2 = Course("Data Science", "Advanced data analysis techniques")
    
    print(f"Course 1: {course1.title}, Max Capacity: {course1.max_capacity}")
    print(f"Course 2: {course2.title}, Max Capacity: {course2.max_capacity}")
    print(f"Initial student count: {len(course1.students)}")

elif test_case == "student_enrollment":
    # Test student enrollment process
    course = Course("Python 101", "Introduction to Python", 2)
    student1 = Student("Alice", "alice@example.com")
    student2 = Student("Bob", "bob@example.com")
    student3 = Student("Charlie", "charlie@example.com")
    
    # Enroll students
    result1 = student1.enroll(course)
    result2 = student2.enroll(course)
    result3 = student3.enroll(course)  # Should fail (capacity)
    
    print(f"Enrollment 1 result: {result1}")
    print(f"Enrollment 2 result: {result2}")
    print(f"Enrollment 3 result: {result3}")
    
    # Try enrolling the same student twice
    result4 = student1.enroll(course)
    print(f"Re-enrollment result: {result4}")
    
    # Check course and student states
    print(f"Course has {len(course.students)} students")
    print(f"Student 1 has {len(student1.enrolled_courses)} enrolled courses")

elif test_case == "student_unenrollment":
    # Test student unenrollment process
    course = Course("Python 101", "Introduction to Python")
    student = Student("Alice", "alice@example.com")
    
    # Enroll and then unenroll
    student.enroll(course)
    print(f"Before unenroll: Course has {len(course.students)} students")
    print(f"Before unenroll: Student has {len(student.enrolled_courses)} courses")
    
    result = student.unenroll(course)
    print(f"Unenrollment result: {result}")
    
    print(f"After unenroll: Course has {len(course.students)} students")
    print(f"After unenroll: Student has {len(student.enrolled_courses)} courses")
    
    # Try unenrolling again
    result = student.unenroll(course)
    print(f"Second unenrollment result: {result}")

elif test_case == "course_completion":
    # Test course completion process
    course = Course("Python 101", "Introduction to Python")
    student = Student("Alice", "alice@example.com")
    
    # Enroll and complete
    student.enroll(course)
    print(f"Before completion: Enrolled in {len(student.enrolled_courses)} courses")
    print(f"Before completion: Completed {len(student.completed_courses)} courses")
    
    result = student.complete_course(course)
    print(f"Completion result: {result}")
    
    print(f"After completion: Enrolled in {len(student.enrolled_courses)} courses")
    print(f"After completion: Completed {len(student.completed_courses)} courses")
    
    # Check course state
    print(f"Course has {len(course.students)} active students")
    print(f"Course has {len(course.completed_students)} completed students")

elif test_case == "instructor_assignment":
    # Test instructor assignment
    course = Course("Python 101", "Introduction to Python")
    instructor = Instructor("Dr. Smith", "smith@example.edu", "Computer Science")
    
    print(f"Before assignment: Instructor has {len(instructor.courses)} courses")
    print(f"Before assignment: Course instructor is {course.instructor}")
    
    result = instructor.assign_to_course(course)
    print(f"Assignment result: {result}")
    
    print(f"After assignment: Instructor has {len(instructor.courses)} courses")
    print(f"After assignment: Course instructor is {course.instructor.name}")

elif test_case == "course_management":
    # Test course capacity management
    course = Course("Limited Course", "Test capacity", 2)
    student1 = Student("Alice", "alice@example.com")
    student2 = Student("Bob", "bob@example.com")
    student3 = Student("Charlie", "charlie@example.com")
    
    # Fill the course
    student1.enroll(course)
    student2.enroll(course)
    result = student3.enroll(course)  # Should fail
    print(f"Enrolling to full course: {result}")
    
    # Make room by unenrolling
    student1.unenroll(course)
    result = student3.enroll(course)  # Should succeed now
    print(f"Enrolling after unenrollment: {result}")
    
    # Check final state
    print(f"Final students in course: {len(course.students)}")
    print(f"Students are: {[s.name for s in course.students]}")

elif test_case == "integrated_test":
    # Test the entire system working together
    # Create courses
    python_course = Course("Python 101", "Introduction to Python", 3)
    data_course = Course("Data Science", "Advanced data analysis", 2)
    
    # Create students
    alice = Student("Alice", "alice@example.com")
    bob = Student("Bob", "bob@example.com")
    charlie = Student("Charlie", "charlie@example.com")
    
    # Create instructor
    dr_smith = Instructor("Dr. Smith", "smith@example.edu", "Computer Science")
    
    # Assign instructor
    dr_smith.assign_to_course(python_course)
    dr_smith.assign_to_course(data_course)
    
    # Enroll students
    alice.enroll(python_course)
    bob.enroll(python_course)
    charlie.enroll(python_course)
    
    alice.enroll(data_course)
    bob.enroll(data_course)  # This fills data_course
    
    # Complete a course
    alice.complete_course(python_course)
    
    # Print system state
    print("System State:")
    print(f"Python course has {len(python_course.students)} active students and {len(python_course.completed_students)} completed")
    print(f"Data course has {len(data_course.students)} active students")
    print(f"Dr. Smith teaches {len(dr_smith.courses)} courses")
    print(f"Alice is enrolled in {len(alice.enrolled_courses)} courses and completed {len(alice.completed_courses)}")
    print(f"Charlie is enrolled in {len(charlie.enrolled_courses)} courses")

elif test_case == "edge_cases":
    # Test edge cases
    course = Course("Small Course", "Test edge cases", 1)
    student1 = Student("Alice", "alice@example.com")
    student2 = Student("Bob", "bob@example.com")
    
    # Test enrollment at exact capacity
    result1 = student1.enroll(course)
    result2 = student2.enroll(course)  # Should fail
    print(f"Enrollment at capacity: {result1}")
    print(f"Enrollment beyond capacity: {result2}")
    
    # Test completing a course student isn't enrolled in
    other_course = Course("Other Course", "Not enrolled")
    result3 = student1.complete_course(other_course)
    print(f"Complete non-enrolled course: {result3}")
    
    # Test unenrolling from a course student isn't enrolled in
    result4 = student2.unenroll(course)
    print(f"Unenroll from non-enrolled course: {result4}")
    
    # Test reassigning an instructor
    instructor1 = Instructor("Dr. Smith", "smith@example.edu", "Python")
    instructor2 = Instructor("Dr. Jones", "jones@example.edu", "Java")
    
    instructor1.assign_to_course(course)
    print(f"First instructor: {course.instructor.name}")
    
    instructor2.assign_to_course(course)
    print(f"After reassignment: {course.instructor.name}")

elif test_case == "capacity_limits":
    # Test capacity limits
    zero_capacity = Course("Empty Course", "No students allowed", 0)
    student = Student("Alice", "alice@example.com")
    
    result1 = student.enroll(zero_capacity)
    print(f"Enroll in zero-capacity course: {result1}")
    
    large_capacity = Course("Huge Course", "Many students", 1000)
    result2 = student.enroll(large_capacity)
    print(f"Enroll in large-capacity course: {result2}")
    print(f"Large course has capacity for {large_capacity.max_capacity} students")

elif test_case == "multiple_courses":
    # Test student with multiple courses
    student = Student("Alice", "alice@example.com")
    course1 = Course("Python 101", "Intro to Python")
    course2 = Course("Java 101", "Intro to Java")
    course3 = Course("C++ 101", "Intro to C++")
    
    # Enroll in all courses
    student.enroll(course1)
    student.enroll(course2)
    student.enroll(course3)
    print(f"Enrolled in {len(student.enrolled_courses)} courses")
    
    # Complete some courses
    student.complete_course(course1)
    student.complete_course(course2)
    print(f"After completion: Enrolled in {len(student.enrolled_courses)} courses")
    print(f"After completion: Completed {len(student.completed_courses)} courses")
    
    # Verify specific courses
    enrolled_titles = [c.title for c in student.enrolled_courses]
    completed_titles = [c.title for c in student.completed_courses]
    print(f"Still enrolled in: {enrolled_titles}")
    print(f"Completed: {completed_titles}")

elif test_case == "instructor_workload":
    # Test instructor with multiple courses
    instructor = Instructor("Dr. Smith", "smith@example.edu", ["Python", "Java", "C++"])
    course1 = Course("Python 101", "Intro to Python")
    course2 = Course("Java 101", "Intro to Java")
    course3 = Course("C++ 101", "Intro to C++")
    
    # Assign to all courses
    instructor.assign_to_course(course1)
    instructor.assign_to_course(course2)
    instructor.assign_to_course(course3)
    
    print(f"Instructor teaches {len(instructor.courses)} courses")
    course_titles = [c.title for c in instructor.courses]
    print(f"Courses taught: {course_titles}")
    
    # Verify instructor is properly assigned to each course
    for i, course in enumerate([course1, course2, course3]):
        print(f"Course {i+1} instructor: {course.instructor.name}")