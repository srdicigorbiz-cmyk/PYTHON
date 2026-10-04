import sys
from solution import countConnectedComponents

data = sys.stdin.read().split("\n")
h = data[0].split()
n = int(h[0]); m = int(h[1])
vertices = [int(x) for x in data[1].split()] if data[1].strip() else []
adjacency = []
for i in range(m):
    parts = data[2 + i].split()
    adjacency.append([int(parts[0]), int(parts[1])])
print(countConnectedComponents(adjacency, vertices))
