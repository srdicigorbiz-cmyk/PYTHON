def hello():
    return "Hello"

def debug(func):
    def wraper():
        print(f"Calling {func.__name__}")
        print(f"{func.__name__} returned: {func()}")
    return wraper

debug_hello = debug(hello)
print(debug_hello())