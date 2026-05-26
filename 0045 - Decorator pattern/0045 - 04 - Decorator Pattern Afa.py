class Szamla:
    def osszeg(self):
        return 5000
class Afa:
    def __init__(self, osztaly):
        self.osztaly = osztaly
    def osszeg(self):
        return self.osztaly.osszeg()*1.27

szamla=Szamla()
szamla=Afa(szamla)
print(szamla.osszeg())
