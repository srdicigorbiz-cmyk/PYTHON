class Parosszamok:
    def __init__(self, num_list):
        self.num_list = num_list
        self.idx=0
        
    def __iter__(self):
        return self
    def __next__(self):
        if self.idx >= len(self.num_list):
            raise StopIteration
        else:
            if self.num_list[self.idx]%2==0:
                result = self.idx
                self.idx += 1
                return self.num_list[result]
            else:
                self.idx += 1
                return self.__next__()

parosszamok = Parosszamok([1,2,3,4,5,6,7,8,10])
for i in parosszamok:
    print(i)