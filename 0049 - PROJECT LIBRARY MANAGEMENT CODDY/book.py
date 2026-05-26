class Book:
    def __init__(self, title, author, isbn):
        # TODO: Initialize the Book class with title, author, and isbn parameters
        # TODO: Store title as self.title
        # TODO: Store author as self.author
        # TODO: Store isbn as self.isbn
        # TODO: Set self.available to True by default
        # TODO: Set self.borrower to None by default
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True 
        self.borrower = None

    def __str__(self):
        # TODO: Implement the string representation method
        # TODO: Check if the book is available using self.available
        # TODO: If available, return: "[title] by [author] (ISBN: [isbn]) - Available"
        # TODO: If not available, return: "[title] by [author] (ISBN: [isbn]) - Not Available"
        if self.available:
            return f"{self.title} by {self.author} (ISBN: {self.isbn}) - Available"
        else:
            return f"{self.title} by {self.author} (ISBN: {self.isbn}) - Not Available"