# Írj egy ItalFactory-t
# - Kave, Tea, Viz osztályok, mindegyiknek: nev() metódus
# - Factory dictionary alapú, raise ValueError ha ismeretlen
class Kave:
    def nev(self):
        return "Ez egy kave"
class Tea:
    def nev(self):
        return "Ez egy Tea"
class Viz:
    def nev(self):
        return "Ez egy viz"

class ItalFactory:
    def __init__(self):        
        if not hasattr(self, "italok"):
            self.italok = {
                "kave": Kave,
                "tea": Tea,
                "viz": Viz
            }
    

    
    def letrehoz(self, cls):
        if cls.lower() in self.italok:
            return self.italok[cls.lower()]()
        else:
            raise ValueError("Ismeretlen!")



f = ItalFactory()
print(f.letrehoz("kave").nev())
print(f.letrehoz("viz").nev())
print(f.letrehoz("sor").nev())  # ValueError!