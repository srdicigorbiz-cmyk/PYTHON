# Write code here
i = input()

result = []

for l in range(len(i)):
    for n in range(10):
        temp_num = list(i)
        if n != int(temp_num[l]):
            temp_num[l]=str(n)
            test_num = int("".join(temp_num))
        else:
            continue
        if test_num%3==0:
            result.append(test_num)
        

    
            

print(max(result))