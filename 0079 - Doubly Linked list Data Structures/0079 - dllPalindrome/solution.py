from doublylinkedlist import DoublyLinkedList


def isPalindrome(arr):
    dll = DoublyLinkedList()
    
    for a in arr:
        dll.addLast(a)
    
    if dll.size() == 0:
        return True

    cur_head = dll.head
    cur_tail = dll.tail

    while cur_head is not None and cur_tail is not None:
        if cur_head.value != cur_tail.value:
            return False
        else:
            cur_head = cur_head.next
            cur_tail = cur_tail.prev
    
    return True
            
