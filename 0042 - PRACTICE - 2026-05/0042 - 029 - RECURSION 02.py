""""
Nézzük meg a következő kódot. Ez a függvény összeadja a számokat a megadott számtól 
lefelé 1-ig (például ha a szám 3, akkor $3 + 2 + 1 = 6$)
Tegyük fel, hogy meghívjuk az osszegzes(3)-at.

A gép eljut a return 3 + osszegzes(2) sorhoz. De a 3 + ...-at nem tudja kiszámolni, 
amíg nem tudja, mennyi az osszegzes(2). Úgyhogy a 3 + műveletet felfüggeszti 
(félbehagyja), és továbblép befelé.

A legbelső szinten megkaptuk az 1-et, a gép visszalépett egy szintet a fagyasztott 
számlákhoz, ahol a 2 + ... várakozott, így a legelső valódi számítás a $2 + 1 = 3$ lett.
Ezután ezt a 3-at viszi tovább felfelé a legkülső szintre, ahol a 3 + ... várta, így az 
utolsó számítás a $3 + 3 = 6$ lesz.
"""

def osszegzes(szam):
    if szam == 1:
        return 1  # Az 1-nél megállunk, tudjuk az eredményt
        
    # Itt a trükk: megvárjuk a kisebb szám összegét, 
    # és ha megvan, hozzáadjuk a jelenlegi számot
    return szam + osszegzes(szam - 1)

print(osszegzes(5))