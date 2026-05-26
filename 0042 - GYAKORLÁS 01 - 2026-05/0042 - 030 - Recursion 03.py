"""
A rekurzió listákkal (A hidat építjük a fákhoz)
Képzelj el egy olyan listát, amiben számok vannak, de néhány elem maga is egy lista! Például:
lista = [1, [2, 3], 4]
Ha meg akarjuk számolni, hány szám van ebben a szerkezetben összesen, a sima for ciklus 
beletörne a bicskája, mert a [2, 3] elemnél azt mondaná, hogy az csak 1 darab elem (egy lista), 
és nem látna bele a belsejébe.
Itt jön a rekurzió! Írunk egy függvényt, ami végigmegy a lista elemein:
Bázis feltétel (ha sima szám): Ha az elem egy sima szám, akkor az 1 darab szám.
Rekurzív lépés (ha beágyazott lista): Ha az elem maga is egy lista, akkor meghívjuk ugyanezt a függvényt erre a belső listára, és megvárjuk, hogy az hányat számol össze benne!
Nézzük meg ezt kódban:
Ha ezt lefuttatjuk a [1, [2, 3], 4] listára, a ciklus elindul:elem = 1: Sima szám -> osszesen = 1.elem = [2, 3]: 
Hoppá, ez egy lista! A gép felfüggeszti a külső listát, és elindít egy új szamol_elemeket függvényt 
a [2, 3]-ra.Az a belső függvény összeszámolja a 2-est és a 3-ast, majd visszadobja, 
hogy: 2.A külső függvény felébred, és hozzáadja a kapott eredményt: 
osszesen = $1 + 2 = 3$.elem = 4: Sima szám -> osszesen = $3 + 1 = 4$.
"""

def szamol_elemeket(lista):
    osszesen = 0
    
    for elem in lista:
        if isinstance(elem, list):
            # REKURZÍV LÉPÉS: ha lista, újra meghívjuk magunkat a belső listára
            osszesen += szamol_elemeket(elem)
        else:
            # BÁZIS FELTÉTEL: ha sima szám, az 1 darab elem
            osszesen += 1
            
    return osszesen

print(szamol_elemeket([1, [2, 3], 4]))