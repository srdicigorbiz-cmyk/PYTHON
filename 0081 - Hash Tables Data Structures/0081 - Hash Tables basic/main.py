import sys
from hashmap import HashMap

h = HashMap()
for raw in sys.stdin.read().split("\n"):
    line = raw.strip()
    if not line:
        continue
    parts = line.split()
    cmd = parts[0]
    if cmd == "state":
        print("%d %d %d" % (h.capacity, len(h.buckets), h.count))
    if cmd == "hash":
        print(h.hash(int(parts[1])))
    if cmd == "put":
        h.put(int(parts[1]), int(parts[2]))
    if cmd == "bucketSize":
        print(len(h.buckets[int(parts[1])]))
    if cmd == "count":
        print(h.count)
