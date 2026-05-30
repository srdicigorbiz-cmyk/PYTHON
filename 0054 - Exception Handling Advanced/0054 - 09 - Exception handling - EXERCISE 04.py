class InvalidAgeError(Exception):
    pass
def check_age(age):
    try:
        num = int(age)
        if num < 18:
            raise InvalidAgeError("Access Denied: Age is under 18!")
        else:
            print(f"Age {num} is valid.")
    except ValueError as valerr:
        print("Invalid input format")
    except InvalidAgeError as iaerr:
        print(f"Custom Error Caught: {iaerr}")






# --- TEST SUITE ---
# Test Case 1: Valid age
check_age(25) 
# Expected output: Age 25 is valid.

# Test Case 2: Underage citizen (Triggers custom exception)
check_age(16) 
# Expected output: Custom Error Caught: Access Denied: Age is under 18!

# Test Case 3: Invalid input type
check_age("húsz") 
# Expected output: Invalid input format
# ------------------