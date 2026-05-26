class NovekvoCsoportositas:
    def rendez(self, adatok):
        return sorted(adatok)
class CsokkenoCsoportositas:
    def rendez(self, adatok):
        return sorted(adatok, reverse = True)

class Rendezo:
    def __init__(self, strategia):
        self.strategia = strategia
    
    def rendez(self, adatok):
        return self.strategia.rendez(adatok)

szamok = [3, 1, 4, 1, 5, 9, 2, 6]

rendezo = Rendezo(NovekvoCsoportositas())
print(rendezo.rendez(szamok))

rendezo.strategia = CsokkenoCsoportositas()
print(rendezo.rendez(szamok))