""""
nevek = ["Kenyér", "Tej"]
arak = [500, 400]

for nev, ar in zip(nevek,arak):
    print(f"Nev: {nev}, ar: {ar}")
"""

# Bemenetek (List comprehension-nel az árakat rögtön számmá alakítjuk)
prices = [int(p) for p in input("unesi cene:").split(",")]
items = input("naziv:").split(",")
budget_per_item = int(input("budzet:"))

affordable_items = []
cant_afford = 0
total_needed = 0

# A zip() segítségével párba állítjuk a nevet és az árat
for nev, ar in zip(items, prices):
    if ar <= budget_per_item:
        total_needed += ar
        affordable_items.append(nev)
    else:
        cant_afford += 1

print("Can buy:", affordable_items)
print("Total budget needed:", total_needed)
print("Can't afford:", cant_afford)