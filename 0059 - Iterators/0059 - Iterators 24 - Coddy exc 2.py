# Read input
colors = input().split(',')
num_colors = int(input())
class ColorCycler:
    def __init__(self, colors):
        # TODO: Initialize the ColorCycler
        self.colors = colors
        self.startidx = 0

    def __iter__(self):
        # TODO: Implement __iter__ method
        return self

    def __next__(self):
        # TODO: Implement __next__ method
        if self.startidx < len(self.colors):
            result = self.colors[self.startidx]
            self.startidx += 1
            return result
        else:
            self.startidx = 0
            result = self.colors[self.startidx]
            self.startidx += 1
            return result

# TODO: Create a ColorCycler instance with the input colors
colorcycler = ColorCycler(colors)
counter = 0

# TODO: Generate and print the specified number of colors
while True:
    print(next(colorcycler))
    counter += 1
    if counter >= num_colors:
        break
# Note: Remember to print each color on a new line



# test
# red,green,blue
# 5