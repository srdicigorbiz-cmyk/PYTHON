class Hiroldal:
    _instance=None
    def __new__(cls):
        if cls._instance is None:
            cls._instance=super().__new__(cls)
        return cls._instance
    def __init__(self):
        if not hasattr(self, "feliratkozottak"):
            self.feliratkozottak = []
    def feliratkozas(self, megfigyelo):
        self.feliratkozottak.append(megfigyelo)
    def ertesites(self, hir_szoveg):
        for f in self.feliratkozottak:
             f.frissites(hir_szoveg)
             
class Olvaso:
    def frissites(self, szoveg):
        print(szoveg)

hir = Hiroldal()
olvas1 = Olvaso() # Ez egy igazi objektum, nem csak egy név
olvas2 = Olvaso()

hir.feliratkozas(olvas1) # Az objektumot regisztráljuk
hir.feliratkozas(olvas2)

hir.ertesites("Új árak vannak")