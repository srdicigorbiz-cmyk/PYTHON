# height and width of the matrix
height, width = input().split()

# numebr of houses to paint
num_house_to_paint = int(input())

# number of coordinate lines to input
num_of_lines = int(input())
# input coordinates and store
coordinates = set()
for n in range(num_of_lines):
    i = (input().split())
    i = [int(x)-1 for x in i]
    i = (i[0], i[1])
    coordinates.add(i)

# input of coordinates to matrix
matrix = []
for h in range(int(height)):
    matrix.append([])
    for w in range(int(width)):
        matrix[-1].append(0)

# addig initial house coordinates to matrix
for c in coordinates:
    x, y = c
    matrix[x][y]=1
    
month = 0
painted_houses = num_of_lines

while painted_houses < num_house_to_paint:
    
    # calculate new coordinate and make a list of them
    add_coordinates = set()
    for c in coordinates:
        add_coordinates.add(((c[0]-1), c[1]))
        add_coordinates.add(((c[0]+1), c[1]))
        add_coordinates.add((c[0], (c[1]-1)))
        add_coordinates.add((c[0], (c[1]+1)))
    
    # move new coordinates to coordinates list
    for ac in add_coordinates:
        if 0 <= ac[0] <= int(height)-1 and 0 <= ac[1] <= int(width)-1:
            coordinates.add(ac)
    
    #reset add coordinates
    add_coordinates = set()
    
    #adding house cordinates to matrix
    for c in coordinates:
        x, y = c
        matrix[x][y]=1
    
    
    # counting the number of houses in the matrix
    painted_houses = 0
    for m in matrix:
        for n in m:
            if n == 1:
                painted_houses += 1

    # add month at the end of the cycle    
    month += 1

print(month)