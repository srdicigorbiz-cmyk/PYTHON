import sys
from solution import bfs

data = sys.stdin.read().split("\n")
header = data[0].split()
n = int(header[0]); m = int(header[1]); start = int(header[2])
adjacency = []
for i in range(m):
    parts = data[1 + i].split()
    adjacency.append([int(parts[0]), int(parts[1])])
result = bfs(adjacency, start)
print(" ".join(str(x) for x in result))
