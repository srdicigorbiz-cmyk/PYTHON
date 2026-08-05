def largestNum(n):
        
    results = []
    l = len(str(n))

    for i in range(l):
        for j in range(10):
            change_num = list(str(n))
            change_num.pop(i)
            change_num.insert(i, str(j))
    
            test_num = int("".join(change_num))


            if not test_num%3 and test_num!=n:
                results.append(test_num)

    return(max(results))

print(largestNum(999))