class BubbleSort:
    def sort(self, data):
        return f"Bubble sorted: {sorted(data)}"

class QuickSort:
    def sort(self, data):
        return f"Quick sorted: {sorted(data)}"

class Sorter:
    def __init__(self, strategy):
        self.strategy = strategy
    
    def set_strategy(self, strategy):
        self.strategy = strategy
    
    def sort_data(self, data):
        return self.strategy.sort(data)

# Use different sorting strategies
numbers = [3, 1, 4, 1, 5]

sorter = Sorter(BubbleSort())
print(sorter.sort_data(numbers))

sorter.set_strategy(QuickSort())
print(sorter.sort_data(numbers))
