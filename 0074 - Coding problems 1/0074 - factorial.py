def factorial(a1):
    
    result = 1
    for i in range(1,a1+1):
        result *= i

    return result

print(factorial(8))