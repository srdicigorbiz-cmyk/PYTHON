def calc(operator, num1, num2=None):
    operations = {
        "+": lambda x,y: x+y,
        "add" : lambda x,y: x+y,
        "-": lambda x,y,: x-y,
        "sub": lambda x,y,: x-y,
        "*": lambda x,y,: x*y,
        "mul": lambda x,y,: x*y,
        "/": lambda x,y,: x/y,
        "div": lambda x,y,: x/y,
        "%": lambda x,y,: x%y,
        "mod": lambda x,y,: x%y,
        "^": lambda x,y,: x**y,
        "pow": lambda x,y,: x**y
    }
    if num2 == None and operator in ["+", "add", "-", "sub"]:
        num2 = num1
        num1 = 0

    if operator not in operations:
        raise Exception(f'Invalid operator "{operator}"')
    
    for n in [num1, num2]:    
        if not isinstance(n, (int, float)):
            raise Exception(f'Invalid number "{n}"')

    try:    
        return operations[operator](num1, num2)
    except ZeroDivisionError as e:
        raise Exception('Division by zero')

def eval(lista):
    if not isinstance(lista, list):
        raise Exception(f'Failed to evaluate "{lista}"')
    
    if not 2 <= len(lista) <= 3:
        raise Exception(f'Failed to evaluate "{lista}"')


    
    if len(lista)==2:
        num1 = 0
        num2 = lista[1]
    else:
        num1 = lista[1]
        num2 = lista[2]

    if isinstance(num1, list):
        num1 = eval(num1)
    
        
    if isinstance(num2, list):
        num2 = eval(num2)
    
    
    return calc(lista[0],num1,num2)

def struct(lista):
    lvl_one_op = ["*","mul","/","div","%","mod"]
    lvl_two_op = ["+", "add", "-", "sub"]
    
    if len(lista) == 3:
        return [lista[1], lista[0], lista[2]]

    for l in lista:
        for op in lvl_one_op:
            if l == op:
                idx = lista.index(l)
                return struct(lista[:idx-1]+[[lista[idx],lista[idx-1], lista[idx+1]]]+lista[idx+2:])

    if len(lista)>3:     
        return struct([[lista[1], lista[0], lista[2]]]+lista[3:])
    
        

    

