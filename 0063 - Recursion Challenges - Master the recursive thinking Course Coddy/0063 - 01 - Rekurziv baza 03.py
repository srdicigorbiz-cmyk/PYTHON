
print("*** multiply elements   ***")
def multiply_elements(lista, szorzo):
    if len(lista)==0:
        return []
    
    if isinstance(lista[0], list):
        return [multiply_elements(lista[0],szorzo)] + multiply_elements(lista[1:],szorzo)
    else:
        return [lista[0]*szorzo] + multiply_elements(lista[1:],szorzo)
#test
try:
    assert multiply_elements([1, [2, 3], 4], 2) == [2, [4, 6], 8]
except AssertionError as e:
    print("valami nem jo")
finally: 
    print(multiply_elements([1, [2, 3], 4], 2))





##########################################################
##########################################################
print("*** FIND MAX NESTED   ***")
def find_max_nested(lista):
    if len(lista) == 0:
        return float('-inf')
    
    if isinstance(lista[0], list):
        return max(find_max_nested(lista[0]), find_max_nested(lista[1:]))
    else:
        return max(lista[0], find_max_nested(lista[1:]))
    
    
lista = [1, [10, 3], [5, [20, 2]]]
print(find_max_nested(lista))




##########################################################
##########################################################
print("***  HAS GREATER?  ***")
def has_greater(lista, ertek):
    if len(lista)==0:
        return False
    if lista[0]>ertek:
        return True
    else:
        return has_greater(lista[1:], ertek)

lista=[2,5,4,10]
print(has_greater(lista,10))



##########################################################
##########################################################
print("***  GET MAX DEPTH LISTS ***")
def get_max_depth(lista):
    if not isinstance(lista, list):
        return 0
    if len(lista)==0:
        return 1
    
    if isinstance(lista[0], list):
        return max(1 + get_max_depth(lista[0]), get_max_depth(lista[1:]))
    else:
        return max(0, get_max_depth(lista[1:]))
        
    


try:
    assert get_max_depth([1, 2, 3])==1
    assert get_max_depth([1, [2, 3]])==2
    assert get_max_depth([1, [2, [3]]])==3
except AssertionError as e:
    print("Nem jo")



##########################################################
##########################################################
print("*** FIND WORDS WITH A SPECIFIC LETTER ***")
