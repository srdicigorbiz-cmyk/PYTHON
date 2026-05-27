class Raktar:
    def __init__(self):  
        self.keszlet = dict()
    def beszerzes(self, nev, ar, db):
        self.keszlet[nev] = (ar, db)
    def ertek(self, nev):
        if nev in self.keszlet:
            return self.keszlet[nev][0]*self.keszlet[nev][1]
        else:
            raise ValueError("Nincs ilyen termék!")
    def legdragabb(self):
        return f"A legdragabb: {max(self.keszlet.items(), key= lambda x: x[1][0])[0]}"
    def __str__(self):
        return f"Raktárkészlet: {', '.join(self.keszlet.keys())}"
    
r = Raktar()
r.beszerzes("Monitor", 50000, 10)
r.beszerzes("Billentyűzet", 15000, 45)
r.beszerzes("Egér", 8000, 100)
r.beszerzes("Laptop", 250000, 3)

print(r.ertek("Monitor"))     # Elvárt: 500000
print(r.legdragabb())         # Elvárt: Laptop
print(r)                      # Elvárt: Raktárkészlet: Monitor, Billentyűzet, Egér, Laptop
# Teszteld a hibaüzenetet is:
# print(r.ertek("Kamera"))    # Elvárt: ValueError