# Van: EuroFizetes, DinarFizetes osztályok
# Mindegyiknek: fizet(osszeg) metódusa
# Van: Penztar context osztály
class EuroFizetes:
    def fizet(self, osszeg):
        return f"Fizetve: {osszeg} EUR"       
        
class DinarFizetes:
    def fizet(self, osszeg):
        return f"Fizetve: {osszeg} RSD"       
    
class Penztar:
    def __init__(self, strategia):
        self.strategia = strategia
    def fizet(self, osszeg):
        return self.strategia.fizet(osszeg)



p = Penztar(EuroFizetes())
print(p.fizet(100))  # "Fizetve: 100 EUR"

p.strategia = DinarFizetes()
print(p.fizet(100))  # "Fizetve: 100 RSD"