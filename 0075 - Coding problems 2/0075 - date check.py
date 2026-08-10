d, m, y = map(int, input().split())


short_m = (4,6,9,11)
long_m = (1,3,5,7,8,10,12)

not_valid = "NOT VALID"
valid = "VALID"


if not 1 <= m <=12:
    print(not_valid)
elif y < 0:
    print(not_valid)
elif m in short_m and not 1 <= d <= 30:
    print(not_valid)
elif m in long_m and not 1 <= d <= 31:
    print(not_valid)
elif m == 2:
    if 1 <= d <= 28:
        print(valid)
    elif not y%400 or (not y%4 and y != 100):
        if d == 29:
            print(valid)
        else:
            print(not_valid)
    else:
        print(not_valid)
else:
    print(valid)

