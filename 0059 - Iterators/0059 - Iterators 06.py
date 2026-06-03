class SzuroIterator:
    def __init__(self, termekek):
        self.termekek = termekek
        self.idx = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.idx >= len(self.termekek):
            raise StopIteration
        else:
            if self.termekek[self.idx]["ar"] < 200:
                result = self.termekek[self.idx]["nev"]
                self.idx += 1
                return result
            else:
                self.idx += 1
                return self.__next__()

termekek = [
    {"nev": "alma", "ar": 150},
    {"nev": "laptop", "ar": 350000},
    {"nev": "kenyér", "ar": 180},
    {"nev": "telefon", "ar": 120000},
    {"nev": "tej", "ar": 190},
    {"nev": "monitor", "ar": 85000},
]
szuro = SzuroIterator(termekek)
for i in szuro:
    print(i)