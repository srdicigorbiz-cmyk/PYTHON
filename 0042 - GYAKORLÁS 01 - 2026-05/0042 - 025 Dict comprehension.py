class Termek:
    def __init__(self, nev, ar, kategoria):
        self.nev = nev
        self.ar = ar
        self.kategoria = kategoria

class Raktar:
    def __init__(self, termek_lista):
        self.termek_lista = termek_lista
        
    def draga_termekek_kategoriai(self):
        # Ide jön a szűrés és a szótárrá alakítás
        # Egy filter és egy lambda segítségével kiszűri azokat a termékeket, amelyeknek az ára szigorúan nagyobb mint 1500.
        #A megszűrt termékekből építsen és adjon vissza egy szótárt (dict), ahol a kulcs a termék neve, az érték pedig a termék kategóriája.
        draga_termekek_lista = list(filter(lambda x: x.ar > 1500, self.termek_lista))
        return {x.nev:x.kategoria for x in draga_termekek_lista}
    


t1 = Termek("Cipő", 2000, "Ruházat")
t2 = Termek("Zokni", 500, "Ruházat")
t3 = Termek("Ing", 1800, "Ruházat")

raktar = Raktar([t1, t2, t3])
print(raktar.draga_termekek_kategoriai())
# Elvárt eredmény: {'Cipő': 'Ruházat', 'Ing': 'Ruházat'}