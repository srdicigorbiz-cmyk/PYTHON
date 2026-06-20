f = open(r"C:\PYTHON\0064 - File Handling\scores.txt")
data = [x.split(",") for x in f.read().split()]
grades = dict()
for score in data[1:]:
    grades[score[0]]=int(score[1]), int(score[2]), int(score[3])


math = max([(x[1][0],x[0]) for x in grades.items()])
science = max([(x[1][1],x[0]) for x in grades.items()])
history = max([(x[1][2],x[0]) for x in grades.items()])


print("Highest Scores:")
print(f"{data[0][1]}: {math[1]} ({math[0]})")
print(f"{data[0][2]}: {science[1]} ({science[0]})")
print(f"{data[0][3]}: {history[1]} ({history[0]})")
