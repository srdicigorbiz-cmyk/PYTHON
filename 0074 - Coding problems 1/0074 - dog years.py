def dogYears(a1):
    result = 0
    for i in range(1,a1+1):
        if i == 1:
            result += 15
        elif i == 2:
            result += 9
        elif 3 <= i <= 6:
            result += 4
        elif i >= 7:
            result += 5
    return result

print(dogYears(2))
print(dogYears(4))
print(dogYears(68))