class RegiFizetes:
    def payment_execute(self, osszeg):
        return f"Fizetve: {osszeg} Ft"

class Adapter:
    def __init__(self, regi_rendszer):
        self.regi_rendszer = regi_rendszer
    def fizet(self, osszeg):
        return self.regi_rendszer.payment_execute(osszeg)
    
def checkout(rendszer, osszeg):
    return rendszer.fizet(osszeg)

regi = RegiFizetes()
adapter = Adapter(regi)
print(checkout(adapter, 300))