"""We have to create a function calculator which will handle all Custom & Built-in Exceptions.
It will take mathematical operation of string type (Expression) as argument. Below are Exception cases:-
1) Expression must contain two operands and an operator, separated by space. i.e 6 * 5 = 30. 
raise InvalidOperation user-defined Exception.
2) Validate operation symbol. Allowed operation symbols are (+, -, *, /). 
raise InvalidOperator user-defined Exception.
3) Operands must be numeric. raise Built-in TypeError.
4) Handle ZeroDivisionError. raise Built-in ZeroDivisionError.
Solve above exercise. Print below messages as it is for Exceptions.
InvalidOperation :- Please enter two operands and operator separated by space.
InvalidOperator :- Invalid operator.
TypeError & ZeroDivisionError :- Standard Exception message."""
class InvalidOperation(Exception):
    pass
class InvalidOperator(Exception):
    pass

def calculator(exp):
    try:
        operators = ('+','-','*','/')
        elements = exp.split()  
        if len(elements) != 3:
            raise InvalidOperation("Please enter two operands and operator separated by space")
        op = elements[1]
        if op not in operators:
            raise InvalidOperator("Invalid operator")
        num1 = float(elements[0])
        num2 = float(elements[2])
        num1/num2
    except Exception as e:
        print(e)
    else:
        if op == '+':
            result = num1 + num2
        elif op == '-':
            result = num1 - num2
        elif op == '*':
            result = num1 * num2
        elif op == '/':
            result = num1/num2
        print(result)


#test
calculator("5 * 8")
calculator("8 / 4")
calculator("5 - 1")
calculator("5 + 8")
calculator("5 a 8")
calculator("0 / 5")
calculator("5 / 0")
calculator("a * 8")
# ==============================================================================
# READY-TO-USE TEST SUITE & SAMPLE DATA
# ==============================================================================
print("--- CODDY PLATFORM TEST SUITE ---")

print("\n[1] Érvényes alapműveletek tesztje:")
calculator("5 * 8")  # Elvárt: 40
calculator("8 / 4")  # Elvárt: 2.0 (vagy 2)
calculator("5 - 1")  # Elvárt: 4
calculator("5 + 8")  # Elvárt: 13

print("\n[2] InvalidOperation (rossz formátum, szóközök hiánya vagy többlete):")
calculator("5*8")    # Elvárt: Please enter two operands and operator separated by space.
calculator("5 *")    # Elvárt: Please enter two operands and operator separated by space.
calculator("5 * 8 2")# Elvárt: Please enter two operands and operator separated by space.

print("\n[3] InvalidOperator (nem megengedett szimbólum):")
calculator("5 a 8")  # Elvárt: Invalid operator.
calculator("5 % 8")  # Elvárt: Invalid operator.

print("\n[4] Built-in TypeError (nem numerikus karakterek):")
calculator("a * 8")  # Elvárt: Standard Exception message (pl. invalid literal for int()...)

print("\n[5] ZeroDivisionError (nullával való osztás):")
calculator("5 / 0")  # Elvárt: Standard Exception message (division by zero)
# ==============================================================================