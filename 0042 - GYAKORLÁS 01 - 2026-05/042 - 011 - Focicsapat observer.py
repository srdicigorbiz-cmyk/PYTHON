# Írj egy Focicsapat osztályt (Subject) és Szurkoló osztályt (Observer)
# - Focicsapat: __init__(nev), feliratkozas(), leiratkozas(), 
#               gol(jatekos_nev) – értesít ÉS tárolja a gólokat listában
# - Szurkolo: __init__(nev), ertesit(csapat, jatekos) 
#   kiírja: "{nev} üvölt: {csapat} - {jatekos} gólt lőtt!"
# - Focicsapat: gol_lista() – visszaadja ki lőtte a legtöbb gólt
class Focicsapat:
    def __init__(self,nev):
        self.nev = nev
        self.feliratkozok = []
        self.golok_listaja = dict()
    def feliratkozas(self, feliratkozo):
        self.feliratkozok.append(feliratkozo)
        
    def leiratkozas(self, leiratkozo):
        self.feliratkozok.remove(leiratkozo)
        
    def gol(self, jatekos_nev):
        for feliratkozo in self.feliratkozok:
            feliratkozo.ertesit(self.nev, jatekos_nev)
        if jatekos_nev not in self.golok_listaja:
            self.golok_listaja[jatekos_nev]= 1
        else:
            self.golok_listaja[jatekos_nev] += 1
    def gol_lista(self):
        return f"A legtöbb gólt: {max(self.golok_listaja.items(), key=lambda x: x[1])[0]} lőtte."

class Szurkolo:
    def __init__(self,nev):
        self.nev = nev
        
    def ertesit(self, csapat, jatekos):
        print(f"{self.nev} üvölt: {csapat} - {jatekos} gólt lőtt!")


f = Focicsapat("Fradi")
s1 = Szurkolo("Pista")
s2 = Szurkolo("Jóska")

f.feliratkozas(s1)
f.feliratkozas(s2)
f.gol("Priskin")
f.gol("Böde")
f.gol("Priskin")
print(f.gol_lista())  # Priskin: 2, Böde: 1