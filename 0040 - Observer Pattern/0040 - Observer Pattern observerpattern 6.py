class Vilagitorony:
    def __init__(self):
        self.feliratkozok = []
    def feliratkozas(self, feliratkozo):
        self.feliratkozok.append(feliratkozo)
    def leiratkozas(self, leiratkozo):
        self.feliratkozok.remove(leiratkozo)
    def ertesit(self, uzenet):
        for feliratkozo in self.feliratkozok:
            feliratkozo.ertesit(uzenet)

class Hajo:
    def __init__(self, nev):
        self.nev = nev
    def ertesit(self, uzenet):
        print(uzenet)
    
hajo1 = Hajo("hajo1")
hajo2 = Hajo("hajo2")
vilagitorony = Vilagitorony()
vilagitorony.feliratkozas(hajo1)
vilagitorony.feliratkozas(hajo2)
vilagitorony.ertesit("Ertesites")
vilagitorony.leiratkozas(hajo2)
vilagitorony.ertesit("Ertesites2")