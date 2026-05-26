# Van: Elofizetes, EgyszeriFizetes, IngyenesFizetes osztályok
# __init__: felhasznalo_nev
# fizet(osszeg): 
#   Elofizetes: "X előfizető: 20% kedvezmény, fizet: Y Ft"
#   EgyszeriFizetes: "X egyszer fizet: Y Ft"
#   IngyenesFizetes: "X ingyenes hozzáférés"
# Van: FizetesFactory – dictionary alapú, raise ValueError
class Elofizetes:
    def __init__(self, felhasznalo_nev):
        self.felhasznalo_nev = felhasznalo_nev
    def fizet(self, osszeg):
        return f"{self.felhasznalo_nev} előfizető: 20% kedvezmény, fizet: {osszeg} Ft"

class EgyszeriFizetes:
    def __init__(self, felhasznalo_nev):
        self.felhasznalo_nev = felhasznalo_nev
    def fizet(self, osszeg):
        return f"{self.felhasznalo_nev} egyszer fizet: {osszeg} Ft"

class IngyenesFizetes:
    def __init__(self, felhasznalo_nev):
        self.felhasznalo_nev = felhasznalo_nev
    def fizet(self, osszeg):
        return f"{self.felhasznalo_nev} ingyenes hozzaferes"

class FizetesFactory:
    def __init__(self):
        self.lista = {
            "elofizeteses": Elofizetes,
            "egyszeri": EgyszeriFizetes,
            "ingyenes": IngyenesFizetes
        }
    def letrehoz(self, tipus, nev):
        if tipus in self.lista:
            return self.lista[tipus](nev)
        else:
            raise ValueError("Hiba. Nem letezo fizetestipus.")

f = FizetesFactory()
print(f.letrehoz("elofizeteses", "Anna").fizet(10000))
print(f.letrehoz("egyszeri", "Béla").fizet(5000))
print(f.letrehoz("ingyenes", "Cili").fizet(0))
print(f.letrehoz("bitcoin", "Dani").fizet(1000))  # ValueError!