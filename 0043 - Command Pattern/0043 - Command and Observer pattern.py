from abc import ABC, abstractmethod

# --- 1. AZ OBSERVER RÉSZ (Aki figyel) ---
class MegfigyeloBase(ABC):
    @abstractmethod
    def frissit(self, uzenet):
        pass

class BankiNaplo(MegfigyeloBase):
    def frissit(self, uzenet):
        print(f"[NAPLÓ]: {uzenet}")

# --- 2. A RECEIVER (Aki ténylegesen dolgozik) ---
class Bankszamla:
    def __init__(self, egyenleg):
        self.egyenleg = egyenleg
        self.megfigyelok = []

    def hozzaad_megfigyelo(self, m):
        self.megfigyelok.append(m)

    def ertesit(self, uzenet):
        for m in self.megfigyelok:
            m.frissit(uzenet)

    def penz_levonas(self, osszeg):
        if osszeg > self.egyenleg:
            raise ValueError(f"Sikertelen levonás: Nincs elég fedezet! (Egyenleg: {self.egyenleg} Ft)")
        
        self.egyenleg -= osszeg
        self.ertesit(f"Levonás: {osszeg} Ft. Új egyenleg: {self.egyenleg} Ft.")

    def penz_hozzaadas(self, osszeg):
        self.egyenleg += osszeg
        self.ertesit(f"Befizetés: {osszeg} Ft. Új egyenleg: {self.egyenleg} Ft.")

# --- 3. A COMMAND RÉSZ (A művelet objektum) ---
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass
    @abstractmethod
    def undo(self):
        pass

class UtalasCommand(Command):
    def __init__(self, szamla, osszeg):
        self.szamla = szamla
        self.osszeg = osszeg

    
    def execute(self):
        try:
            self.szamla.penz_levonas(self.osszeg)
            
        except ValueError as e:
            print(f"Hiba törént {e}")
    

    def undo(self):
        self.szamla.penz_hozzaadas(self.osszeg)

class HitelCommand(Command):
    def __init__(self, szamla, osszeg):
        self.szamla = szamla
        self.osszeg = osszeg

    def execute(self):
        self.szamla.penz_hozzaadas(self.osszeg) # Ide jön a kódod: add hozzá az összeget a számlához!
        

    def undo(self):
        self.szamla.penz_levonas(self.osszeg) # Ide jön a kódod: vond le az összeget!
        

# --- Tesztelés ---
szamlam = Bankszamla(5000)
szamlam.hozzaad_megfigyelo(BankiNaplo())

hitel = HitelCommand(szamlam, 10000)

print("--- Hitel folyósítása ---")
# Itt hívd meg a hitel parancs végrehajtását!
hitel.execute()
print("--- Hitel visszavonása ---")
# Itt hívd meg a visszavonást!
hitel.undo()

# Parancs létrehozása és végrehajtása
utalas = UtalasCommand(szamlam, 525200)
utalas.execute() # [NAPLÓ]: Levonás: 200 Ft...

# Visszavonás
utalas.undo()    # [NAPLÓ]: Befizetés: 200 Ft...