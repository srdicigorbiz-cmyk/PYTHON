def get_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier

double = get_multiplier(2)
triple = get_multiplier(3)

print(double(5)) # Output: 10
print(triple(5)) # Output: 15

print(get_multiplier(3)(2))
