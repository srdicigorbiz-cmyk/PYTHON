import time

def rate_limit(max_calls):
    start_time = [0]
    count_calls = [0]
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Write code here
            # Change start_time[0] and count_calls[0]
            current_time = time.monotonic()

            if current_time - start_time[0] < 1:
                count_calls[0] += 1  
            else:
                start_time[0] = current_time
                count_calls[0] = 1
                
            if count_calls[0]>max_calls:
                raise Exception("Function called too quickly")

            return func(*args, **kwargs)

        return wrapper
    return decorator