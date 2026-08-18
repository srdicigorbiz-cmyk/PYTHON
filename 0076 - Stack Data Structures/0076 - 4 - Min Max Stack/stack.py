class Stack:
    def __init__(self):
        self.elements = []
        self.min_stack = []
        self.max_stack = []

    def push(self, element):
        self.elements.append(element)

        if self.max_stack:
            if element > self.max_stack[-1]:
                self.max_stack.append(element)
            else:
                self.max_stack.append(self.max_stack[-1])
        else:
            self.max_stack.append(element)

        if self.min_stack:    
            if element < self.min_stack[-1]:
                self.min_stack.append(element)
            else:
                self.min_stack.append(self.min_stack[-1])
        else:
            self.min_stack.append(element)

    def top(self):
        return self.elements[-1]

    def pop(self):
        self.min_stack.pop()
        self.max_stack.pop()
        return self.elements.pop()

    def size(self):
        return len(self.elements)

    def empty(self):
        return len(self.elements) == 0
    
    def min(self):
        return self.min_stack[-1]

    def max(self):
        return self.max_stack[-1]
