# Van: KilometerSzamitas, MerfoldSzamitas, TengerimerfoldSzamitas osztályok
# Mindegyiknek: szamit(tavolsag) metódusa
# Van: Tavolsagmero context osztály
# + set_strategia() metódus
class KilometerSzamitas:
    def szamit (self, tavolsag):
        return f"{tavolsag} km"
    
class MerfoldSzamitas:
    def szamit (self, tavolsag):
        return f"{round(tavolsag * 0.6214, 2)} mérföld"
    
class TengerimerfoldSzamitas:
    def szamit (self, tavolsag):
        return f"{round(tavolsag*0.5399,2)} tengeri mérföld"

class Tavolsagmero:
    def __init__(self, strategia):
        self.strategia = strategia
    def set_strategia(self, strategia):
        self.strategia = strategia
    def szamit(self, tavolsag):
        return self.strategia.szamit(tavolsag)

t = Tavolsagmero(KilometerSzamitas())
print(t.szamit(100))  # "100 km"

t.set_strategia(MerfoldSzamitas())
print(t.szamit(100))  # "62.14 mérföld"

t.set_strategia(TengerimerfoldSzamitas())
print(t.szamit(100))  # "53.99 tengeri mérföld"