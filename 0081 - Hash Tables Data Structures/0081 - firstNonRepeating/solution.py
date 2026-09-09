from hashmap import HashMap


def firstNonRepeating(arr):
    
    hm = HashMap()

    for num in arr:
        if hm.containsKey(num):
            hm.put(num, hm.get(num)+1)
        else:
            hm.put(num, 1)

    for num in arr:
        if hm.get(num) == 1:
            return num
    
    return -1