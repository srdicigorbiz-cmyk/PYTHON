print("***equal inputs****************************")
a = 1
b = 1
c = 1
is_equal = lambda a, b, c : (a is None and b == c) or (b is None and a == c) or (c is None and a == b) or (a == b and b == c)
print(is_equal(a,b,c))

print("*****function  return a lambda function**************************")
def message_constructor(first, last):
    # Write code here
    if last is None:
        full_name = first
    else:
        full_name = first+" "+last
    return lambda udvozles : udvozles + ", " + full_name   
uzenet = message_constructor("john", "Doe")
print(uzenet("hello"))

print("****function  return a lambda function***************************")
# 1. LÉPÉS: Megírjuk a gyárat
def fagylaltgep_gyar(iz):
    # Ez a gyár nem fagyit ad vissza, hanem egy MINI GÉPET (lambdát)
    # Ez a mini gép várni fog egy 'tolcser_meret' változót!
    return lambda tolcser_meret : f"Kaptál egy {tolcser_meret} adag {iz} fagyit!"
# 2. LÉPÉS: Rendelünk a gyáratól egy CSOMAGOLT GÉPET
# Meghívjuk a gyárat a "csoki" szóval:
csokis_gepem = fagylaltgep_gyar("csoki")
# 3. LÉPÉS: Elindítjuk a gépet (meghívjuk a lambdát)
# Most adjuk meg neki azt a változót, amit a lambda a kettőspont előtt kért (tolcser_meret):
print(csokis_gepem("nagy"))   # Kimenet: Kaptál egy nagy adag csoki fagyit!
print(csokis_gepem("kicsi"))  # Kimenet: Kaptál egy kicsi adag csoki fagyit!

print("****FILTER: vowels out***************************")
iterable = input("Give me the word(s)") 
function = lambda x: x not in ('a', 'e', 'i', 'o', 'u')
no_vowels = filter(function, iterable)
print(''.join(list(no_vowels)))

print("***MAP:vowels x 2****************************")
iterable = input("Give me the word(s)")
function = lambda x: x*2 if x in ('a', 'e', 'i', 'o', 'u') else x
double_vowels = map(function, iterable)
print(''.join(list(double_vowels)))

print("*****FIRST BIGGER**************************")
first_bigger = lambda lista: list(filter(lambda x: x[0]>x[1], lista)) 
print(first_bigger([(1, 2), (3, 1), (4, 4), (5, 3), (2, 6)]))

print("****SUM BIGGER THAN 20***************************")
sum_bigger = lambda lista: list(filter(lambda x: x>20, list(map(lambda x: sum(x), lista))))
print(sum_bigger([(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12)]))
sum_bigger1 = lambda lista: list(filter(lambda x: x > 20, list(map(sum, lista))))
print(sum_bigger1([(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12)]))

print("****MEDIAN***************************")
median = 
print(median([10, 5, 8, 7, 9, 4]))