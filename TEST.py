lista = [2, '%', 3, '-', 4, '/', 5.2]
lvl_one_op = ["*","mul","/","div","%","mod"]



for l in lista:
    for op in lvl_one_op:
        if l == op:
            print(lista.index(l))



