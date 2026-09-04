import sys
from doublylinkedlist import DoublyLinkedList

ll = DoublyLinkedList()
for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    parts = line.split()
    cmd = parts[0]
    if cmd == "state":
        print(("true" if ll.head is None else "false") + " " + ("true" if ll.tail is None else "false") + " " + str(ll.count))
    if cmd == "count":
        print(ll.count)
    if cmd == "headValue":
        print(ll.head.getValue())
    if cmd == "tailValue":
        print(ll.tail.getValue())
    if cmd == "addFirst":
        ll.addFirst(int(parts[1]))
    if cmd == "addLast":
        ll.addLast(int(parts[1]))
    if cmd == "get":
        print(ll.get(int(parts[1])))
    if cmd == "removeLast":
        ll.removeLast()
    if cmd == "size":
        print(ll.size())
