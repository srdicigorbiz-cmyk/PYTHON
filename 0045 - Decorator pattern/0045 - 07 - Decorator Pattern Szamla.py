class Szamla:
    def __init__(self, ertek):
        self.__osszeg = ertek
    @property
    def ertek(self):
        return self.__osszeg
    @ertek.setter
    def ertek(self, ertek):
        if ertek > 0:
            self.__osszeg = ertek
        else:
            raise ValueError("Az érték nem lehet kisebb mint 0")
    def osszeg (self):
        return self.__osszeg
class Afa:
    def __init__(self, osztaly):
        self.osztaly = osztaly
    def osszeg(self):
        return self.osztaly.osszeg()*1.27
class Kedvezmeny:
    def __init__(self, osztaly):
        self.osztaly = osztaly
    def osszeg(self):
        return self.osztaly.osszeg()*0.90

# TESZT
szamla = Szamla(1000)
szamla = Afa(szamla)
szamla = Kedvezmeny(szamla)
print(szamla.osszeg())
szamla1 = Szamla(6000)
szamla1 = Afa(szamla1)
szamla1 = Kedvezmeny(szamla1)
print(szamla1.osszeg())