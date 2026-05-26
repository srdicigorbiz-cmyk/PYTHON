class OldSystem:
    def get_nev(self, nev):
        return nev

class NewSystem:
    def nev(self, nev):
        return nev

class Adapter:
    def __init__(self, old_sys):
        self.old_sys = old_sys
    def nev(self, nev):
        return self.old_sys.get_nev(nev)

def kiir(rendszer):
    print(rendszer.nev("Mark"))

old = OldSystem()
adapter = Adapter(old)
new = NewSystem()

print(adapter.nev("Mark"))
kiir(adapter)

