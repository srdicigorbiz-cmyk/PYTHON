# Írj egy Szamla osztályt
# - __init__: tulajdonos, _egyenleg=0 (privát)
# - @property + setter: egyenleg – csak >= 0 fogadható el
# - befizet(osszeg): növeli az egyenleget
# - kivesz(osszeg): csökkenti – de csak ha van elég fedezet, különben print: "Nincs fedezet!"
# - __str__: "Tulajdonos: X, Egyenleg: Y"
class Szamla:
    def __init__(self, tulajdonos):
        self.tulajdonos = tulajdonos
        self.egyenleg = 0
    @property
    def egyenleg(self):
        return self._egyenleg
    @egyenleg.setter
    def egyenleg(self, ertek):
        if ertek >= 0:
            self._egyenleg = ertek
    def __str__(self):
        return f"Tulajdonos: {self.tulajdonos}, Egyenleg: {self.egyenleg}"
    def befizet(self, osszeg):
        self.egyenleg += osszeg
    def kivesz(self, osszeg):
        if osszeg > self.egyenleg:
            print("Nincs fedezet!")
        else:
            self.egyenleg -= osszeg


sz = Szamla("Anna")
sz.befizet(1000)
sz.befizet(500)
print(sz)
sz.kivesz(200)
print(sz)
sz.kivesz(2000)  # Nincs fedezet!
print(sz)