from abc import ABC, abstractmethod

class ItalKeszito(ABC):
    def vizet_elokeszit(self):
        return"Elokesziti a vizet"
    def vizet_forral(self):
        return"Vizet forral"
    @abstractmethod
    def ital_keszites(self, hozzavalo):
        pass
    def keszit(self, hozzavalo):
        print(self.vizet_elokeszit())
        print(self.vizet_forral())
        return(self.ital_keszites(hozzavalo))

class KaveKeszito(ItalKeszito):
    def ital_keszites(self, hozzavalo):
        return "A vízbe " + hozzavalo + " kerul"
class TeaKeszito(ItalKeszito):
    def ital_keszites(self, hozzavalo):
        return "A vizbe " + hozzavalo + " kerül"
class JegesTea(ItalKeszito):
    def ital_keszites(self, hozzavalo):
        return "A vizbe " + hozzavalo + " kerül"
class Smoothie(ItalKeszito):
    def vizet_elokeszit(self):
        return "Előkészíti a gyümölcsöt."
    def ital_keszites(self, hozzavalo):
        return "A vizbe " + hozzavalo + " kerül"

kave=KaveKeszito()
tea=TeaKeszito()
jegestea=JegesTea()
smoothie=Smoothie()
print(kave.keszit("kave"))
print(tea.keszit("tea"))
print(jegestea.keszit("citrom"))
print(smoothie.keszit("banan"))
