class FlattenIterator:
    def __init__(self, nested_list):
        self.nested_list = nested_list
        self.innerid = 0
        self.outerid = 0

    def __iter__(self):
        self.outerid = 0
        self.innerid = 0
        return self
    def __next__(self):
        while self.outerid < len(self.nested_list):
             if self.innerid<len(self.nested_list[self.outerid]):
                 result = self.nested_list[self.outerid][self.innerid]
                 self.innerid += 1
                 return result
             else:
                 self.innerid = 0
                 self.outerid += 1
        raise StopIteration


nested_list = [[1, 2], [3], [4, 5]]
flat_iter = FlattenIterator(nested_list)

for num in flat_iter:
    print(num, end=" ")
# Elvárt eredmény: 1 2 3 4 5 

print("\n--- Második kör ---")
for num in flat_iter:
    print(num, end=" ")
# Elvárt eredmény: 1 2 3 4 5