from linkedlist import LinkedList


def mergeSorted(a, b):
    # TODO: Write code here
    ll_a = LinkedList()
    ll_b = LinkedList()

    for n in a:
        ll_a.addLast(n)
    for n in b:
        ll_b.addLast(n)

    current_a = ll_a.head
    current_b = ll_b.head

    result = []

    while current_a is not None or current_b is not None:
        if current_a is None:
            result.append(current_b.value)
            current_b = current_b.next
        elif current_b is None:
            result.append(current_a.value)
            current_a = current_a.next
        elif current_a.value < current_b.value:
            result.append(current_a.value)
            current_a = current_a.next
        else:
            result.append(current_b.value)
            current_b = current_b.next
    
    
    return result
