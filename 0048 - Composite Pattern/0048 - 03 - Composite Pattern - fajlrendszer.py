from abc import ABC, abstractmethod
class RendszerElem(ABC):
    @abstractmethod
    def meret_szamit(self):
        pass
class File(RendszerElem):
    def __init__(self, nev, meret):
        self.nev = nev
        self.meret = meret
    def meret_szamit(self):
        return self.meret
class Mappa(RendszerElem):
    def __init__(self, nev):
        self.nev = nev
        self.elemek = []
    def hozzaad(self, elem):
        self.elemek.append(elem)
    def meret_szamit(self):
        return sum(list(map(lambda x: x.meret_szamit(), self.elemek)))
    
fajl1 = File("egyes", 123)
fajl2 = File("kettes", 321)
mappa = Mappa("mappa")
mappa1 = Mappa("mappa1")
mappa.hozzaad(fajl1)
mappa.hozzaad(fajl2)
mappa.hozzaad(mappa1)
mappa1.hozzaad(fajl1)
print(mappa.meret_szamit())

