from hashmap import HashMap


def firstRepeated(arr):
    
    hm = HashMap()

    for item in arr:
        if hm.containsKey(item):
            return item
        else:
            hm.put(item, True)
    
    return -1
