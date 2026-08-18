class Stack:
    def __init__(self):
        self.elements = []

    def push(self, element):
        self.elements.append(element)

    def top(self):
        return self.elements[-1]

    def pop(self):
        return self.elements.pop()

    def size(self):
        return len(self.elements)

    def empty(self):
        return len(self.elements) == 0
