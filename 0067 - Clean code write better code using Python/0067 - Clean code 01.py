def greet(name, age):
    print('Hello,', name)
    if age >= 18:
        print('Above 18')
    else:
        print('Below 18')

def calc_id(name, age):
    res = 0
    for c in name:
        res += ord(c) * age
    return res

def init(name, age):
    greet(name, age)
    res = calc_id(name, age)
    return res

print(init("igor", 47))