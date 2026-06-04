print("***********************************")
termekek = ["kenyér", "tej", "vaj", "sajt"]
for i in (list(enumerate(reversed(termekek)))):
    print(f"{i[0]}: {i[1]}")

print("***********************************")
dolgozok = ["Anna", "Béla", "Csaba"]
fizetesek = [350000, 420000, 380000]
result = zip(dolgozok, fizetesek)
for number, result in enumerate(result):
    print(f"{number}. {result[0]}: {result[1]} Ft")

print("***********************************")
termekek = ["alma", "körte", "szilva", "barack"]
arak = [150, 200, 180, 220]
result = list(filter(lambda x: x if x[1] < 200 else None, list(reversed(list((zip(termekek, arak)))))))
for no, data in enumerate(result):
    print(f"#{no}. {data[0]}: {data[1]}")