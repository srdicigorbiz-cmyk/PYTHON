def isBalanced(s):
    if len(s)%2 or 0:
        return False
    else:
        balance = 0
        for z in s:
            if z == "(":
                balance += 1
            elif z ==")":
                balance += -1
            if balance < 0:
                return False
        if balance != 0:
            return False
        else:
            return True




def test_isBalanced():
    # Test esetek: (bemenet, várt eredmény)
    test_cases = [
        ("((()))", True),
        ("()()", True),
        ("(())()", True),
        ("(()", False),
        (")(", False),
        ("())", False),
        ("", True),          # Üres sztring is "kiegyensúlyozott"
        ("((((", False),
        ("())(()", False)
    ]
    
    for s, expected in test_cases:
        result = isBalanced(s)
        status = "SIKER" if result == expected else "HIBA"
        print(f"Bemenet: '{s}' | Várt: {expected} | Eredmény: {result} -> {status}")
test_isBalanced()
# Így tudod futtatni:
# test_isBalanced()