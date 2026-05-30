def process_string(data_str):
    try:
        float(data_str)
    except ValueError:
        print("Conversion failed")
    else:
        print(float(data_str))

# --- TEST SUITE ---
# Test Case 1: Valid conversion
process_string("42") 
# Expected output: 42.0

# Test Case 2: Invalid conversion (letters instead of digits)
process_string("hello") 
# Expected output: Conversion failed

# Test Case 3: Empty string input
process_string("") 
# Expected output: Conversion failed
# ------------------