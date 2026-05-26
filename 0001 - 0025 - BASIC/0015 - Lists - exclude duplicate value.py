elements=["freedom", "liberty", "justice", "hope", "dreams", "hope", "peace"]


filter1=[n.upper() for n in elements if len(n)>=5]    
result=[]
for i in filter1:
    if i not in result:
        result.append(i)
return result