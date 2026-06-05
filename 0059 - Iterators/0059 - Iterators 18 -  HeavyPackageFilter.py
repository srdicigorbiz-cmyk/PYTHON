class HeavyPackageFilter:
    def __init__(self, packages):
        self.packages = packages
        self.packages_no = list(enumerate(packages, start=1))
        self.idx = 0
    def __iter__(self):
        self.idx = 0
        return self
    def __next__(self):
        while self.idx < len(self.packages_no):
            if self.packages_no[self.idx][1]>20:
                result = self.packages_no[self.idx]
                self.idx += 1
                return result
            else:
                self.idx +=1
                
        raise StopIteration("No more packages")
        
        


packages = [10, 25, 15, 30, 5, 40]
filterpack = HeavyPackageFilter(packages)

for i in filterpack:
    print(i)


# Elvárt eredmény:
# (2, 25)
# (4, 30)
# (6, 40)