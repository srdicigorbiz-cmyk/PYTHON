import itertools
print("***********************************")
ranks = ['Ace','2','3','4','5']
suits = ['Hearts','Diamonds','Clubs','Spades']
start, stop = 0, 5
# TODO: Write your code below
# Use itertools.product() to generate all possible combinations of ranks and suits
# Use itertools.islice() to select a portion of these combinations
# Format each card as "Rank of Suit"
card = list(itertools.islice((itertools.product(ranks, suits)), start, stop))
# Print each formatted card on a new line
# print(card)
for c in card:
    print(f"{c[0]} of {c[1]}")

print("***********************************")
munkakozok = ["Anna", "Béla", "Csaba", "Dóra"]
varosok = ["Budapest", "Pécs", "Győr"]