from hashmap import HashMap


def mostFrequent(arr):

    hm = HashMap()

    result = [None, 0]

    for num in arr:
        if hm.containsKey(num):
            hm.put(num, hm.get(num)+1)
            if hm.get(num) > result[1]:
                result[0] = num
                result[1] = hm.get(num)
        else:
            hm.put(num, 1)
            if hm.get(num) > result[1]:
                result[0] = num
                result[1] = hm.get(num)
    
    return result[0]