from student import Student
from studentregistry import StudentRegistry
import time
import random

# Test case handler for comprehensive testing
test_case = input()

if test_case == "default_test":
    # Create students
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

    # Display student records
    print("Student Records:")
    student1.display_record()
    print()
    student2.display_record()
    print()
    student3.display_record()
    print()

    # Test name validation
    try:
        student1.name = "J"  # Too short
    except ValueError as e:
        print(f"Name validation error: {e}")
    print()

    # Create registry and add students
    registry = StudentRegistry()
    registry.add_student(student1)
    registry.add_student(student2)
    registry.add_student(student3)

    # Display all students
    print("All Students in Registry:")
    registry.display_all()
    print()

    # Get top student
    top_student = registry.get_top_student()
    print(f"Top Student: {top_student.name} (Average: {top_student.grade_average})")

    # Remove a student
    registry.remove_student(1002)  # Remove Bob
    print("\
After removing student 1002:")
    registry.display_all()

elif test_case == "empty_registry":
    # Test an empty registry
    registry = StudentRegistry()
    top_student = registry.get_top_student()
    if top_student is None:
        print("Top student in empty registry: None")
    print("Displaying all students in empty registry:")
    registry.display_all()  # Should not display anything

elif test_case == "validation_tests":
    # Test all validation rules
    student = Student(1001, "Valid Name")
    print(f"Created student with name: {student.name}")
    
    # Test empty name
    try:
        student.name = ""
    except ValueError as e:
        print(f"Empty name test: {e}")
    
    # Test single character name
    try:
        student.name = "A"
    except ValueError as e:
        print(f"Single character name test: {e}")
    
    # Test non-boolean enrolled value
    try:
        student.enrolled = "yes"
    except ValueError as e:
        print(f"Non-boolean enrolled test: {e}")
    
    # Test valid changes
    student.name = "New Valid Name"
    student.enrolled = False
    print(f"After valid changes - Name: {student.name}, Enrolled: {student.enrolled}")

elif test_case == "grade_calculation":
    # Test grade average calculation
    student = Student(1001, "Test Student")
    print(f"Student with no grades - Average: {student.grade_average}")
    
    # Add one grade
    student.add_grade("Math", 85)
    print(f"Student with one grade - Average: {student.grade_average}")
    
    # Add more grades
    student.add_grade("Science", 90)
    student.add_grade("English", 95)
    print(f"Student with multiple grades - Average: {student.grade_average}")

elif test_case == "registry_operations":
    # Test all registry operations
    registry = StudentRegistry()
    
    # Create students
    student1 = Student(101, "Student One")
    student2 = Student(102, "Student Two")
    
    # Add students
    registry.add_student(student1)
    registry.add_student(student2)
    print("After adding students:")
    registry.display_all()
    
    # Get student
    retrieved_student = registry.get_student(101)
    print(f"\
Retrieved student 101: {retrieved_student.name if retrieved_student else None}")
    
    # Get non-existent student
    non_existent = registry.get_student(999)
    print(f"Retrieved student 999: {non_existent}")
    
    # Remove student
    registry.remove_student(101)
    print("\
After removing student 101:")
    registry.display_all()
    
    # Remove non-existent student (should not raise error)
    registry.remove_student(999)
    print("\
After attempting to remove non-existent student 999:")
    registry.display_all()

elif test_case == "large_registry":
    # Test performance with many students
    start_time = time.time()
    registry = StudentRegistry()
    
    # Create 100 students with random grades
    for i in range(1, 101):
        student = Student(1000 + i, f"Student {i}")
        # Add 5 random grades
        for j in range(5):
            student.add_grade(f"Course {j+1}", random.randint(60, 100))
        registry.add_student(student)
    
    creation_time = time.time() - start_time
    print(f"Time to create 100 students: {creation_time:.4f} seconds")
    
    # Find top student
    start_time = time.time()
    top_student = registry.get_top_student()
    top_time = time.time() - start_time
    print(f"Time to find top student: {top_time:.4f} seconds")
    print(f"Top student: {top_student.name} with average {top_student.grade_average:.2f}")
    
    # Find top 5 students manually
    print("\
Top 5 students:")
    students_list = []
    for i in range(1, 101):
        student = registry.get_student(1000 + i)
        students_list.append(student)
    
    # Sort by grade average in descending order
    students_list.sort(key=lambda s: s.grade_average, reverse=True)
    
    # Display top 5
    for i in range(5):
        student = students_list[i]
        print(f"{i+1}. {student.name}: {student.grade_average:.2f}")