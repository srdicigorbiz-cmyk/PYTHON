# Read input
limit = int(input())

class PrimeNumberFilter:
    def __init__(self, limit):
        self.limit = limit
        self.current = 2

    def __iter__(self):
        return self

    def __next__(self):
        # TODO: Implement the __next__ method to generate the next prime number
        while self.current <= self.limit:
            result = self.current 
            self.current += 1
            if self.is_prime(result):
                return result
        raise StopIteration
            

    def is_prime(self, n):
        # TODO: Implement the is_prime method to check if a number is prime
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

# Create an instance of PrimeNumberFilter
prime_filter = PrimeNumberFilter(limit)

# TODO: Iterate through the prime numbers and print each one
# Remember to handle the StopIteration exception
for i in prime_filter:
    print(i)
# Note: Make sure to print each prime number on a new line