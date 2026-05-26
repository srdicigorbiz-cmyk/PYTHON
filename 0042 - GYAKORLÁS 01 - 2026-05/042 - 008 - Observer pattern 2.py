# Írj egy Termek osztályt (Subject) és Vasarlo osztályt (Observer)
# - Termek: __init__(nev, ar), feliratkozas(), leiratkozas(), ar_valtozas(uj_ar)
#   ar_valtozas: frissíti az árat ÉS értesít
# - Vasarlo: __init__(nev), ertesit(termek_nev, uj_ar)
#   kiírja: "{nev} értesítve: {termek_nev} új ára: {uj_ar} Ft"
class Termek:
    def __init__(self, nev, ar):
        self.nev = nev
        self.ar = ar
        self.feliratkozok = []
    def feliratkozas(self, feliratkozo):
        self.feliratkozok.append(feliratkozo)
    def leiratkozas(self, leiratkozo):
        self.feliratkozok.remove(leiratkozo)
    def ar_valtozas(self, uj_ar):
        self.ar = uj_ar
        for feliratkozo in  self.feliratkozok:
            feliratkozo.ertesit(self.nev, uj_ar)


class Vasarlo:
    def __init__(self, nev):
        self.nev = nev
    def ertesit(self, termek_nev, uj_ar):
        print(f"{self.nev} értesítve: {termek_nev} új ára: {uj_ar} Ft")



t = Termek("Laptop", 500000)
v1 = Vasarlo("Anna")
v2 = Vasarlo("Béla")

t.feliratkozas(v1)
t.feliratkozas(v2)
print()
t.ar_valtozas(450000)

t.leiratkozas(v1)
t.ar_valtozas(400000)  # csak Béla kapja