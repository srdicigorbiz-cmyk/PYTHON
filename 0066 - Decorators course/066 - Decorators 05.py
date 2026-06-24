def debug(func):
    def wrapper(a,b):
        print(f"Calling {func.__name__} with arguments {(a,b)}")
        print(f"{func.__name__} returned: {func(a,b)}")
        
    return wrapper

@debug
def add(a, b):
    return a + b

print(add(2,3))