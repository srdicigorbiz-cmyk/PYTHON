i = int(input())
matrix = [[int(x) for x in input().split()] for _ in range (i)]


result = set()

for row in matrix:
    result.add(sum(row))

for row in zip(*matrix):
    result.add(sum(row))





if len(result) != 1:
    print(False)
else:
    print("True",*result)


