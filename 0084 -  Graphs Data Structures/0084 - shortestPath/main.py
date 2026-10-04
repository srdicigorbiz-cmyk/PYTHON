import sys
from solution import shortestPath

data = sys.stdin.read().split("\n")
header = data[0].split()
n = int(header[0]); m = int(header[1]); start = int(header[2]); end = int(header[3])
adjacency = []
for i in range(m):
    parts = data[1 + i].split()
    adjacency.append([int(parts[0]), int(parts[1])])
print(shortestPath(adjacency, start, end))
