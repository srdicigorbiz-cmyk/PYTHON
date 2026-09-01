from linkedlist import LinkedList


def findMiddle(arr):
    ll = LinkedList()
    
    for a in arr:
        ll.addLast(a)
    
    if ll.size() == 0:
        return -1

    current = ll.head
    middle = ll.head

    while current is not None and current.next is not None:
        current = current.next.next
        middle = middle.next

    return middle.getValue()