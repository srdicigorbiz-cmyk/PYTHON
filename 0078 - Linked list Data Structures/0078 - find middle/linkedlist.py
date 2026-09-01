from node import Node


class LinkedList:

    def __init__(self):
        self.head = None
        self.count = 0

    def addFirst(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node
        self.count += 1

    def addLast(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = node
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

    def remove(self, index):
        if self.head is None or index < 0:
            return
        if index == 0:
            self.head = self.head.next
            self.count -= 1
            return
        prev = self.head
        j = 0
        while prev.next is not None and j < index - 1:
            prev = prev.next
            j += 1
        if prev.next is None:
            return
        prev.next = prev.next.next
        self.count -= 1

    def size(self):
        return self.count
