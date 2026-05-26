def transform_dataset(data):
    #######################
    #passed students list
    #######################
    passed=[]
    for student in data:
        if all(grade > 70 for grade in student['grades']):
            passed.append(student)
    
    #######################    
    #average grade 2 decimals
    #######################
    
    qualified_students = {'qualified_students':{},'subject_summary':{}}
    
    for student in passed:
        avg_grade=round(sum(student["grades"])/len(student["grades"]),2)
        qualified_students['qualified_students'][student['student_id']]=avg_grade
    
    #######################    
    #subjects count
    #######################
    for student in passed:
        for subject in student['subjects']:
            if subject in qualified_students['subject_summary'].keys():
                qualified_students['subject_summary'][subject] += 1
            else:
                qualified_students['subject_summary'][subject] = 1
         
    
    return qualified_students


students=[{"student_id": "S1", "grades": [72, 73, 74], "subjects": ["Physics"]}, 
          {"student_id": "S2", "grades": [75, 76, 77], "subjects": ["Chemistry"]}, 
          {"student_id": "S3", "grades": [78, 79, 80], "subjects": ["Biology"]}, 
          {"student_id": "S4", "grades": [70, 85, 90], "subjects": ["Math"]}, 
          {"student_id": "S5", "grades": [95, 65, 85], "subjects": ["English"]}]
print(transform_dataset(students))