# Van: NovekvőRendezes, CsökkőRendezes, HosszSzerintiRendezes osztályok
# Mindegyiknek: rendez(elemek) metódusa – elemek egy lista
# Van: Rendezo context osztály + set_strategia() metódus
class NovekvőRendezes:
    def rendez(self, elemek):
        return sorted(elemek)
class CsökkőRendezes:
    def rendez(self, elemek):
        return sorted(elemek, reverse=True)
class HosszSzerintiRendezes:
    def rendez(self, elemek):
        return sorted(elemek, key= lambda x: len(x))
class Rendezo:
    def __init__(self, strategia):
        self.strategia = strategia
    def set_strategia(self, strategia):
        self.strategia = strategia
    def rendez(self, elemek):
        return self.strategia.rendez(elemek)


r = Rendezo(NovekvőRendezes())
print(r.rendez([3, 1, 4, 1, 5]))  # [1, 1, 3, 4, 5]

r.set_strategia(CsökkőRendezes())
print(r.rendez([3, 1, 4, 1, 5]))  # [5, 4, 3, 1, 1]

r.set_strategia(HosszSzerintiRendezes())
print(r.rendez(["alma", "kiwi", "ananász", "ék"]))  # ["ék", "alma", "kiwi", "ananász"]