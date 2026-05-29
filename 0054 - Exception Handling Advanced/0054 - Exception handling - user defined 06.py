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
        if len(exp.split(" ")) != 3:
            raise InvalidOperation("Please enter two operands and operator separated by space.")
        if 


    except InvalidOperation as iopn:
        print(iopn)

    except InvalidOperator as iopr:
        print(iopr)

    except Exception as e:
        print(e)


#test
calculator("5 * 8")
calculator("8 / 4")
calculator("5 - 1")
calculator("5 + 8")
calculator("5 a 8")
calculator("5 / 0")
calculator("a * 8")