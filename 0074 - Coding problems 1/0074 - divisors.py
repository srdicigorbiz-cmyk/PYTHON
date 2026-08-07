# Write code here
i = input().split()
i = [int(x) for x in i]
x, y = i

result = []


for o in range(x,y+1):
    counter = 0

    for w in range(1, int(o**0.5) + 1):
        if o % w == 0:
            if w * w == o:
                counter += 1
            else:
                counter += 2

    result.append([o, counter])



result= max(sorted(result), key=lambda x: x[1])
            




print(f"{result[0]} {result[1]}")