# Írj egy Iskola osztályt
# - __init__: nev, tanulok = {} (dictionary: nev -> jegyek listája)
# - hozzaad_tanulo(nev): hozzáadja a tanulót üres listával
# - jegy_hozzaad(nev, jegy): hozzáadja a jegyet a tanuló listájához
# - atlag(nev): visszaadja a tanuló átlagát
# - legjobb_tanulo(): visszaadja a legjobb átlagú tanuló nevét
# - __str__: kiírja az összes tanulót és átlagukat
class Iskola:
    def __init__(self, nev):
        self.nev = nev
        self.tanulok = {}
    def hozzaad_tanulo(self, diak):
        self.tanulok[diak]=[]
    def jegy_hozzaad(self, diak, jegy):
        self.tanulok[diak].append(jegy)
    def atlag(self, diak):
        return round((sum(self.tanulok[diak]))/(len(self.tanulok[diak])),2)
    def legjobb_tanulo(self):
        legjobb = 0
        legjobb_diak = None
        for diak in self.tanulok:
            if self.atlag(diak) > legjobb:
                legjobb = self.atlag(diak)
                legjobb_diak = diak
        return legjobb_diak
    def __str__(self):
        osszes_atlag = {}
        for diak in self.tanulok:
            osszes_atlag[diak] = self.atlag(diak)
        return f"{osszes_atlag}"



i = Iskola("Python Iskola")
i.hozzaad_tanulo("Anna")
i.hozzaad_tanulo("Béla")
i.jegy_hozzaad("Anna", 5)
i.jegy_hozzaad("Anna", 4)
i.jegy_hozzaad("Béla", 3)
i.jegy_hozzaad("Béla", 5)
print(i.atlag("Anna"))
print(i.atlag("Béla"))

print(i.legjobb_tanulo())
print(i)