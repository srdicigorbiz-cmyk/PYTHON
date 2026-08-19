import sys
from circular_queue import CircularQueue

lines = sys.stdin.read().split("\n")
q = CircularQueue(int(lines[0]))
for raw in lines[1:]:
    line = raw.strip()
    if not line:
        continue
    parts = line.split()
    cmd = parts[0]
    if cmd == "enqueue":
        q.enqueue(int(parts[1]))
    if cmd == "dequeue":
        q.dequeue()
    if cmd == "front":
        print(q.front())
    if cmd == "rear":
        print(q.rear())
    if cmd == "size":
        print(q.size())
