class Fizetes:
    def osszeg(self):
        return 10000
class Jutalek:
    def __init__(self, osztaly):
        self.osztaly = osztaly
    def osszeg(self):
        return self.osztaly.osszeg() * 1.05
class Afa:
    def __init__(self, osztaly):
        self.osztaly = osztaly
    def osszeg(self):
        return self.osztaly.osszeg() * 1.27
    
fizetes = Fizetes()
print(fizetes.osszeg())
fizetes = Jutalek(fizetes)
print(fizetes.osszeg())
fizetes=Afa(fizetes)
print(fizetes.osszeg())