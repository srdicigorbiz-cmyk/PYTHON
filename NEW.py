def longestCommonPrefix(a):
    prime = a[0]
    lenght = len(a[0])
    idx = 1
    
    for word in a:
        if word[0:idx] != prime[0:idx]:
            return result
        else: 
            result = word[0:idx]
        idx += 1
        
    return result
        


    


    
    

list1= ["something", "somehow", "somewhat"]
list2= ["Hello Bob", "Hello Jake"]
list3= ["example", "sample"]
print(longestCommonPrefix(list1))
print(longestCommonPrefix(list2))
print(longestCommonPrefix(list3))