from abc import ABC, abstractmethod
class OkosElem(ABC):
    @abstractmethod
    def fogyasztas_szamit(self):
        pass
    @abstractmethod
    def minden_lekapcsol(self):
        pass

class Eszkoz(OkosElem):
    def __init__(self, nev, fogyasztas):
        self.be_van_kapcsolva = True
        self.nev = nev
        self.fogyasztas = fogyasztas
    def fogyasztas_szamit(self):
        if self.be_van_kapcsolva is True:
            return self.fogyasztas
        else:
            return 0
    def minden_lekapcsol(self):
        self.be_van_kapcsolva = False
class Helyseg(OkosElem):
    def __init__(self, nev):
        self.nev = nev
        self.egysegek = []
    def hozzaad(self, egyseg):
        self.egysegek.append(egyseg)
    def fogyasztas_szamit(self):
        return sum(list(map(lambda x: x.fogyasztas_szamit(), self.egysegek)))

    def minden_lekapcsol(self):
        for egyseg in self.egysegek:
            egyseg.minden_lekapcsol()
    
# TEST
tv = Eszkoz("tv", 150)
lampa = Eszkoz("lampa", 70)
huto = Eszkoz("huto", 1500)
bojler = Eszkoz("bojler", 2500)
pc = Eszkoz("pc", 200)
suto = Eszkoz("Suto", 2150)
telefon = Eszkoz("Telefon", 50)
#helysegek
haz = Helyseg("Haz")
nappali = Helyseg("Nappali")
haloszoba = Helyseg("Haloszoba")
konyha = Helyseg("konyha")
furdo = Helyseg("Furdoszoba")

#konfiguralas
haz.hozzaad(nappali)
haz.hozzaad(haloszoba)
haz.hozzaad(konyha)
haz.hozzaad(furdo)
nappali.hozzaad(tv)
nappali.hozzaad(telefon)
nappali.hozzaad(lampa)
nappali.hozzaad(pc)
haloszoba.hozzaad(lampa)
haloszoba.hozzaad(telefon)
konyha.hozzaad(huto)
konyha.hozzaad(lampa)
konyha.hozzaad(suto)
konyha.hozzaad(bojler)
furdo.hozzaad(lampa)
furdo.hozzaad(bojler)
#eredmenyek
print(nappali.fogyasztas_szamit())
print(haloszoba.fogyasztas_szamit())
print(konyha.fogyasztas_szamit())
print(furdo.fogyasztas_szamit())
print(haz.fogyasztas_szamit())
#kikapcsol
konyha.minden_lekapcsol()
print(haz.fogyasztas_szamit())