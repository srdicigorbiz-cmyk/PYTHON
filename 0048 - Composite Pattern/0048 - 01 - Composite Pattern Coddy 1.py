class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size
    
    def get_size(self):
        return self.size
    
    def display(self):
        return f"File: {self.name} ({self.size}KB)"


class Folder:
    def __init__(self, name):
        self.name = name
        self.children = []
    
    def add(self, item):
        self.children.append(item)
    
    def get_size(self):
        total = 0
        for child in self.children:
            total += child.get_size()
        return total
    
    def display(self):
        result = f"Folder: {self.name}"
        for child in self.children:
            result += f"\n  {child.display()}"
        return result
# Create files
file1 = File("document.txt", 10)
file2 = File("image.jpg", 50)
file3 = File("video.mp4", 200)


# Create folders
documents = Folder("Documents")
media = Folder("Media")
root = Folder("Root")


# Build the tree structure
documents.add(file1)
media.add(file2)
media.add(file3)
root.add(documents)
root.add(media)



print(f"Root size: {root.get_size()}KB")
print(root.display())
