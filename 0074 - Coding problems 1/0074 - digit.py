def digit(a1):

    num_list = ""
    counter = 1

    while len(num_list) < a1:
        for i in range(1, counter+1):
            num_list += str(i)
        counter += 1

    return num_list[a1-1]



print(digit(10))
print(digit(17))
print(digit(170))
print(digit(1))
