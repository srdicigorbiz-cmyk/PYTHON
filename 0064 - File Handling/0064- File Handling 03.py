def solve_scores(filename):
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]
        
        # A fejléc az első sor, a diákok a többi
        header = lines[0].split(',')[1:] # ['Math', 'Science', 'History']
        students = [line.split(',') for line in lines[1:]]
        
        print("Highest Scores:")
        
        # Végigmegyünk a tantárgyakon (oszlopokon)
        # i a tantárgy indexe (0, 1, 2...)
        for i, subject in enumerate(header):
            max_score = -1
            best_student = ""
            
            # Megkeressük az adott tantárgyhoz tartozó legmagasabb pontszámot
            for student_data in students:
                name = student_data[0]
                score = int(student_data[i + 1]) # +1 mert a 0. oszlop a név
                
                if score > max_score:
                    max_score = score
                    best_student = name
            
            print(f"{subject}: {best_student} ({max_score})")

# Hívd meg a függvényt a fájllal:
solve_scores(r"C:\PYTHON\0064 - File Handling\scores.txt")