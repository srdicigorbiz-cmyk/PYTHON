# Read input
end_letter = input().strip().upper()

class AlphabetIterator:
    def __init__(self, end_letter):
        self.end_letter = end_letter
        self.current_letter = ord('A')


    def __iter__(self):
        return self

    # TODO: Implement the __next__() method
    def __next__(self):
        if self.current_letter > ord(self.end_letter):
            raise StopIteration
        else:
            result = chr(self.current_letter)
            self.current_letter += 1
            return result



# Create an instance of AlphabetIterator
alphabet_iter = AlphabetIterator(end_letter)

# TODO: Iterate through the AlphabetIterator and print each letter
for i in alphabet_iter:
    print(i)
# Note: Make sure to print each letter on a new line