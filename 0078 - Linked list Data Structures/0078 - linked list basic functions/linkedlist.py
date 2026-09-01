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

    def get(self, value):
        if value < 0 or value >= self.count:
            return -1
        else:
            current = self.head
            for n in range(value):
                current = current.next
            return current.getValue()
    
    def remove(self, index):
        
        current = self.head

        if not 0 <= index < self.count:
            return
        else:
            if index == 0:
                self.head = current.next
            else:
                for n in range(index-1):
                    current = current.next
                current.next = current.next.next
            self.count -= 1

    def size(self):
        counter = 0
        current = self.head
        while current is not None:
            current = current.next
            counter += 1    
        return counter


            
