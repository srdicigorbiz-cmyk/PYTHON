# Van: ParosszamSzuro, NagyobbMintOtSzuro osztályok
# Mindegyiknek: szur(adatok) metódusa
# Van: Szuro context osztály - tarolja a strategiat, meghivja
class ParosszamSzuro:
    def szur(self, adat):
        return list(filter(lambda a: a%2==0, adat)) 
                
class NagyobbMintOtSzuro:
    def szur(self, adat):
        return list(filter(lambda x: x>5, adat))
    
class Szuro:
    def __init__(self,strategia):
        self.strategia = strategia
    
    def szur(self, adat):
        return self.strategia.szur(adat)

szamok = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

szuro = Szuro(ParosszamSzuro())
print(szuro.szur(szamok))  # [2, 4, 6, 8, 10]

szuro.strategia = NagyobbMintOtSzuro()
print(szuro.szur(szamok))  # [6, 7, 8, 9, 10]