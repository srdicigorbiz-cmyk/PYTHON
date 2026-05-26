class AdatFeldolgozo:
    def szurt_felhasznalok(self, adat_lista):
        try:
            return list(filter(lambda x: x[2] is True , adat_lista))
        except IndexError:
            print("Hibás adatformátum!")
            return []
        

feldolgozo = AdatFeldolgozo()

# 1. Teszt: Jó adatok
jok = [("Anna", 25, True), ("Béla", 40, False), ("Cili", 30, True)]
print(feldolgozo.szurt_felhasznalok(jok))
# Elvárt: [('Anna', 25, True), ('Cili', 30, True)]

# 2. Teszt: Hibás adatok (Béla tuple-je hibás, hiányzik a True/False)
hibasok = [("Anna", 25, True), ("Béla", 40)]
print(feldolgozo.szurt_felhasznalok(hibasok))
# Elvárt: Üzenet: "Hibás adatformátum!" és kimenet: []