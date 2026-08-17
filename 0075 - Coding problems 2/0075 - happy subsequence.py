# Write code here
i = int(input())
numbers = [int(x) for x in input().split()]


results = [0]

for idx in range(i):
    
    count=0
    sublist = numbers[idx:]
    
    for idx_sub in range(len(sublist)):
        if sublist[idx_sub] == 3:
            count += 1
        if count == 3:
            results.append(idx_sub+1)

print(max(results))
        