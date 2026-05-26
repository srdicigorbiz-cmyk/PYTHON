class RegiEuro:
    def get_euro(self, osszeg):
        return f"{osszeg} EUR"

class RegiDollar:
    def get_dollar(self, osszeg):
        return f"{osszeg} USD"
    
class AdapterEuro:
    def __init__(self, oldsys):
        self.oldsys = oldsys
    def fizet(self, osszeg):
        return self.oldsys.get_euro(osszeg)

class AdapterDollar:
    def __init__(self, oldsys):
        self.oldsys = oldsys
    def fizet(self,osszeg):
        return self.oldsys.get_dollar(osszeg)

def checkout(rendszer, osszeg):
    return rendszer.fizet(osszeg)

regieuro = RegiEuro()
regidollar = RegiDollar()
euroadapter = AdapterEuro(regieuro)
dollaradapter = AdapterDollar(regidollar)

print(checkout(euroadapter,300))
print(checkout(dollaradapter, 300))