class MinHeap:

    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def insert(self, value):
        self.heap.append(value)
        i = len(self.heap) - 1
        while i > 0:
            p = self.parent(i)
            if self.heap[p] > self.heap[i]:
                self.heap[p], self.heap[i] = self.heap[i], self.heap[p]
                i = p
            else:
                break

    def peek(self):
        if len(self.heap) == 0:
            return -1
        return self.heap[0]

    def extractMin(self):
        if len(self.heap) == 0:
            return -1
        min_val = self.heap[0]
        last = self.heap.pop()
        if len(self.heap) > 0:
            self.heap[0] = last
            i = 0
            n = len(self.heap)
            while True:
                left = 2 * i + 1
                right = 2 * i + 2
                smallest = i
                if left < n and self.heap[left] < self.heap[smallest]:
                    smallest = left
                if right < n and self.heap[right] < self.heap[smallest]:
                    smallest = right
                if smallest == i:
                    break
                self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
                i = smallest
        return min_val

    def size(self):
        return len(self.heap)

    def isEmpty(self):
        return len(self.heap) == 0
