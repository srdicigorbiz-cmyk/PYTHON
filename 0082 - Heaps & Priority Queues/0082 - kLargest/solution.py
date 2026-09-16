from minheap import MinHeap


def kLargest(arr, k):
    
    mh = MinHeap()

    if k <= 0:
        return []
    
    if k > len(arr):
        k = len(arr)
    
    for x in range(k):
        mh.insert(arr[x])
    
    
    for x in range(k, len(arr)):
        if mh.peek() < arr[x]:
            mh.extractMin()
            mh.insert(arr[x])

    result = []
    
    while mh.size() != 0:
        result.append(mh.extractMin())
    
    return result
