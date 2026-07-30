inp = int(input())


sequence = [1,1]

while True:
    result = sequence[-1]+sequence[-2]
    if result <= inp:
        sequence.append(result) 
    else:
        break
    


res = [str(x) for x in sequence]
print(" ".join(res))