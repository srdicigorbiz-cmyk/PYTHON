from abc import ABC, abstractmethod
class Bank:
    def __init__(self, limit):
        self.tranzakciok = {}
        self.tranzakciok_szama = 0
        self.megfigyelok = []
        self.limit = limit
    def feliratkozo(self, feliratkozo):
        if isinstance(feliratkozo, MegfigyeloBase):
            if feliratkozo not in self.megfigyelok:
                self.megfigyelok.append(feliratkozo)
        else:
            print("Hiba: Ez az objektum nem érvényes megfigyelő!")
    def leiratkozo(self, leiratkozo):
        self.megfigyelok.remove(leiratkozo)

    def utalas(self, nev, osszeg):
        
        elozo_osszeg = self.tranzakciok.get(nev, 0)
        self.tranzakciok[nev]= elozo_osszeg + osszeg
                
        print(f"Sikeres utalas {nev} részére, {osszeg} Ft")

        if elozo_osszeg <= self.limit and self.tranzakciok[nev] > self.limit:
            for figyelo in self.megfigyelok:
                figyelo.figyelmeztet(nev, osszeg)
        
        self.tranzakciok_szama += 1
        
    
    def gyanus_ugyletek(self):
        gyanusak = dict()
        for key, value in self.tranzakciok.items():
            if value > self.limit:
                gyanusak[key]=value
        return gyanusak
    def __str__(self):
        return f"Banki napló: {self.tranzakciok_szama} db tranzakció."
class MegfigyeloBase(ABC):
    @abstractmethod
    def figyelmeztet(self, nev, osszeg):
        pass
class Ellenor(MegfigyeloBase):
    def figyelmeztet(self, nev, osszeg):
        print(f"RIASZTÁS: {nev} gyanús utalást végzett: {osszeg} Ft!")

class Logger(MegfigyeloBase):
    def figyelmeztet(self, nev, osszeg):
        print(f"Log: {nev} gyanús utalást végzett: {osszeg} Ft!")

e = Ellenor()
l = Logger()


b = Bank(100000) # Az ellenőrt és a 150.000-es limitet is átadjuk
b.feliratkozo(e)
b.feliratkozo(l)

b.utalas("János", 50000)
b.utalas("Sára", 200000) # Ez elvileg azonnal ki kell váltson egy riasztást!
b.utalas("János", 50000)
b.utalas("János", 60000)
b.utalas("Péter", 120000)
b.utalas("Anna", 30000)
b.utalas("Sára", 200000)

print(b.gyanus_ugyletek()) # Elvárt: {'Péter': 120000, 'Sára': 200000}
print(b)                         # Elvárt: Banki napló: 4 db tranzakció.
