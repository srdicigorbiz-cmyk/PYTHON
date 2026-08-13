i = 30

res = []

for x in range(1, i):
    result = []
    for y in range(1,x):
        if x%y==0:
           result.append(y)        
    
    res.append([x, sum(result)])

print(max(res, key=lambda x: x[-1])[0])