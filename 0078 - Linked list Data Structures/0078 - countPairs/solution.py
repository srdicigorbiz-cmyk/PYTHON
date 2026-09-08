from doublylinkedlist import DoublyLinkedList


def countPairs(arr, n):
    dll = DoublyLinkedList()

    for a in arr:
        dll.addLast(a)

    result = 0

    front = dll.head
    back = dll.tail
    
    while front != back and front is not None and back is not None and front.prev != back:

        if front.value + back.value == n:
            result += 1
            front = front.next
            back = back.prev
        elif front.value + back.value < n:
            front = front.next
        elif front.value + back.value > n:
            back = back.prev

    
    return result


