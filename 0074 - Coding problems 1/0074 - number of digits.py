def numberOfDigits(a1):
    # Write code here
    counter = 1
    result = a1
    while True:
        if result//10 >= 1:
            counter += 1
            result = result//10
        else:
            break
    return(counter)

print(numberOfDigits(1432))