# Chess knight attack
column = ["a", "b", "c", "d", "e", "f", "g", "h"]

position = input()

num_enemy_positions = int(input())

enemy_positions = []
for num in range(num_enemy_positions):
    i = input()
    e_col = column.index(i[0])
    e_row = int(i[2])
    enemy_positions.append((e_col, e_row))


col = column.index(position[0])
row = int(position[2])

attack_positions = [
    (col-2, row+1),
    (col-1, row+2),
    (col+1, row+2),
    (col+2, row+1),
    (col+2, row-1),
    (col+1, row-2),
    (col-1, row-2),
    (col-2, row-1)
    ]

result = 0

for i in enemy_positions:
    for x in attack_positions:
        if i == x:
            result += 1


print(result)



