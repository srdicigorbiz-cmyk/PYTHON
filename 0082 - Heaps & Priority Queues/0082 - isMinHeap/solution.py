from minheap import MinHeap


def isMinHeap(arr):
    
    mh = MinHeap()

    mh.heap = arr

    if len(arr) < 2:
        return True

    for index, num in enumerate(mh.heap):
        if index > 0:
            if mh.heap[mh.parent(index)] > num:
                return False
    
    return True   
