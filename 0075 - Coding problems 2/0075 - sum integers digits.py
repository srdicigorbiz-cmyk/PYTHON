sum_num = sum(map(int, input()))

result = []

while True:
    try:
        i = int(input())
        sum_n = (sum(map(int, str(i))))
        if sum_num == sum_n:
                result.append(i)

    except ValueError:
        break

for r in result:
    print(r)