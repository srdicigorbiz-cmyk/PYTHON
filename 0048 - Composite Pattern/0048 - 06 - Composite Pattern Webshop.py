from abc import ABC, abstractmethod
class KosarElem(ABC):
    @abstractmethod
    def ar_szamit(self):
        pass
    @abstractmethod
    def kedvezmeny_beallit(self, szazalek):
        pass

class Termek(KosarElem):
    def __init__(self, nev, ar):
        self.nev = nev
        self.ar = ar
        self.kedvezmeny = 1
    def ar_szamit(self):
        return self.ar*self.kedvezmeny
    def kedvezmeny_beallit(self, szazalek):
        self.kedvezmeny = (100-szazalek)/100
    

class Csomag(KosarElem):
    def __init__(self, nev):
        self.nev = nev
        self.egysegek = []
        self.kedvezmeny = 1
    def hozzaad(self, egyseg):
        self.egysegek.append(egyseg)
    def ar_szamit(self):
        return sum(list(map(lambda x: x.ar_szamit(), self.egysegek)))
    def kedvezmeny_beallit(self, szazalek):
        for egyseg in self.egysegek:
            egyseg.kedvezmeny_beallit(szazalek)
    


# ==============================================================================
# TESZTSZVIT ÉS MINTAADATOK (Másold ki a kódod végére a teszteléshez)
# ==============================================================================
try:
    # Egyszerű termékek
    laptop = Termek("Laptop", 400000)
    eger = Termek("Egér", 15000)
    billentyuzet = Termek("Billentyűzet", 25000)
    csoki = Termek("Prémium Csokoládé", 3000)
    bor = Termek("Minőségi Bor", 8000)

    # Összetett csomagok (Composite)
    # 1. Szint: Egy irodai kezdőcsomag
    iroda_csomag = Csomag("Gamer Kezdőszett")
    iroda_csomag.hozzaad(eger)
    iroda_csomag.hozzaad(billentyuzet)

    # 2. Szint: Egy exkluzív ajándékkosár, ami egy másik csomagot is tartalmaz
    ajandek_kosar = Csomag("Szülinapi VIP Kosár")
    ajandek_kosar.hozzaad(csoki)
    ajandek_kosar.hozzaad(bor)
    ajandek_kosar.hozzaad(iroda_csomag)  # Beágyazott kompozit struktúra

    # Fő kosár (A legfelső szintű kompozit)
    bevasarlo_kosar = Csomag("Fő Vásárlói Kosár")
    bevasarlo_kosar.hozzaad(laptop)        # Sima termék a kosárban
    bevasarlo_kosar.hozzaad(ajandek_kosar) # Összetett csomag a kosárban

    # --- TESZTELÉS ---
    print("--- Alapárak ellenőrzése ---")
    print(f"Iroda csomag alapára (15000 + 25000 = 40000): {iroda_csomag.ar_szamit()} Ft")
    print(f"Teljes kosár alapára (400000 + 3000 + 8000 + 40000 = 451000): {bevasarlo_kosar.ar_szamit()} Ft")

    print("\n--- Kedvezmények érvényesítése (10% mindenre) ---")
    bevasarlo_kosar.kedvezmeny_beallit(10)
    print(f"Iroda csomag akciós ára (40000 * 0.9 = 36000): {iroda_csomag.ar_szamit()} Ft")
    print(f"Teljes kosár akciós ára (451000 * 0.9 = 405900): {bevasarlo_kosar.ar_szamit()} Ft")

except NameError as e:
    print(f"Sikeres teszteléshez még hiányzik egy osztály vagy metódus: {e}")