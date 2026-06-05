print("*****GENERATOR YIELD**********************")
def szamlalo(max):
    current = 0
    while current < max:
        yield current
        current += 1

gen = szamlalo(5)
print(next(gen))
for i in gen:
    print(i)

print("*****GENERATOR () LIST COMPREHENSION**********************")
lista = [x**2 for x in range(5)]      # lista, mindent memóriában tárol
gen   = (x**2 for x in range(5))      # generátor, egyenként adja
print(lista)
print(next(gen))
print(next(gen))


def teszt():
    print("1. lépés")
    yield 10
    print("2. lépés")
    yield 20
    print("3. lépés")
    yield 30

gen = teszt()
print(next(gen))
print(next(gen))
print(next(gen))

print("*****GENERATOR () LIST COMPREHENSION**********************")

# Read input
start, end = map(int, input().split())

# TODO: Create your generator expression here
generator_exp = (x**2 for x in range(start,end) if x%2==0)  # Replace None with your generator expression

# Print the results
for value in generator_exp:
    print(value)