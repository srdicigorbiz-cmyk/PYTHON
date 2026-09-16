from minheap import MinHeap


def kthSmallest(arr, k):
    mh = MinHeap()

    if k < 1 or k > len(arr):
        return -1

    for x in arr:
        mh.insert(x)
    
    for _ in range(k-1):
        mh.extractMin()
    
    return mh.extractMin()
