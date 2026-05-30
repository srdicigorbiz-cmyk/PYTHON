import sys

def calculate_power(base_str, exp_str):
    try:
        num1=float(base_str)
        num2=float(exp_str)
        if num2 < 0:
            raise ValueError("Negative exponent not allowed")
        else:
            print(num1**num2)
    except ValueError as e:
        if str(e) == "Negative exponent not allowed":
            print(e)
        else:
            print("Invalid input format")
        




# --- TEST SUITE ---
# Test Case 1: Valid calculation
calculate_power("5", "2") 
# Expected output: 25.0

# Test Case 2: Invalid number format
calculate_power("abc", "2") 
# Expected output: Invalid input format

# Test Case 3: Negative exponent (Not allowed in this task)
calculate_power("5", "-1") 
# Expected output: Negative exponent not allowed
# ------------------