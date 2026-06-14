print("***counter***")
def counter(n):
    if n==0:
        print("Start")
        return
    print(n)
    counter(n-1)
counter(3)




##########################################################
##########################################################
print("***recursive sum***")
def recursive_sum(lista):
    if len(lista) == 0:
        return 0
    return lista[0]+recursive_sum(lista[1:])
print(recursive_sum([1, 2, 3, 4]))




##########################################################
##########################################################
print("***find max ***")
def find_max(lista):
    if len(lista) == 1:
        return lista[0]
    fm= find_max(lista[1:])
    if lista[0]>fm:
        return lista[0]
    else:
        return fm
print(find_max([3, 7, 2, 9, 5]))




##########################################################
##########################################################
print("*** is palindrom ***")
def ispalindrom(string):
    if len(string) <= 1:
        return True
    
    if string[0] == string[-1]:
        return ispalindrom(string[1:-1])
    else:
        return False
print(ispalindrom("oko"))





##########################################################
##########################################################
print("*** count occurencies ***")
def count_occurrences(lista, target):
    if len(lista) == 0:
        return 0
    
    match=1 if lista[0]==target else 0
    return match + count_occurrences(lista[1:],target)

print("*** filter even numbers sorted ***")
print(count_occurrences([2,5,3,6,78,4,3,5,7,78,4,435,67,74,3,33,4,5,7,8,3,2,5,67,2,2,2], 2))




##########################################################
##########################################################
def filter_even(lista):
    if len(lista)==0:
        return []
    
    if lista[0]%2:
        return filter_even(lista[1:])
    else:
        return sorted(set([lista[0]] + filter_even(lista[1:])))


lista = [2,5,3,6,78,4,3,5,7,78,4,435,67,74,3,33,4,5,7,8,3,2,5,67,2,2,2]
print(filter_even(lista))




##########################################################
##########################################################
print("*** filter long words ***")
def filter_long_words(lista, min_hossz):
    if len(lista)==0:
        return []
    
    maradek = filter_long_words(lista[1:], min_hossz)

    if len(lista[0])>min_hossz:
        return [lista[0]] + maradek
    else:
        return maradek

lista= "Mehetünk tovább egy fokkal xxxxxxxxxxxxxxxxxx nehezebbre Ezúttal ne számokat hanem szavakat szűrjünk".split(" ")
min_hossz = 9
print(filter_long_words(lista, min_hossz))




##########################################################
##########################################################
print("*** recursive sum list ***")
def recursive_sum_list(lista):
    # Ez a te már jól ismert, listás rekurziód
    if len(lista) == 0:
        return 0
    return lista[0] + recursive_sum_list(lista[1:])




##########################################################
##########################################################
def sum_dictionary_values(szotar):
    # Itt alakítjuk át egyszer
    ertekel = list(szotar.values())
    # Itt indítjuk a rekurziót a listán
    return recursive_sum_list(ertekel)

szotar = {"a":2, "b":4, "c":8, "d":12}
print(sum_dictionary_values(szotar))