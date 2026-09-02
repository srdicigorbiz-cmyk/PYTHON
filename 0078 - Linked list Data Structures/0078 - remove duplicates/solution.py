from linkedlist import LinkedList


def removeDuplicates(arr):
    
    ll = LinkedList()

    for a in arr:
        ll.addLast(a)

    if ll.size() == 0:
        return []

    current = ll.head
    result = []

    while current is not None and current.next is not None:
        if current.value == current.next.value:
            current.next = current.next.next
        else:
            current = current.next
        
    current = ll.head

    while current is not None:
        result.append(current.value)
        current = current.next




    return result
    
    
