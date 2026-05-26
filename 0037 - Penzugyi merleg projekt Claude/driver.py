from tranzakciok import Tranzakcio
from tranzakciok import Penztar
from tranzakciok import Mutatok
from tranzakciok import Fiok
from tranzakciok import Bevetel
from tranzakciok import Kiadas
from tranzakciok import Tranzakciok

srdic_igor = Tranzakciok()
penztar = Penztar()
mutato = Mutatok(srdic_igor, penztar)

penztar.hozzad(Fiok("Banca Intesa", 250, "EUR"))
penztar.hozzad(Fiok("Cash", 1500, "EUR"))
penztar.hozzad(Fiok("Paypall", 30, "EUR"))

srdic_igor.hozzad(Bevetel("2023-01-15", "2023-01-17", "Fizetés", "Roadex", 116.15, 1150, "Fizetés"))
srdic_igor.hozzad(Bevetel("2023-08-16", "2023-09-02", "Fizetés", "Roadex", 116.55, 1200, "Fizetés"))
srdic_igor.hozzad(Kiadas("2023-05-22", "2023-05-22", "Rezsi költségek", "Rezsi", 116.35, 300, "Rezsi"))
srdic_igor.hozzad(Kiadas("2023-08-22", "2023-08-25", "Toszter Gorenje", "Media Markt", 116.55, 50, "Technika"))



print(f"Osszes bevetel: {srdic_igor.sum_bevetel()} EUR")
print(f"Osszes kiadas: {abs(srdic_igor.sum_kiadas())} EUR")
print(f"Mérleg: {srdic_igor.merleg()} EUR")
print(f"A vizsgált időszak mérlege: {srdic_igor.szures(2023,1)} EUR")

print(f"Osszes penz a penzartban: {penztar.osszes_osszeg()}")

penztar.osszeg_update("Cash",2500)
print(f"Osszes penz a penzartban: {penztar.osszes_osszeg()}")
print(mutato.egyensuly())



