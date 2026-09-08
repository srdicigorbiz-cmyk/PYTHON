from doublylinkedlist import DoublyLinkedList


def moveToFront(arr, n):
    
    dll = DoublyLinkedList()

    if n not in arr:
        return arr

    for a in arr:
        dll.addLast(a)
    
    current = dll.head

    for x in range(dll.size()):
        # to work on
        if current.value == n:
            dll.addFirst(current.value)

            current.prev.next = current.next

            current = current.next
            
        else:
            current = current.next

    current = dll.head
    result = []

    while current is not None:
        result.append(current.value)
        current = current.next
        
    return result
    
