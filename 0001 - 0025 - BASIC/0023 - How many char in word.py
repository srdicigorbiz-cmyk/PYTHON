def countChar(s, char):
    counter = 0
    for c in s:
        if c == char:
            counter += 1
    return counter

s = input("Give me a word:")
char = (input("Give me a letter:"))
print(countChar(s, char))