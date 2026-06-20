# Írás
f = open(r"C:\\PYTHON\0064 - File Handling\hello.txt", "a")
f.write('abrakadabra')
f.close()

# Olvasás ellenőrzés
f = open(r"C:\\PYTHON\0064 - File Handling\hello.txt", "r")
print(f.read())
f.close()

def get_max_min_numbers(filename):
    # Write code here
    with open(filename) as f:
        print(f.read().split(','))
        return f"{max(list(f.read().split(',')))}, {min(list(f.read().split(',')))}"
            
def average_word_length(filename):
    with open(filename, 'r') as f:
        # 1. Beolvasunk mindent egyben
        content = f.read()
        
        # 2. Írásjelek cseréje szóközre, hogy a szavak ne "ragadjanak össze"
        for char in "!?\'\",.":
            content = content.replace(char, " ")
        
        # 3. Szavakra bontás (a split() paraméter nélkül a legjobb: 
        # kezeli az újsorokat és a többszörös szóközöket is)
        words = content.split()
        
        # 4. Hosszok kiszámítása (ha a szó üres volt, az split() nem adja vissza, 
        # így a len() mindig a valódi szavak hosszát adja)
        if not words:
            return 0.0
            
        total_length = sum(len(word) for word in words)
        avg = total_length / len(words)
        
        return round(avg, 2)
    

