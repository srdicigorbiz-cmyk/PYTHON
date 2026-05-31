print("**************************")
lst1 = [1, 3, 5]
lst2 = [2, 4, 6, 8]
result = [x+y for x in lst1 for y in lst2]
print(result)
print("**************************")
szinek = ["piros", "kék", "fekete"]
meretek = ["S", "M", "L"]
nem = ["női", "férfi"]
# Minden színt kombinálunk minden mérettel:
variaciok = [f"{n}-{szin}-{meret}" for n in nem for szin in szinek for meret in meretek]
print(variaciok)
# Kimenet: ['piros-S', 'piros-M', 'piros-L', 'kék-S', 'kék-M', 'kék-L', 'fekete-S', 'fekete-M', 'fekete-L']
print("**************************")
heti_kiadasok = [
    [1200, 4500, 300],  # 1. hét
    [2000, 1500],       # 2. hét
    [6000, 900]         # 3. hét
]

# Kilapítjuk egyetlen listává:
osszes_kiadas = [kiadas for het in heti_kiadasok for kiadas in het]

print(osszes_kiadas)
# Kimenet: [1200, 4500, 300, 2000, 1500, 6000, 900]
print("**************************")
havi_kiadasok=[[[1200, 4500, 300],[56,48,12,33],[28,1,56,99,1],[2,77,4,68,5]],[[45,96,3,78],[1,6,8,10],[13,37,91,2],[1,8,9,7]],[[80, 45, 30],[22,30,78],[10,2],[2,3,5]]]
result =[kiadas for havi in havi_kiadasok for het in havi for kiadas in het]
print(result)
print("**************************")
# divisible containing only the integers that are divisible by the sum of their digits.
nums = [123, 45, 67, 89, 1011]
#divisible = [x for x in nums if not x%3]
divisible = [x for x in nums if not x%sum([int(y) for y in str(x)])]
print(nums)
print(divisible)
print("**************************")
# Given a list of strings "strings". Create a list comprehension that takes in a list of 
# strings "strings" and returns a new list named "pairs" containing all the pairs of strings 
# that share no common letters. The result should be ordered by the occurrence of the words 
# in the given list (by indexes).
strings = ['cat', 'dog', 'rat', 'bat']
pairs = [(szo1, szo2) for szo1 in strings for szo2 in strings if len(set(szo1) & set(szo2)) == 0 and strings.index(szo1) < strings.index(szo2)]

print(pairs)
# expected pairs = [('cat', 'dog'), ('dog', 'rat'), ('dog', 'bat')]
