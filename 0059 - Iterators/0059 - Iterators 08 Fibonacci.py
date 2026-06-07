# Read input
limit = int(input())

class FibonacciIterator:
    def __init__(self, limit):
        self.limit = limit
        self.a, self.b = 0, 1
    def __iter__(self):
        return self
    def __next__(self):
        # TODO: Implement the __next__() method
        # Generate the next Fibonacci number
        # Raise StopIteration when the sequence is exhausted
        
        if self.a > self.limit:
            raise StopIteration
        else:
            result = self.a
            self.a, self.b = self.b, self.a + self.b
            return result
        

# Create an instance of FibonacciIterator
fib_iterator = FibonacciIterator(limit)

# TODO: Iterate through the Fibonacci sequence and print each number
for i in fib_iterator:
    print(i)

# Note: Make sure to print each Fibonacci number to pass the test cases