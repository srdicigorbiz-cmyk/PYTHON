from hashmap import HashMap


def isAnagram(s1, s2):
    
    hm = HashMap()

    if len(s1) != len(s2):
        return False
    
    
    for letter in s1:
        if hm.containsKey(ord(letter)):
            hm.put(ord(letter), hm.get(ord(letter)) + 1)
        else:
            hm.put(ord(letter), 1)
    
    for letter in s2:
        if hm.containsKey(ord(letter)):
            hm.put(ord(letter), hm.get(ord(letter)) - 1)
            if hm.get(ord(letter)) < 0:
                return False
        else:
            return False
    
    return True

    
    
    