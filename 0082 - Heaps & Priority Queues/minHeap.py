class MinHeap:

    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i-1)//2

    def insert(self, value):
        self.heap.append(value)

        i = len(self.heap)-1

        while i > 0 and self.heap[i] < self.heap[self.parent(i)]:
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)
        
    def peek(self):
        if len(self.heap) ==0:
            return -1
        
        return self.heap[0]

    def extractMin(self):
        if len(self.heap) ==0:
            return -1
        
        if len(self.heap) == 1:
            return self.heap.pop()
        
        min_value = self.heap[0]

        self.heap[0] = self.heap.pop()

        i = 0

        while 2 * i + 1 < len(self.heap):
            smallest = i
            left = 2 * i + 1
            right = 2 * i + 2

            if right < len(self.heap):
                if self.heap[left] < self.heap[right]:
                    if self.heap[smallest] > self.heap[left]:
                        self.heap[smallest], self.heap[left] = self.heap[left], self.heap[smallest]
                        i = left
                    else:
                        return min_value
                elif self.heap[smallest] > self.heap[right]:
                    self.heap[smallest], self.heap[right] = self.heap[right], self.heap[smallest]
                    i = right
                else:
                    return min_value
            else:
                if self.heap[smallest] > self.heap[left]:
                    self.heap[smallest], self.heap[left] = self.heap[left], self.heap[smallest]
                    
                break
        
        return min_value

        
    def size(self):
        return len(self.heap)

    def isEmpty(self):
        if len(self.heap):
            return False
        else:
            return True

mh = MinHeap()

mh.insert(3)
mh.insert(1)
mh.insert(4)
mh.insert(1)
mh.insert(5)
mh.insert(9)
mh.insert(2)
mh.insert(6)

print(mh.heap)
print(mh.size())
print(mh.isEmpty())
print(mh.parent(5))