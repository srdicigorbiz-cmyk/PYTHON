print("***Find index 1***")
def findIndex(s, char):
    counter = 0
    empty = True
    for c in s:
        if c == char:
            empty = False
            return counter
        else:
            counter += 1
    if empty is True:
        return -1   



word = input("Give me a word:")
char = input("Give me a char:")
print(findIndex(word, char))


print("***Find index 2***")
def findIndex(s, char):
    for index, c in enumerate(s):
        if c == char:
            return index
    return -1

word = input("Give me a word:")
char = input("Give me a char:")
print(findIndex(word, char))