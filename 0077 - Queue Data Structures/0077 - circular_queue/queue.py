class CircularQueue:
    def __init__(self, size):
        self.items = []
        self.max_size = size

    def enqueue(self, item):
        # Write code here
        if len(self.items) >= self.max_size:
            self.items.pop(0)    
            self.items.append(item)
        else:
            self.items.append(item)

    def dequeue(self):
        self.items.pop(0)

    def front(self):
        return self.items[0]

    def rear(self):
        return self.items[-1]

    def size(self):
        return len(self.items)
