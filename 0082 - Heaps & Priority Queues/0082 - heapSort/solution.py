from minheap import MinHeap


def heapSort(arr):
    mh = MinHeap()

    for x in arr:
        mh.insert(x)

    result = []

    while mh.size()!=0:
        result.append(mh.extractMin())

    return result