#string
print("***STRING**************************")
exp = "fff jj gg 11 22 *"
print(exp.split(" "))
print(len(exp.split(" ")))

print(type("+"))



#list
print("***LIST************************")
L = [2,4,6,8,10]
L[1:4] = [7,9]
L.append(12)
L.insert(0,1)
del L[3]
print(L)



#dict
print("***DICTIONARY************************")
dic = dict()
dic["D"]=35
#dic = {"a":13, "b":15}
dic["c"]=34
print(dic)
print("c" in dic)
print(dic["c"])
