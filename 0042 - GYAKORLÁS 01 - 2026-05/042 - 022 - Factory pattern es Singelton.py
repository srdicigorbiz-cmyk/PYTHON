class Raktar:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    def __init__(self):
        if not hasattr(self, "_keszlet"):
            self._keszlet = dict()
    def alacsony_keszlet(self, limit):
        # A filter a self._keszlet.items() elemeit szűri a lambda alapján
        szurt_elemek = filter(lambda x: x[1]<limit, self._keszlet.items())
        return dict(szurt_elemek)

class TermekFactory:
    def __init__(self):
        self.lista={
            "tartos":TartosElelmiszer,
            "friss":FrissAru

        }
    def letrehoz(self, tipus, nev, ar):
        if tipus in self.lista.keys():
            return self.lista[tipus](nev, ar)
        else:
            raise ValueError("Ilyen tipus nincs")

class TartosElelmiszer:
    def __init__(self, nev, ar):
        self.nev = nev
        self.ar = ar
class FrissAru:
    def __init__(self, nev, ar):
        self.nev = nev
        self.ar = ar




r = Raktar()
r._keszlet = {"Tej": 5, "Kenyér": 2, "Sajt": 10, "Alma": 1}

# Teszt: keressük a 3-nál kevesebb termékeket
print(r.alacsony_keszlet(3))  
# Elvárt eredmény: {'Kenyér': 2, 'Alma': 1}



# Regisztráció és gyártás tesztelése
factory = TermekFactory()
# Itt hívd meg a letrehoz metódust

try:
    termek1 = factory.letrehoz("tartos", "Liszt", 350)
    print(f"Sikeres: {type(termek1).__name__} - {termek1.nev}")
    
    # Hiba tesztelése:
    factory.letrehoz("ruha", "Póló", 5000)
except ValueError as e:
    print(f"Hiba elkapva: {e}")