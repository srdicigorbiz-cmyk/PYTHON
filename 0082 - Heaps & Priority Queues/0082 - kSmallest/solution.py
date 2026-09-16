from minheap import MinHeap


def kSmallest(arr, k):
    mh = MinHeap()

    for num in arr:
        mh.insert(num)

    if k <=0:
        return []
    
    if k > mh.size():
        return mh.heap
    
    result = []

    for idx in range(k):
        result.append(mh.heap[idx])
    
    return result
    
    
    
    