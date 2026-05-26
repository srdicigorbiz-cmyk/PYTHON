# Írj egy Verseny osztályt
# - __init__: nev, eredmenyek = [] (lista of tuple-ok: (nev, ido))
# - hozzaad(nev, ido): hozzáad egy (nev, ido) tuple-t
# - gyoztes(): visszaadja a legkisebb idővel rendelkező nevet
# - top3(): visszaadja a 3 legjobb eredményt rendezve
# - __str__: "Verseny: X, Indulók: Y"
class Verseny:
    def __init__(self, nev):
        self.nev = nev
        self.eredmenyek = []
        
    def hozzaad(self, nev, ido):
        self.eredmenyek.append((nev,ido))
    def gyoztes(self):
        gyoztes = min(self.eredmenyek, key = lambda x: x[1])
        return gyoztes[0]

    def top3(self):
        lista = sorted(self.eredmenyek, key= lambda x: x[1])
        top3 = lista[0:3]         
        
        return top3

    def __str__(self):
        return f"Verseny: {self.nev}, Indulók: {list(map(lambda x: x[0], self.eredmenyek))}"
    

v = Verseny("Maraton")
v.hozzaad("Anna", 245)
v.hozzaad("Béla", 198)
v.hozzaad("Cili", 210)
v.hozzaad("Dani", 188)
print(v.eredmenyek)

print(v.gyoztes())
print(v.top3())
print(v)
