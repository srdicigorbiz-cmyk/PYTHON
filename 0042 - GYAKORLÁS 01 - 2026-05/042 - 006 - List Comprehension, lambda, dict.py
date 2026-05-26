# Írj egy Konyvtar osztályt
# - __init__: nev, keszlet = {} (dictionary: cim -> (szerzo, ar, darab))
# - hozzaad(cim, szerzo, ar, darab): hozzáadja a könyvet
# - vasarol(cim): csökkenti a darabszámot 1-gyel, ha van készlet
#   különben: "Elfogyott!"
# - kereses(szerzo): visszaadja az adott szerző összes könyvét
# - legdragabb(): visszaadja a legdrágább könyv címét
# - __str__: "Könyvtár: X, Könyvek száma: Y"
class Konyvtar:
    def __init__(self, nev):
        self.nev = nev
        self.keszlet = dict()
        
    def hozzaad(self,cim, szerzo, ar, darab):
        self.keszlet[cim] = [szerzo, ar, darab]
    def vasarol(self, cim):
        if cim in self.keszlet:
            if self.keszlet[cim][2]<1:
                print("Elfogyott!")
            else:
                self.keszlet[cim][2] -= 1
                print("Sikeres vasarlas!")

    def kereses(self, szerzo):
        return f"A kereses eredmenye: {[{cim: adat} for cim, adat in self.keszlet.items() if adat[0] == szerzo]}"
                
    def legdragabb(self):
        
        return f"Legdragabb könyv cim: {max(self.keszlet.items(), key=lambda item: item[1][1])[0]}"
                
        """
        max_ar = None
        max_cim = None
        for cim, adatok in self.keszlet.items():
            if max_ar is None:
                max_ar = adatok[1]
                max_cim = cim
            else:
                if max_ar < adatok[1]:
                    max_ar = adatok[1]
                    max_cim = cim
        return f"Legdragabb könyv cim: {max_cim}."
        """
    
    def __str__(self):
        konyvek_szama = 0
        for cim, adat in self.keszlet.items():
            konyvek_szama += adat[2]
        return f"Könyvtár: {self.nev} , Könyvek száma:{konyvek_szama}"

k = Konyvtar("Peti könyvtára")
k.hozzaad("Python alapok", "Kiss J.", 5000, 3)
k.hozzaad("Clean Code", "Martin R.", 8000, 1)
k.hozzaad("Python haladó", "Kiss J.", 7000, 2)
print(k.kereses("Kiss J."))
print(k.legdragabb())
k.vasarol("Clean Code")
k.vasarol("Clean Code")  # Elfogyott!
print(k)
