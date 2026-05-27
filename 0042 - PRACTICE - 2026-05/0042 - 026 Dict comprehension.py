class Diak:
    def __init__(self, nev, atlag):
        self.nev = nev
        self.atlag = float(atlag)
class Iskola:
    def __init__(self, diakok_szotara):
        self.diakok_szotara = diakok_szotara
    def osztondijasok(self, hatarertek):
        eredmeny = list(filter(lambda x: x.atlag >= hatarertek, self.diakok_szotara.values()))
        return {x.nev:x.atlag for x in eredmeny}

# Diákok létrehozása
d1 = Diak("Kovács Péter", 4.8)
# Azonosító (ID) alapú szótár
iskola_adatok = {
    "ID001": d1,
    "ID002": Diak("Nagy Anna", 3.9),
    "ID003": Diak("Szabó Gábor", 4.5)
}

iskola = Iskola(iskola_adatok)

# Teszt: Azok a diákok, akiknek az átlaga legalább 4.2
print(iskola.osztondijasok(4.2))
# Elvárt eredmény: {'Kovács Péter': 4.8, 'Szabó Gábor': 4.5}