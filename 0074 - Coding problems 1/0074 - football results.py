# Write code here
n = int(input())

result = 0

for i in range(n):
    inp = input()
    raw_results = []
    raw_results.append(inp.split(" "))
    raw_results[0] = [int(x) for x in raw_results[0]]
    if ((raw_results[0][0]*3) + (raw_results[0][1]*1))> result:
        result = (raw_results[0][0]*3) + (raw_results[0][1]*1)

print(result)


