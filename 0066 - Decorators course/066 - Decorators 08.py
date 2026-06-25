def restrict_range(arg1,arg2):
    def decorator(func):
        def wrapper(*args):
            for arg in args:
                if not arg1<=arg<=arg2:
                    raise ValueError("Input argument out of range")
            return func(*args)
        return wrapper
    return decorator