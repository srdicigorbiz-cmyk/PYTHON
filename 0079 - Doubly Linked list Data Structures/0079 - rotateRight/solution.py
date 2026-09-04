from doublylinkedlist import DoublyLinkedList


def rotateRight(arr, n):
    dll = DoublyLinkedList()

    for a in arr:
        dll.addLast(a)
    
    if dll.size()==0:
        return []
    
    if n >= dll.size():
        n = n%dll.size()

    current = dll.tail

    for x in range(n):
        dll.addFirst(current.value)
        dll.removeLast()
        current = dll.tail
    
    current = dll.head

    result = []

    while current is not None:
        result.append(current.value)
        current = current.next
    
    return result
