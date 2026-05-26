class Kosar:
    def __init__(self, termeklista):
        self.termeklista = termeklista
    
    def termek_arak(self):
        return(list(map(lambda x: x["ar"], self.termeklista)))

    def nagyobb_mint(self):
        return list(filter(lambda x: x["ar"]>=5000 , self.termeklista))
    
class Megrendeles:
    def __init__(self, kosar):
        self.kosar = kosar
        self.strategia = None
    def strategiavalaszto(self, strategia):
        self.strategia = strategia
    def fizet(self):
        kosarerteke = sum(list(map(lambda x: x["ar"], self.kosar.termeklista)))
        return self.strategia.alkalmaz(kosarerteke)

class FixKedvezmeny:
    def alkalmaz(self, osszeg):
        return osszeg - 1000

class SzazalekosKedvezmeny:
    def alkalmaz(self, osszeg):
        return osszeg * 0.9

            
#TEST    
kosar = Kosar([{"nev":"Dezodor","ar":5500},{"nev":"Keksz", "ar":150},{"nev":"Kenyer", "ar":100},{"nev":"Sajt", "ar":500}])
print(kosar.termek_arak())
print(kosar.nagyobb_mint())
megrendeles = Megrendeles(kosar)

fix = FixKedvezmeny()
szazalek = SzazalekosKedvezmeny()
megrendeles.strategiavalaszto(fix)
print(megrendeles.fizet())
megrendeles.strategiavalaszto(szazalek)
print(megrendeles.fizet())
