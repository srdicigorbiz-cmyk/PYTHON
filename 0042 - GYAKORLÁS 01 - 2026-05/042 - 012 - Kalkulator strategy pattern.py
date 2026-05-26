# Van: KilometerSzamitas, MerfoldSzamitas osztályok
# Mindegyiknek: szamit(ertek) metódusa
# Van: Kalkulator context osztály + set_strategia() metódus
class KilometerSzamitas:
    def szamit(self, ertek):
        return f"{ertek*1} km"
class MerfoldSzamitas:
    def szamit(self, ertek):
        return f"{round(ertek*0.6214, 2)} mérföld"

class Kalkulator:
    def __init__(self, strategia):
        self.strategia = strategia

    def set_strategia(self, strategia):
        self.strategia = strategia

    def szamit(self, ertek):
        return self.strategia.szamit(ertek)


k = Kalkulator(KilometerSzamitas())
print(k.szamit(100))  # "100 km"

k.set_strategia(MerfoldSzamitas())
print(k.szamit(100))  # "62.14 mérföld"