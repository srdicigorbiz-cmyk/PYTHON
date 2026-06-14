print("*** is sorted ***")
def is_sorted(lista):
    if len(lista)<=1:
        return True
    
    maradek=lista[1:]
    if lista[0]<lista[1]:
        return is_sorted(maradek)
    else:
        return False

lista = [2,5,3,6,78,4,3,5,7,78,4,435,67,74,3,33,4,5,7,8,3,2,5,67,2,2,2]
#lista = [2,3,4,5]
print(is_sorted(lista))




##########################################################
##########################################################
print("*** power, num ***")
def power(alap, kitevo):
    if kitevo < 0:
        return 1 / power(alap, -kitevo)
    
    if kitevo == 0:
        return 1
    return alap*power(alap,kitevo-1)  
print(power(12,3))




##########################################################
##########################################################
print("*** flatten list ***")
def flatten(lista):
    if len(lista)==0:
        return []
   
    if isinstance(lista[0], list):
        return flatten(lista[0])+flatten(lista[1:])
    else:
        return [lista[0]]+flatten(lista[1:])
lista = [1, [2, 3], [4, [5, 6]]]
print(flatten(lista))




##########################################################
##########################################################
print("***  count elements  ***")
def count_elements(lista):
    if len(lista) ==0:
        return 0
    
    if isinstance(lista[0], list):
        return count_elements(lista[0]) + count_elements(lista[1:])
    else:
        return 1 + count_elements(lista[1:])
    
lista = [1, [2, 3], 4]
print(count_elements(lista))
def test_count_elements():
    assert count_elements([1, [2, 3], 4]) == 4
    assert count_elements([1, [2, [3, 4]], 5]) == 5
    assert count_elements([]) == 0
    assert count_elements([1, 2, 3]) == 3
    assert count_elements([[[1]]]) == 1
    print("Minden teszt sikeresen lefutott!")

test_count_elements()