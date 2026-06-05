print("****cycle********")
import itertools
nevek = ["Anna", "Bence", "Cili"]
counter = 0
for n in itertools.cycle(nevek):
    if counter <7:
        print(n)
        counter += 1
    else:
        break
# or version 2.
import itertools
nevek = ["Anna", "Bence", "Cili"]
korforgas = itertools.cycle(nevek)
for _ in range(7):
    print(next(korforgas))

print("****chain********")
import itertools
fiuk = ["Bence", "Dávid"]
lanyok = ["Anna", "Cili"]
# Úgy megy végig rajtuk, mintha egy nagy lista lenne
for ember in itertools.chain(fiuk, lanyok):
    print(ember)

print("****accumulate & chain********")
bolt_bevetel = [100, 200]
web_bevetel = [300, 400]
print(list(itertools.accumulate(itertools.chain(bolt_bevetel, web_bevetel))))

print("**** KOMBINATORIKA ********")
student=["Dóra", "Gábor", "Hanna", "Tamás"]
print(list(itertools.combinations(student, 2)))