# Read input
start, stop, step = map(int, input().split())

class StepRange:
    def __init__(self, start, stop, step):
        self.start = start
        self.stop = stop
        self.step = step
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        # TODO: Implement the __next__() method
        if self.step > 0:
            if self.current < self.stop:
                result = self.current
                self.current += self.step
                return result
            else:
                raise StopIteration
        else:
            if self.current > self.stop:
                result = self.current
                self.current += self.step
                return result
            else:
                raise StopIteration

# Create an instance of StepRange
step_range = StepRange(start, stop, step)

# TODO: Iterate through the StepRange and print each value
# Remember to print each value on a new line
for i in step_range:
    print(i)