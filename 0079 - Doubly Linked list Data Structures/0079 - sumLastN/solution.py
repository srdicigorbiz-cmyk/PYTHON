from doublylinkedlist import DoublyLinkedList


def sumLastN(arr, n):
    
    dll = DoublyLinkedList()
    
    for a in arr:
        dll.addLast(a)
    
    if n <= 0:
        return 0
    
    if n > dll.size():
        n = dll.size()
    
    current = dll.tail
    result = []

    for x in range(n):
        result.append(current.value)
        current = current.prev
    
    return sum(result)

