from money import Money

# Test case handler
test_case = input("basic_test")

def test_basic_functionality():
    # Test initialization and string representation
    m1 = Money(10.0, "USD")
    assert str(m1) == "10.00 USD", f"__str__ method failed, got {str(m1)}"
    
    # Test addition
    m2 = Money(20.0, "USD")
    m3 = m1 + m2
    assert str(m3) == "30.00 USD", f"Addition failed, got {str(m3)}"
    
    # Test different currency addition
    m4 = Money(20.0, "EUR")
    try:
        m5 = m1 + m4
        assert False, "Adding different currencies should raise an error"
    except ValueError as e:
        assert str(e) == "Cannot add different currencies", f"Wrong error message: {str(e)}"
    
    # Test multiplication
    m6 = m1 * 3
    assert str(m6) == "30.00 USD", f"Multiplication failed, got {str(m6)}"
    
    # Test equality
    assert m1 == Money(10.0, "USD"), "Equality test failed"
    assert m1 != m2, "Inequality test failed"
    
    print("All basic functionality tests passed!")

def test_zero_values():
    # Test with zero amount
    m1 = Money(0.0, "USD")
    assert str(m1) == "0.00 USD", f"Zero amount string representation failed, got {str(m1)}"
    
    # Test addition with zero
    m2 = Money(10.0, "USD")
    m3 = m1 + m2
    assert str(m3) == "10.00 USD", f"Addition with zero failed, got {str(m3)}"
    
    # Test multiplication by zero
    m4 = m2 * 0
    assert str(m4) == "0.00 USD", f"Multiplication by zero failed, got {str(m4)}"
    
    # Test equality with zero amount
    assert m1 == Money(0.0, "USD"), "Equality with zero amount failed"
    assert m1 != m2, "Inequality with zero amount failed"
    
    print("All zero value tests passed!")

def test_negative_values():
    # Test with negative amount
    m1 = Money(-10.0, "USD")
    assert str(m1) == "-10.00 USD", f"Negative amount string representation failed, got {str(m1)}"
    
    # Test addition with negative amounts
    m2 = Money(20.0, "USD")
    m3 = m1 + m2
    assert str(m3) == "10.00 USD", f"Addition with negative amount failed, got {str(m3)}"
    
    m4 = Money(-5.0, "USD")
    m5 = m1 + m4
    assert str(m5) == "-15.00 USD", f"Addition of two negative amounts failed, got {str(m5)}"
    
    # Test multiplication by negative scalar
    m6 = m2 * -2
    assert str(m6) == "-40.00 USD", f"Multiplication by negative scalar failed, got {str(m6)}"
    
    # Test equality with negative amounts
    assert m1 == Money(-10.0, "USD"), "Equality with negative amount failed"
    assert m1 != m2, "Inequality with negative amount failed"
    
    print("All negative value tests passed!")

def test_large_values():
    # Test with very large amounts
    m1 = Money(1000000.0, "USD")
    assert str(m1) == "1000000.00 USD", f"Large amount string representation failed, got {str(m1)}"
    
    # Test addition with large amounts
    m2 = Money(2000000.0, "USD")
    m3 = m1 + m2
    assert str(m3) == "3000000.00 USD", f"Addition with large amounts failed, got {str(m3)}"
    
    # Test multiplication with large scalar
    m4 = m1 * 1000
    assert str(m4) == "1000000000.00 USD", f"Multiplication with large scalar failed, got {str(m4)}"
    
    print("All large value tests passed!")

def test_precision():
    # Test with fractional amounts
    m1 = Money(10.25, "USD")
    assert str(m1) == "10.25 USD", f"Fractional amount string representation failed, got {str(m1)}"
    
    m2 = Money(10.2, "USD")
    assert str(m2) == "10.20 USD", f"Two decimal place formatting failed, got {str(m2)}"
    
    # Test addition with fractional amounts
    m3 = Money(0.75, "USD")
    m4 = m1 + m3
    assert str(m4) == "11.00 USD", f"Addition with fractional amounts failed, got {str(m4)}"
    
    # Test multiplication with fractional scalar
    m5 = m1 * 0.5
    assert str(m5) == "5.13 USD", f"Multiplication with fractional scalar failed, got {str(m5)}"
    
    print("All precision tests passed!")

def test_type_validation():
    try:
        # These operations should work without errors
        m1 = Money(10.0, "USD")
        m2 = m1 * 2
        m3 = m1 * 2.5
        
        # Test equality with different types
        assert (m1 == "10.00 USD") == False, "Equality with string should return False"
        assert (m1 == 10.0) == False, "Equality with number should return False"
        
        print("All type validation tests passed!")
    except Exception as e:
        print(f"Type validation test failed: {e}")

def test_currency_case_sensitivity():
    # Test currency case sensitivity
    m1 = Money(10.0, "USD")
    m2 = Money(10.0, "usd")
    
    # Currencies should be case-sensitive
    assert m1 != m2, "Currency comparison should be case-sensitive"
    
    # Adding different cases should fail
    try:
        m3 = m1 + m2
        assert False, "Adding different currency cases should raise an error"
    except ValueError as e:
        assert str(e) == "Cannot add different currencies", f"Wrong error message: {str(e)}"
    
    print("All currency case sensitivity tests passed!")

def test_performance():
    # Create many Money objects and perform operations
    base = Money(1.0, "USD")
    result = base
    
    # Perform 1000 additions
    for i in range(1000):
        result = result + Money(1.0, "USD")
    
    assert str(result) == "1001.00 USD", f"Performance test addition failed, got {str(result)}"
    
    # Perform 10 multiplications
    result = base
    for i in range(10):
        result = result * 2
    
    assert str(result) == "1024.00 USD", f"Performance test multiplication failed, got {str(result)}"
    
    print("All performance tests passed!")

# Run the appropriate test based on input
if test_case == "basic_test":
    test_basic_functionality()
elif test_case == "zero_values":
    test_zero_values()
elif test_case == "negative_values":
    test_negative_values()
elif test_case == "large_values":
    test_large_values()
elif test_case == "precision":
    test_precision()
elif test_case == "type_validation":
    test_type_validation()
elif test_case == "currency_case":
    test_currency_case_sensitivity()
elif test_case == "performance":
    test_performance()
else:
    print(f"Unknown test case: {test_case}")