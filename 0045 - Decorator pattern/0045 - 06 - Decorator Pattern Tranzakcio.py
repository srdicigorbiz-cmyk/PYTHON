class Tranzakcio:
    def __init__(self, ertek):
        self.__ertek = ertek
    @property
    def ertek(self):
        return self.__ertek
    @ertek.setter
    def ertek(self, ertek):
        self.__ertek = ertek
        
    def osszeg(self):
        return self.__ertek

    def leiras(self):
        return f"Ez egy tranzakcio {self.__ertek} ft"

class Afa:
    def __init__(self, osztaly):
        self.osztaly = osztaly
    def osszeg(self):
        return self.osztaly.osszeg() * 1.27
    def leiras(self):
        return self.osztaly.leiras()
        
class Leiras:
    def __init__(self, osztaly):
        self.osztaly = osztaly
    
    def leiras(self):
        return self.osztaly.leiras() + ". Ami ki lett fizetve."
    

tranzakciok = [Tranzakcio(1000), Tranzakcio(6000), Tranzakcio(3000)]


tranzakcio = Tranzakcio(1000)
print(tranzakcio.osszeg())
print(tranzakcio.leiras())
tranzakcio = Afa(tranzakcio)
print(tranzakcio.osszeg())
tranzakcio = Leiras(tranzakcio)
print(tranzakcio.leiras())