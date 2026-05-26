from abc import ABC, abstractmethod

class SzervezetiEgyseg(ABC):
    @abstractmethod
    def koltseg_szamit(self):
        pass
    @abstractmethod
    def letszam_szamit(self):
        pass


class Alkalmazott(SzervezetiEgyseg):
    def __init__(self, nev, fizetes):
        self.nev = nev
        self.fizetes = fizetes
    def koltseg_szamit(self):
        return self.fizetes
    def letszam_szamit(self):
        return 1

class Reszleg(SzervezetiEgyseg):
    def __init__(self, nev):
        self.nev = nev
        self.egysegek = []
    def hozzad(self, egyseg):
        self.egysegek.append(egyseg)
    def koltseg_szamit(self):
        return sum(list(map(lambda x: x.koltseg_szamit(), self.egysegek)))
    def letszam_szamit(self):
        return sum(list(map(lambda x: x.letszam_szamit(), self.egysegek)))
    
pista = Alkalmazott("Pista", 1500)
matyi = Alkalmazott("Matyi", 1800)
ilona = Alkalmazott("Ilona",2500)
robi = Alkalmazott("Robi",1800)
kati = Alkalmazott("Kati",1300)
gyartas = Reszleg("Gyartas")
iroda = Reszleg("Iroda")
kft = Reszleg("Proba kft")
kft.hozzad(gyartas)
kft.hozzad(iroda)
gyartas.hozzad(pista)
gyartas.hozzad(matyi)
gyartas.hozzad(ilona)
gyartas.hozzad(robi)
iroda.hozzad(kati)
print(gyartas.koltseg_szamit())
print(gyartas.letszam_szamit())
print(iroda.koltseg_szamit())
print(iroda.letszam_szamit())
print(kft.koltseg_szamit())
print(kft.letszam_szamit())