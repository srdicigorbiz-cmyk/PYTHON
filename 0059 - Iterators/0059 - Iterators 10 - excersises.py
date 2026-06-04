print("*****EGYSZERŰ SZÁMLÁLÓ*********************")
class EgyszeruSzamlalo:
    def __init__(self):
        self.start = 1
    def __iter__(self):
        return self
    def __next__(self):
        result = self.start
        self.start +=1
        return result
    
szamlalo = EgyszeruSzamlalo()
for i in range(5):
    print(next(szamlalo))

print("*****FORGO BANNER*********************")
class ForgoBanner:
    def __init__(self, lista):
        self.lista = lista
        self.start = 0
        self.end= len(lista)
        self.current = self.start
    def __iter__(self):
        return self
    def __next__(self):
        if self.current < self.end:
            result = self.lista[self.current]
            self.current += 1
            return result
        else:
            self.current=self.start
            return self.__next__()


forgobanner = ForgoBanner(["Akció!", "Új termék!", "Ingyenes szállítás!"])
for i in range(8):
    print(next(forgobanner))

print("*****MUNKABEOSZTAS*********************")
class Munkabeosztas:
    def __init__(self, dolgozok, muszakok):
        self.dolgozok = dolgozok
        self.muszakok = muszakok
        self.muszak_start = 1
        self.muszak_jelen = self.muszak_start
        self.dolgozo_start = 0
        self.dolgozo_jelen = self.dolgozo_start
        self.dolgozo_max = len(dolgozok)
    def __iter__(self):
        return self
    def __next__(self):
        if self.muszak_jelen <= self.muszakok:
            result2 = self.muszak_jelen
            if self.dolgozo_jelen < self.dolgozo_max: 
                result1 = self.dolgozok[self.dolgozo_jelen]
                self.dolgozo_jelen += 1
            else:
                self.dolgozo_jelen = self.dolgozo_start
                result1 = self.dolgozok[self.dolgozo_jelen]
                self.dolgozo_jelen +=1
                
            self.muszak_jelen += 1
            return f"Muszak: {result2}: {result1}"
        else:
            self.muszak_jelen = self.muszak_start
            return self.__next__()
        
        
        

dolgozok = ["Anna", "Béla", "Csaba", "Dóra"]
muszakok = 3
munkabeosztas = Munkabeosztas(dolgozok, muszakok)
for i in range(10):
    print(next(munkabeosztas))
