from abc import ABC, abstractmethod
class SzervezetiEgyseg(ABC):
    @abstractmethod
    def ber_szamit(self):
        pass
    @abstractmethod
    def bonusz_oszt(self, osszeg):
        pass

class Alkalmazott(SzervezetiEgyseg):
    def __init__(self, nev, fizetes):
        self.nev = nev
        self.fizetes = fizetes
    def ber_szamit(self):
        return self.fizetes
    def bonusz_oszt(self, osszeg):
        self.fizetes += osszeg
    
        
class Reszleg(SzervezetiEgyseg):
    def __init__(self, nev):
        self.nev=nev
        self.egysegek =[]
    def hozzaad(self, egyseg):
        self.egysegek.append(egyseg)
    def ber_szamit(self):
        return sum(list(map(lambda x: x.ber_szamit(), self.egysegek)))
    def bonusz_oszt(self, osszeg):
        for egyseg in self.egysegek:
            egyseg.bonusz_oszt(osszeg)
    


# ==============================================================================
# TESZTSZVIT ÉS MINTAADATOK (Másold ki a kódod végére a teszteléshez)
# ==============================================================================
try:
    # 1. Alap alkalmazottak (Fejlesztők a Tech részlegen)
    kovacs = Alkalmazott("Kovács János", 500000)
    szabo = Alkalmazott("Szabó Mária", 600000)
    
    # Tech részleg létrehozása és tagok hozzáadása
    tech_reszleg = Reszleg("Fejlesztés")
    tech_reszleg.hozzaad(kovacs)
    tech_reszleg.hozzaad(szabo)
    
    # 2. Marketingesek és a Marketing részleg
    nagy = Alkalmazott("Nagy Péter", 450000)
    marketing_reszleg = Reszleg("Marketing")
    marketing_reszleg.hozzaad(nagy)
    
    # 3. Fő Cégstruktúra (A teljes vállalat)
    vallalat = Reszleg("Global Corp")
    vallalat.hozzaad(tech_reszleg)       # Részleg a részlegben
    vallalat.hozzaad(marketing_reszleg)  # Részleg a részlegben

    # --- TESZTELÉS: 1. Fázis (Alapberek) ---
    print("--- Alapberek ellenőrzése ---")
    print(f"Tech részleg összköltsége (500000 + 600000 = 1100000): {tech_reszleg.ber_szamit()} Ft")
    print(f"Teljes vállalat összköltsége (1100000 + 450000 = 1550000): {vallalat.ber_szamit()} Ft")

    # --- TESZTELÉS: 2. Fázis (Rendkívüli bónusz) ---
    print("\n--- Rendkívüli bónusz kiosztása a Tech részlegnek (50 000 Ft mindenkinek) ---")
    tech_reszleg.bonusz_oszt(50000)
    # Kovács: 550e, Szabó: 650e -> Tech: 1200e. Nagy Péter nem kapott!
    print(f"Tech részleg új költsége (1200000): {tech_reszleg.ber_szamit()} Ft")
    print(f"Teljes vállalat új költsége (1200000 + 450000 = 1650000): {vallalat.ber_szamit()} Ft")

except NameError as e:
    print(f"Sikeres teszteléshez még hiányzik egy osztály vagy metódus: {e}")