from node import Node


class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def addFirst(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.count += 1

    def addLast(self, value):
        node = Node(value)
        if self.tail is None:
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        self.count += 1

    def get(self, index):
        cur = self.head
        i = 0
        while cur is not None:
            if i == index:
                return cur.value
            cur = cur.next
            i += 1
        return -1

    def removeLast(self):
        if self.tail is None:
            return
        if self.count == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.count -= 1

    def size(self):
        return self.count
