print("***KILÖVÉS***")
start = int(input("Kérek egy számot:"))
def kiloves(start):
    while start > 0:
        result = start
        start -=1
        print(result)
    print("Kilövés")
kiloves(start)

print("***PÁROS SZÁMOK***")
limit= int(input("Kérek egy számot:"))
def paros(limit):
    counter = 1
    while counter <= limit:
        if counter%2==0:
            print(counter)
        counter += 1
paros(limit)

print("***ÖSSZEGZŐ***")    
n = int(input("Kérek egy számot:"))
def osszegzo(n):
    counter_n = 1
    result = 0
    while counter_n <= n:
        result = result + counter_n
        print(result)
        counter_n += 1
osszegzo(n)


print("***hatványozó***")    
alap = int(input("Alap:"))
kitevo = int(input("Kitevo:"))
def hatvanyozo(alap, kitevo):
    counter = 1
    result = 1
    while counter <= kitevo:
        result *= alap
        counter += 1
    print(result)
hatvanyozo(alap, kitevo)

print("***szá,jegyek összeadása***")    
n = int(input("Kérek egy számot:"))
def szamj_osszeg(n):
    result=0
    while n > 0:
        result += n%10
        n= n//10
    print(result)
szamj_osszeg(n)
        
print("***szám palindrom***")
n = int(input("Kérek egy számot:"))
