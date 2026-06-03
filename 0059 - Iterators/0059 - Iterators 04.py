class Visszaszamlalo:
    def __init__(self, num):
        self.num = num
        
    def __iter__(self):
        return self
    def __next__(self):
        if self.num < 0:
            raise StopIteration
        else:
            result = self.num
            self.num -= 1
            return result

visszaszamlalo = Visszaszamlalo(5)

for i in visszaszamlalo:
    print(i)