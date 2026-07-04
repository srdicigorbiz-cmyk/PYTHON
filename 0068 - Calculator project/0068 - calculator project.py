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
    
    if isinstance(lista, (str, int, float, bool)) or len(lista) == 1 or not len(lista)%2:
        raise Exception(f'Failed to structure "{lista}"')
    
    

    if len(lista) == 2:
        return lista

    if len(lista) == 3:
        return [lista[1], lista[0], lista[2]]

    for l in lista:
        if l == "^" or l == "pow":
            idx = lista.index(l)
            return struct(lista[:idx-1]+[[lista[idx],lista[idx-1], lista[idx+1]]]+lista[idx+2:])



    for l in lista:
        for op in lvl_one_op:
            if l == op:
                idx = lista.index(l)
                return struct(lista[:idx-1]+[[lista[idx],lista[idx-1], lista[idx+1]]]+lista[idx+2:])

    for l in lista:
        for op in lvl_two_op:
            if l == op:
                idx = lista.index(l)
                return struct(lista[:idx-1]+[[lista[idx],lista[idx-1], lista[idx+1]]]+lista[idx+2:])

        
    if len(lista)>3:     
        return struct([[lista[1], lista[0], lista[2]]]+lista[3:])
    
def get_next(lst_str, idx):
    if lst_str == "" or idx >= len(lst_str):
        raise Exception("End of string")
    
    result_string = ""    

    #check for int or float
    for n in range(0, (len(lst_str)-idx)):
        check = lst_str[idx+n]
        if check.isdigit() or check == ".":
            result_string += lst_str[idx+n]
        else:
            break
    
    #check for operator
    for n in range(0, (len(lst_str)-idx)):
        check = lst_str[idx+n]
        if check.isalpha() or check in ["+", "-", "*","/","%","^"]:
            result_string += lst_str[idx+n]
        else:
            break
    


    
    if "." in result_string:
        return float(result_string)
    
    if result_string.isdigit():
        return int(result_string)

    if isinstance(result_string, str):
        return result_string

def parse(input_string):
    input_string = input_string.replace(' ', '')
    idx = 0

    def list_maker():
        lista = []
        len_lst = len(input_string)
        nonlocal idx

        while idx < len_lst and input_string[idx] != ")":
            if input_string[idx] == "(":
                idx += 1
                sub_list = list_maker()
                lista.append(struct(sub_list))
            else:
                a = get_next(input_string, idx)
                lista.append(a)
                idx += len(str(a))
            

        if idx < len_lst and input_string[idx] == ")":
            idx += 1

        return lista   
    
    lista=list_maker()
    return struct(lista)
    
def pre_parse(input_string):
    counter = 0
    for s in input_string:
        if s == "(":
            counter += 1
        elif s == ")":
            counter -= 1
    if counter != 0:
        raise Exception("Not matching parenthesis")
  

