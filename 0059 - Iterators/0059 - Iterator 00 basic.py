lista = [1, 2, 3]
it = iter(lista)
print(type(it))

print(dir(it))

print(next(it))
print(next(it))
print(next(it))
print(next(it))

print("*****ENUMERATE ZIP REVERSED")
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
combined = list(zip(names, ages))
revers = list(reversed(combined))
enumer = list(enumerate(revers))
proba = list(enumerate(reversed(list(zip(names, ages)))))
proba1 = list(reversed(list(zip(names, ages))))
print(combined)
print(revers)
print(enumer)
print(proba)
print(proba1)
