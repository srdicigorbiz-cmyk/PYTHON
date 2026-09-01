from linkedlist import LinkedList


def removeDuplicates(arr):
    
    ll = LinkedList()

    for a in arr:
        ll.addLast(a)

    if ll.size() == 0:
        return None

    current = None   
    result = []

    for n in range(ll.size()):
        value = ll.get(n)
        if current != value:
            current = value
            result.append(current)
        




    return result
    
    
