char = input()
message = input()[::-1]
result = []
for idx in range(len(message)):
    if idx%2:
        result.append(message[idx])
    else:
        result.append(char)

print("".join(result))

