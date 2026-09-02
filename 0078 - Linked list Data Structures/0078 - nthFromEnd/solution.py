from linkedlist import LinkedList


def nthFromEnd(arr, n):
    ll = LinkedList()

    for a in arr:
        ll.addLast(a)
    
    if n > ll.size():
        return -1
    
    return ll.get(ll.size()-n)
