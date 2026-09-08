def twoSum(arr, target):
    hm = HashMap()

    for index, num in enumerate(arr):
        res = target - num
        if hm.containsKey(res):
            return [hm.get(res), index]
        
        hm.put(num, index)