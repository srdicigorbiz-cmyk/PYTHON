def analyze_grades(grades):
    # Write code here


    average_grade=round((sum(grades.values())/len(grades.items())),2)
    highest_grade=max(grades.values())
    lowest_grade=min(grades.values())
    
    top_student= None
    bottom_student = None

    for student in grades:
        
        if grades[student] == highest_grade:
            top_student=(student)
        if grades[student] == lowest_grade:
             bottom_student=(student)
        

    result={"average":average_grade,
            "highest":highest_grade, 
            "lowest": lowest_grade , 
            "top_student": top_student , 
            "bottom_student": bottom_student}

    return result

# Test the function
student_grades = {'Alice': 85, 'Bob': 92, 'Charlie': 78, 'David': 95, 'Eve': 88}
result = analyze_grades(student_grades)
print(result)