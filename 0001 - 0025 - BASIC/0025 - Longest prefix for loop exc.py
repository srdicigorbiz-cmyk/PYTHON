def longestCommonPrefix(a):
    prime_word = a[0]
    lenght = len(a[0])
    idx = 1
    
    for letter in prime_word:
        for item in a:
           if prime_word[0:idx] != item[0:idx]:
               return prime_word[0:(idx-1)]
        idx += 1
    return prime_word
        
list1= ["something", "somehow", "somewhat"]
list2= ["Hello Bob", "Hello Jake"]
list3= ["example", "sample"]
print(longestCommonPrefix(list1))
print(longestCommonPrefix(list2))
print(longestCommonPrefix(list3))