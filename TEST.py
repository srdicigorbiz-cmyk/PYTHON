# lista = [2, '%', 3, '-', 4, '/', 5.2]
# lvl_one_op = ["*","mul","/","div","%","mod"]

def parse_toy(s):
    idx = 0                      # ez a "közös jegyzet"

    def helper():
        nonlocal idx             # ez mondja: ne hozz létre saját idx-et, a külsőt használd
        result = []
        while idx < len(s) and s[idx] != ")":
            if s[idx] == "(":
                idx += 1          # lépj túl a '('-en
                inner = helper()  # rekurzió — ez maga is a közös idx-et tolja előre
                result.append(inner)
            else:
                result.append(s[idx])
                idx += 1
        if idx < len(s) and s[idx] == ")":
            idx += 1              # lépj túl a ')'-n is
        return result

    return helper()

print(parse_toy("a(b(c)d)e"))