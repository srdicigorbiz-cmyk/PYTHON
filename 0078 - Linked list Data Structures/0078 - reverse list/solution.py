from linkedlist import LinkedList


def reverseList(arr):
    l_lst = LinkedList()
    result = []
    for a in arr:
        l_lst.addFirst(a)

    current = l_lst.head

    while current is not None:
        result.append(current.getValue())
        current = current.next
    return result