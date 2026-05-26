from vehicle import Vehicle
from car import Car
from truck import Truck
jarmuvek = [
    Car("Audi", 50, 5, "diesel"),
    Truck("Scania", 120, 15, "diesel"),
    Car("Tesla", 80, 5, "elektromos"),
    Car("Fiat", 20, 4, "benzin"),
    Truck("Volvo", 150, 18, "diesel")
]
""""
for jarmu in jarmuvek:
    jarmu.display_info()
    uj_ar=jarmu.rent_price *1.2
    print(uj_ar)

for jarmu in jarmuvek:
    if jarmu.rent_price > 100:
        jarmu.display_info()

for jarmu in jarmuvek:
    if isinstance(jarmu, Truck):
        jarmu.display_info()

for jarmu in jarmuvek:
    if isinstance(jarmu, Car) and jarmu.fuel=="diesel":
        jarmu.display_info()

def szamold_ki_a_bevételt(jarmuvek):
    osszes_bevétel = 0
    for jarmu in jarmuvek:
        osszes_bevétel += jarmu.rent_price
    return osszes_bevétel

eredmeny = szamold_ki_a_bevételt(jarmuvek)
print(f"A függvény szerint a bevétel: {eredmeny} Ft")

def szamolj_tipusokat(jarmuvek):
    kamion = 0
    auto = 0
    for jarmu in jarmuvek:
        if isinstance(jarmu, Truck):
            kamion += 1
        elif isinstance(jarmu, Car):
            auto += 1

    return(f"A flottában {auto} autó és {kamion} teherautó található.")

print(szamolj_tipusokat(jarmuvek))


def akcios_ar_beallitas(jarmuvek, szazalek):
    for jarmu in jarmuvek:
        sale_price=jarmu.rent_price*szazalek
        jarmu.rent_price = sale_price
    
    print("Az árak frissítve!")

    for jarmu in jarmuvek:
        jarmu.display_info()

akcios_ar_beallitas(jarmuvek, 0.9)
""

def keresd_a_legdragabbat(jarmuvek):
    legdragabb = 0
    for jarmu in jarmuvek:
        if jarmu.rent_price > legdragabb:
            legdragabb = jarmu.rent_price
    for jarmu in jarmuvek:
        if jarmu.rent_price == legdragabb:
            jarmu.display_info()
    

keresd_a_legdragabbat(jarmuvek)


def szervizre(jarmuvek):
    szerviz_utca = list()
    for jarmu in jarmuvek:
        if jarmu.rent_price < 40:
            szerviz_utca.append(jarmu)
    
    for jarmu in szerviz_utca:
        jarmu.display_info()

szervizre(jarmuvek)
"""
def melyik_olcsobb(j1, j2):
    result = j1
    if j1.rent_price > j2.rent_price:
        result=j2
    return result


olcsobb_jarmu = melyik_olcsobb(jarmuvek[1],jarmuvek[4])
print("A kettő közül ez az olcsóbb:")
olcsobb_jarmu.display_info()



