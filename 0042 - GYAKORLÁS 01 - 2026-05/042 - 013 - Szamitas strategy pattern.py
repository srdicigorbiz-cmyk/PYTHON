# Van: OsszegSzamitas, AtlagSzamitas, MaxSzamitas osztályok
# Mindegyiknek: szamit(szamok) metódusa – szamok egy lista
# Van: Statisztika context osztály + set_strategia() metódus
class OsszegSzamitas:
    def szamit(self, szamok):
        return f"Összeg: {sum(szamok)}"

class AtlagSzamitas:
    def szamit(self,szamok):
        return f"Átlag: {sum(szamok)/len(szamok)}"

class MaxSzamitas:
    def szamit(self,szamok):
        return f"Maximum: {max(szamok)}"

class Statisztika:
    def __init__(self, strategia):
        self. strategia = strategia
    def set_strategia(self, strategia):
        self.strategia = strategia
    def szamit(self, szamok):
        return self.strategia.szamit(szamok)
    

s = Statisztika(OsszegSzamitas())
print(s.szamit([1, 2, 3, 4, 5]))  # "Összeg: 15"

s.set_strategia(AtlagSzamitas())
print(s.szamit([1, 2, 3, 4, 5]))  # "Átlag: 3.0"

s.set_strategia(MaxSzamitas())
print(s.szamit([1, 2, 3, 4, 5]))  # "Maximum: 5"