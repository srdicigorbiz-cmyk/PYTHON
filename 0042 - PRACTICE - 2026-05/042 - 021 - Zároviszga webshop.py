# ZÁRÓVIZSGA FELADAT
# Írj egy Webshop rendszert az alábbiak szerint:

# 1. Termek osztály:
#    - __init__: nev, ar, keszlet
#    - @property + setter: ar – csak pozitív
#    - @property + setter: keszlet – csak >= 0
#    - __str__: "Termek: X, Ár: Y Ft, Készlet: Z db"
class Termek:
    def __init__(self, nev, ar, keszlet):
        self.nev = nev
        self.ar = ar
        self.keszlet = keszlet
    @property
    def ar(self):
        return self._ar
    @ar.setter
    def ar(self,ertek):
        if ertek > 0:
            self._ar = ertek
    @property
    def keszlet(self):
        return self._keszlet
    @keszlet.setter
    def keszlet(self, ertek):
        if ertek >= 0:
            self._keszlet = ertek
    def __str__(self):
        return f"Termek: {self.nev}, Ár: {self.ar} Ft, Készlet: {self.keszlet} db"
# 2. TermekFactory – dictionary alapú:
#    - letrehoz(tipus, nev, ar, keszlet)
#    - tipusok: "elektronika", "ruha", "elelmiszer"
class Elektronika(Termek):
    def __init__(self, nev, ar, keszlet):
        super().__init__(nev, ar, keszlet)
        self.tipus = "Elektronika"
    def __str__(self):
        return f"Termek: {self.nev}, Ár: {self.ar} Ft, Készlet: {self.keszlet} db, Típus: {self.tipus}."
class Ruha(Termek):
    def __init__(self, nev, ar, keszlet):
        super().__init__(nev, ar, keszlet)
        self.tipus = "Ruha"
    def __str__(self):
        return f"Termek: {self.nev}, Ár: {self.ar} Ft, Készlet: {self.keszlet} db, Típus: {self.tipus}."
class Elelmiszer(Termek):
    def __init__(self, nev, ar, keszlet):
        super().__init__(nev, ar, keszlet)
        self.tipus = "Elelmiszer"
    def __str__(self):
        return f"Termek: {self.nev}, Ár: {self.ar} Ft, Készlet: {self.keszlet} db, Típus: {self.tipus}."
class TermekFactory:
#    - minden típusnak saját osztálya van ami örököl Termek-ből
#    - minden gyerek __str__-je tartalmazza a típust is
    def __init__(self):
        self.lista = {
            "elektronika": Elektronika,
            "ruha": Ruha,
            "elelmiszer" : Elelmiszer
                    }
    def letrehoz(self,tipus, nev, ar, keszlet):
        if tipus in self.lista:
            return self.lista[tipus.lower()](nev, ar, keszlet)
        else:
            raise ValueError("Hiba.Ilyen tipus nincs.")
# 3. Webshop osztály (Singleton!):
class Webshop:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
#    - keszlet = {} (dictionary: nev -> Termek objektum)
        if not hasattr(self, "keszlet"):
            self.keszlet = dict()

    def hozzaad(self, termek):
#    - hozzaad(termek): hozzáadja a terméket          
        self.keszlet[termek.nev] = termek

    def vasarol(self, nev, darab):
#    - vasarol(nev, darab): csökkenti a készletet, raise ValueError ha nincs elég
        if nev in self.keszlet.keys():
            if self.keszlet[nev].keszlet >= darab:
                self.keszlet[nev].keszlet -= darab
            else:
                raise ValueError("Nincs elég termék a készleten!")

        else:
            raise ValueError("Ilyen termék nincs a készleten.")

    def kereses(self, max_ar):
#    - kereses(max_ar): visszaadja az összes terméket ami olcsóbb – filter+lambda
        #result=[]
        #for key, value in self.keszlet.items():
        #    if self.keszlet[key].ar < max_ar:
        #        result.append({key:self.keszlet[key].ar})
        #return {result}"
        
        #return f"A keresett termekek olcsobbak: {list(map(lambda x: f"{x.nev}: {x.ar}", list(filter(lambda x: x.ar<max_ar, self.keszlet.values()))))}"
        
        return f"A keresett termekek olcsobbak: {list(map(lambda x: f"{x.nev}: {x.ar}", list(filter(lambda x: x.ar<max_ar, self.keszlet.values()))))}"

    def legdragabb(self):
#    - legdragabb(): visszaadja a legdrágább terméket – max+lambda
        return f"A legdragabb termek és ára: {max([[key, value.ar] for key, value in self.keszlet.items()], key=lambda x: x[1])}"


    def osszErtek(self):
#    - osszErtek(): az összes termék (ar * keszlet) összege – map+sum+lambda
        #result=0
        #for key, value in self.keszlet.items():
        #    result += self.keszlet[key].ar*self.keszlet[key].keszlet
                
        #return f"Az összes termék összege: {result}"

        return f"Az összes termék összege: {sum(map(lambda x: x.ar * x.keszlet, self.keszlet.values()))}"
         


# Teszteld:
shop = Webshop()
shop.hozzaad(TermekFactory().letrehoz("elektronika", "Laptop", 500000, 5))
shop.hozzaad(TermekFactory().letrehoz("ruha", "Póló", 5000, 20))
shop.hozzaad(TermekFactory().letrehoz("elelmiszer", "Alma", 500, 100))

shop.vasarol("Laptop", 2)
print(shop.legdragabb())
print(shop.kereses(10000))
print(shop.osszErtek())