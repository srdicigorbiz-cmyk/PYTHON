import itertools
print("***********************************")
ranks = ['Ace','2','3','4','5']
suits = ['Hearts','Diamonds','Clubs','Spades']
start, stop = 0, 5
card = list(itertools.islice((itertools.product(ranks, suits)), start, stop))
for c in card:
    print(f"{c[0]} of {c[1]}")

print("***********************************")
munkakozok = ["Anna", "Béla", "Csaba", "Dóra"]
varosok = ["Budapest", "Pécs", "Győr"]
print(list(itertools.zip_longest(munkakozok, varosok, fillvalue="nincs beosztás")))

print("***********************************")
muszakok = ["reggel", "déli", "éjjel"]
dolgozok = ["Anna", "Béla"]
print(list(itertools.product(muszakok, dolgozok)))

print("***********************************")
termekek = ["alma", "körte", "szilva", "barack", "meggy"]
arak = [150, 200, 180, 220, 160]
print(list(enumerate(list(itertools.islice((list(reversed(list(zip(termekek,arak))))), 2, 4)))))