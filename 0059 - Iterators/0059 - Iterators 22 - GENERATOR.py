print("****YIELD****************")
def paros_generator(max):
    for i in range(max+1):
        if i%2==0:
            yield i
for szam in paros_generator(6):
    print(szam)
# Elvárt kiírás: 0, 2, 4, 6

print("****GENERATOR EXPRESSION****************")
szamok = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
generator = (x**2 for x in szamok if x%3==0)
print(list(generator))

print("****YIELD FROM****************")
def sorszamok():
    for x in [1, 2, 3]:
        yield x
print(list(sorszamok()))
def sorszamok1():
    yield from [1, 2, 3]
print(list(sorszamok1()))
