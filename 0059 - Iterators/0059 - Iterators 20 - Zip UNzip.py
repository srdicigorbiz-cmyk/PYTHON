print("***zip reversed***************************")
nevek = ["Anna", "Bence", "Cili"]
ajandekok = ["Labda", "Könyv", "Csoki"]
# Azt szeretnénk, hogy:
# Anna kapja a Csokit (ajándékok utolsó eleme)
# Bence kapja a Könyvet (ajándékok középső eleme)
# Cili kapja a Labdát (ajándékok első eleme)
print(list(zip(nevek, list(reversed(ajandekok)))))

print("***UNzip***************************")
points = [(1, 10), (2, 20), (3, 30)]
all_x, all_y=(zip(*points))
print(all_x)
print(all_y)