class Auto:
    def __init__(self, marka, ev):
        self.marka = marka
        self.ev = ev
        self.km = 0
    def __str__(self):
        return (f"Marka: {self.marka}, Év: {self.ev}, Km: {self.km}")
    
    @property
    def km(self):
        return self._km
    
    @km.setter
    def km(self, value):
        if value >= 0:
            self._km = value
            
        

# Teszteld:
a = Auto("Toyota", 2020)
a.km = 15000
print(a)
print(a.km)
a.km = -100  # nem változhat!
print(a.km)  # még mindig 15000