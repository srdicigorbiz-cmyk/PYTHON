# Read input
limit = int(input())

# TODO: Write your code here
# Implement the even number iterator using iter() and next()
class CountUpEven:
    def __init__(self,end):
        self.current = 2
        self.end = int(end)
    def __iter__(self):
        return self
    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        else:
            result=self.current
            self.current += 2
            return result
# Example of how to print the result
# print(next_even_number)
counter = CountUpEven(limit)
iterator_obj = iter(counter)


# 3. LÉPÉS: Addig hívjuk a next()-et és printeljük, amíg el nem fogy
try:
    while True:
        print(next(iterator_obj))
except StopIteration:
    pass