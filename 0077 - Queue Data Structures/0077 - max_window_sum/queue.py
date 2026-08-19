class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        self.items.pop(0)

    def front(self):
        return self.items[0]

    def rear(self):
        return self.items[-1]

    def size(self):
        return len(self.items)
