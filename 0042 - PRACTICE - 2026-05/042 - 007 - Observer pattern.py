# Írj egy Idojaras osztályt (Subject) és Allomas osztályt (Observer)
# - Idojaras: __init__(varos), feliratkozas(), leiratkozas(), ertesit(homerseklet)
# - Allomas: __init__(nev), frissit(homerseklet) – kiírja: "{nev} mér: {homerseklet}°C"
class Idojaras:
    def __init__(self, varos):
        self.varos = varos
        self.feliratkozok = []
    def feliratkozas(self, feliratkozo):
        self.feliratkozok.append(feliratkozo)
    def leiratkozas(self, leiratkozo):
        self.feliratkozok.remove(leiratkozo)
    def ertesit(self, homerseklet):
        for feliratkozo in self.feliratkozok:
            feliratkozo.frissit(homerseklet)

class Allomas:
    def __init__(self, nev):
        self.nev=nev
    def frissit(self, homerseklet):
        print(f"{self.nev} mér: {homerseklet}°C")


i = Idojaras("Budapest")
a1 = Allomas("Keleti")
a2 = Allomas("Déli")

i.feliratkozas(a1)
i.feliratkozas(a2)
i.ertesit(25)

i.leiratkozas(a1)
i.ertesit(30)  # csak a2 kapja