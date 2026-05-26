class Lampa:
    def felkapcsol(self):
        print("Lámpa felkapcsol.")
    def lekapcsol(self):
        print("Lámpa lekapcsol.")
class LampaFelCommand:
    def __init__(self, lampa):
        self.lampa = lampa
    def execute(self):
        self.lampa.felkapcsol()
class LampaLeCommand:
    def __init__(self, lampa):
        self.lampa = lampa
    def execute(self):
        self.lampa.lekapcsol()

class Taviranyito:
    def __init__(self):
        self.parancsok = {}
    def parancs_regisztral(self, gomb_neve, command_objektum):
        self.parancsok[gomb_neve]=command_objektum
    def gomb_megnyom(self, gomb_neve):
        parancs = self.parancsok.get(gomb_neve)
        if parancs:
            parancs.execute()
        else:
            raise ValueError("Ilyen gomb nincs.")







# Eszköz és parancsok létrehozása
nappali_lampa = Lampa()
fel_parancs = LampaFelCommand(nappali_lampa)
le_parancs = LampaLeCommand(nappali_lampa)

# Vezérlő konfigurálása szótárral
taviranyito = Taviranyito()
taviranyito.parancs_regisztral("A", fel_parancs)
taviranyito.parancs_regisztral("B", le_parancs)

# Tesztelés
taviranyito.gomb_megnyom("A")  # Elvárt: A lámpa felkapcsolódott.
taviranyito.gomb_megnyom("B")  # Elvárt: A lámpa lekapcsolódott.
taviranyito.gomb_megnyom("C")