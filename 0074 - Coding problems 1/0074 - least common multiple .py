def lcm(a1, a2):
    # Write code here
    result = 2
    
    while True:
        res1 = result%a1
        res2 = result%a2
        if res1==0 and res2==0:
            break
        result += 1
    
    return result

print(lcm(2,3))