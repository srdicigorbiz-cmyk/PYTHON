# TODO: Tranzakcio szülő osztály
# Attribútumok: datum, megnevezes, forras, osszeg, tipus
# __str__: "{datum} | {megnevezes} | {forras} | {osszeg} Ft | {tipus}"
class Tranzakcio:
    def __init__(self, esemeny_datum, tranzakcio_datum, megnevezes, kliens, arfolyam, osszeg, tipus):
        self.esemeny_datum=esemeny_datum
        self.tranzakcio_datum = tranzakcio_datum
        self.megnevezes = megnevezes
        self.kliens = kliens
        self.arfolyam = arfolyam
        self.osszeg = osszeg
        self.tipus = tipus

    def __str__(self):
        return f"{self.esemeny_datum} | {self.tranzakcio_datum} | {self.megnevezes} | {self.kliens} | {self.arfolyam:.2f} | {self.osszeg} EUR | {self.tipus}"

    
# TODO: Bevetel osztály - örököl Tranzakciotól
# - @property + setter az összegre
# - setter: csak pozitív számot fogad el
# - különben raise ValueError: "A bevétel csak pozitív lehet!"
class Bevetel(Tranzakcio):
    def __init__(self, esemeny_datum, tranzakcio_datum, megnevezes, kliens, arfolyam, osszeg, tipus):
        super().__init__(esemeny_datum, tranzakcio_datum, megnevezes, kliens, arfolyam, osszeg, tipus)
    
    @property
    def osszeg(self):
        return self._osszeg
    
    @osszeg.setter
    def osszeg(self, ertek):
        if ertek <=0:
            raise ValueError("A bevétel csak pozitív lehet!")
        else:
            self._osszeg = ertek


# TODO: Kiadas osztály - örököl Tranzakciotól  
# - @property + setter az összegre
# - setter: csak negatív számot fogad el
# - ha valaki pozitívat ad meg, alakítsd át negatívra automatikusan
class Kiadas(Tranzakcio):
    def __init__(self, esemeny_datum, tranzakcio_datum, megnevezes, kliens, arfolyam, osszeg, tipus):
        super().__init__(esemeny_datum, tranzakcio_datum, megnevezes, kliens, arfolyam, osszeg, tipus)
    
    @property
    def osszeg(self):
        return self._osszeg
    
    @osszeg.setter
    def osszeg(self, ertek):
        if ertek >=0:
            self._osszeg = ertek*-1
        else:
            self._osszeg = ertek

# TODO: Tranzakciok osztály
# - __init__: üres lista (tranzakciok = [])
# - hozzaad(tranzakcio): listához adja a tranzakciót
# - merleg(): összeadja az összes tranzakció összegét és visszaadja
class Tranzakciok:
    def __init__(self):
        self.tranzakciok = []
    
    def hozzad(self, tranzakcio):
        self.tranzakciok.append(tranzakcio)

    def merleg(self):
        eredmeny = 0
        for t in self.tranzakciok:
            eredmeny += t.osszeg
            
        return eredmeny
    
    def sum_bevetel(self):
        eredmeny = 0
        for t in self.tranzakciok:
            if isinstance(t, Bevetel):
                eredmeny += t.osszeg
        return eredmeny

    def sum_kiadas(self):
        eredmeny = 0
        for t in self.tranzakciok:
            if isinstance(t, Kiadas):
                eredmeny += t.osszeg
        return eredmeny



# TODO: szures(self, ev=None, honap=None, nap=None)
# - ha ev=None, ne szűrj évre
# - ha honap=None, ne szűrj hónapra
# - ha nap=None, ne szűrj napra
# - írd ki a megfelelő tranzakciókat és add vissza az összeget
    def szures(self, ev=None, honap=None, nap=None):
        print("A vizsgált tranzakciók listája:")
        eredmeny = 0
        
        for t in self.tranzakciok:            
            reszek = t.esemeny_datum.split('-')
            if (ev is None or ev==int(reszek[0])) and (honap is None or honap==int(reszek[1])) and (nap is None or nap==int(reszek[2])):
                eredmeny += t.osszeg
                print(t)
        return eredmeny

#P É N Z T Á R#################################################################
#Penztar
class Penztar:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)    
        return cls._instance
    
    def __init__(self):
        if not hasattr(self, "penztarfiokok"):
            self.penztarfiokok=[]
    
    def hozzad(self, fiok):
        self.penztarfiokok.append(fiok)

    def osszes_osszeg(self):
        eredmeny = 0
        for p in self.penztarfiokok:
            eredmeny += p.osszeg
        return eredmeny
    
    def osszeg_update (self, fioknev, ertek):
        for fiok in self.penztarfiokok:
            if fiok.megnevezes == fioknev:
                fiok.osszeg = ertek

class Fiok:    
    def __init__(self, megnevezes, osszeg, penznem="EUR"):
        self.megnevezes = megnevezes
        self.osszeg = osszeg
        self.penznem = penznem
    def __str__(self):
        return f"{self.megnevezes} | {self.osszeg} | {self.penznem}"
    @property
    def osszeg(self):
        return self._osszeg
    @osszeg.setter
    def osszeg(self, ertek):
        if ertek >= 0:
            self._osszeg= ertek

# TODO: Egyensuly osztály
# - @staticmethod: egyensuly(konyvelt, valosnpenz)
# - adja vissza a különbséget
# - ha 0: "Egyensúlyban"
# - ha nem 0: "Eltérés: X EUR"    
class Mutatok:
    def __init__(self, tranzakciok, penztar):
        self.tranzakciok = tranzakciok
        self.penztar = penztar

    def egyensuly(self):
        konyvelt = self.tranzakciok.merleg()
        valospenz = self.penztar.osszes_osszeg()
        if konyvelt-valospenz ==0:
            return "A könyvelés és a pénztár egyensúlyban van."
        else:
            return f"A könyvelés és a pénztár közti eltérés {konyvelt-valospenz} EUR"

