import itertools
print("***COUNT********************************")
# Using count
for i in itertools.count(10, 2):
    if i > 20:
        break
    print(i)  # Prints 10, 12, 14, 16, 18, 20

print("****CYCLE*******************************")
# Using cycle
colors = itertools.cycle(['red', 'green', 'blue'])
for _ in range(6):
    print(next(colors))  # Prints red, green, blue, red, green, blue

print("****CHAIN*******************************")
# Using chain
numbers = itertools.chain([1, 2, 3], [4, 5, 6])
print(list(numbers))  # Prints [1, 2, 3, 4, 5, 6]

print("****COMBINATIONS*******************************")
# Using combinations
letters = 'ABCD'
print(list(itertools.combinations(letters, 2)))
# Prints [('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'C'), ('B', 'D'), ('C', 'D')]

print("******COMBINATIONS*****************************")
import itertools
polok = ["piros", "kék", "zöld"]
print(list(itertools.combinations(polok, r=2)))

print("******PERMUTATIONS*****************************")
import itertools
polok = ["piros", "kék", "zöld"]
print(list(itertools.permutations(polok)))


print("******ISLICE*****************************")
import itertools
szamok = itertools.count(1)
print(list(itertools.islice(szamok, 2, 7)))

print("******ZIP LONGEST*****************************")
import itertools
nevek = ["Anna", "Béla", "Csaba"]
varosok = ["Budapest", "Pécs"]
print(list(itertools.zip_longest(nevek, varosok, fillvalue="ismeretlen")))

print("******COMBINED*****************************")
import itertools
print(list(itertools.permutations(itertools.islice(itertools.count(1,1),0,4))))
