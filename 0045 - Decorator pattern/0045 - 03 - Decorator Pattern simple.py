class Fizetes:
    def fizetes(self):
        return 1000

class PontossagiBonusz:
    def __init__(self, osztaly):
        self.osztaly = osztaly
    def fizetes(self):
        return self.osztaly.fizetes() + 200

fizetes = Fizetes()
p_bonusz = PontossagiBonusz(fizetes)
print(fizetes.fizetes())
print(p_bonusz.fizetes())