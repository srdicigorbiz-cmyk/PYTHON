# Read input
limit = int(input())

class PrimeIterator:
    def __init__(self, limit):
        self.limit = limit
        self.current = 2

    def __iter__(self):
        return self

    def __next__(self):
        def is_prime(n):
            if n < 2:
                return False
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    return False
            return True

        while self.current <= self.limit:
            if is_prime(self.current):
                prime = self.current
                self.current += 1
                return prime
            self.current += 1
        
        raise StopIteration

# Create an instance of PrimeIterator
prime_iter = PrimeIterator(limit)

# Iterate through the prime numbers and print each one
try:
    for prime in prime_iter:
        print(prime)
except StopIteration:
    pass  # End of iteration