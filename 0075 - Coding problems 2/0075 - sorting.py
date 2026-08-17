# sorting
i = int(input())
numbers = [int(x) for x in input().split()]

counter = 0
idx = 0

while True:
    if i < 2:
        break

    if numbers[idx]>numbers[idx+1]:
        save = numbers[idx]
        numbers[idx] = numbers[idx+1]
        numbers[idx+1] = save
        counter += 1
        idx = 0
    else:
        idx += 1
    
    if idx == i-1:
        break
 
print(counter)

