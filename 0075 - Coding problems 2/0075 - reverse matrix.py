i = int(input())

result = []

for n in range(i):
    x = [int(x) for x in input().split()]
    for y in range(i):
        if y <= n:
            print(f"{-1*x[y]} ", end="")
        else:
            print(f"{x[y]} ", end="")
    print("")


    
