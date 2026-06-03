class ProbaIterator:
    def __init__(self, max):
        self.max = max
        self.counter = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.counter < self.max:
            result = self.counter
            self.counter += 1
            return result
        else:
            raise StopIteration
        
szamlalo = ProbaIterator(5)
for i in szamlalo:
    print(i)