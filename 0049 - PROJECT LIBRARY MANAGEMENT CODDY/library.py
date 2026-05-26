from book import Book
from user import User

class Library:
    def __init__(self, name):
        # TODO: Initialize the Library class with the given name parameter
        # TODO: Store the name parameter as an instance attribute called 'name'
        # TODO: Initialize an empty list called 'books' as an instance attribute
        # TODO: Initialize an empty list called 'users' as an instance attribute
        self.name = name
        self.books = []
        self.users = []
    
    def add_book(self, book):
        self.books.append(book)
    
    def add_user(self, user):
        self.users.append(user)
    
    # TODO: Implement the borrow_book method that takes book_isbn and user_id parameters
    def borrow_book(self, book_isbn, user_id):
        # TODO: Find the book with matching ISBN using next() and generator expression
        # Hint: book = next((book for book in self.books if book.isbn == book_isbn), None)
        book = next((book for book in self.books if book.isbn == book_isbn), None)
        
        # TODO: Find the user with matching user_id using next() and generator expression
        # Hint: user = next((user for user in self.users if user.user_id == user_id), None)
        user = next((user for user in self.users if user.user_id == user_id), None)
        # TODO: Check if book exists, if not return "Book not found"
        if book == None:
            return "Book not found"
        
        # TODO: Check if user exists, if not return "User not found"
        if user == None:
            return "User not found"
        
        # TODO: Check if book is available, if not return "Book is not available"
        if book.available == False:
            return "Book is not available"
        # TODO: Update book's available status to False
        book.available = False
        # TODO: Set book's borrower to the user
        book.borrower = user
        # TODO: Add the book to user's books_borrowed list
        user.books_borrowed.append(book)
        # TODO: Return "Book borrowed successfully"
        return "Book borrowed successfully"
    
    def search_by_title(self, title):
    # TODO: Implement the search_by_title method that:
    # 1. Takes a title parameter (string to search for in book titles)
    # 2. Returns a list of all books whose titles contain the search term
    # 3. The search should be case-insensitive (e.g., "GREAT" matches "Great")
    # 4. The search should match partial titles (e.g., "great" matches "The Great Gatsby")
    # 5. Use a list comprehension to filter the books
    # 6. Convert both the search term and book titles to lowercase for comparison   
        return [book for book in self.books if title.lower() in book.title.lower()]

 # TODO: Implement the get_statistics method that returns a dictionary with the following statistics:
    # - "total_books": the total number of books in the library
    # - "available_books": the number of books that are available for borrowing
    # - "borrowed_books": the number of books that are currently borrowed
    # - "total_users": the total number of users in the library
    # - "users_with_books": the number of users who have borrowed at least one book
    def get_statistics(self):
        # TODO: Calculate total_books as the length of the books list
        # TODO: Calculate available_books by counting books where available is True
        # TODO: Calculate borrowed_books as total_books minus available_books
        # TODO: Calculate total_users as the length of the users list
        # TODO: Calculate users_with_books by counting users with non-empty books_borrowed list
        # TODO: Return a dictionary with all these statistics
        total_books = len(self.books)
        available_books = len([book for book in self.books if book.available == True])
        borrowed_books = len([book for book in self.books if book.available == False])
        total_users =len(self.users)
        users_with_books = len([user for user in self.users if len(user.books_borrowed)>0])

        return {
                "total_books": total_books, 
                "available_books": available_books,
                "borrowed_books":borrowed_books,
                "total_users": total_users,
                "users_with_books": users_with_books
                      }





    def __str__(self):
        # TODO: Implement the string representation method
        # TODO: Return a formatted string that includes:
        #       - The library name
        #       - The number of books (use len(self.books))
        #       - The number of users (use len(self.users))
        # TODO: Format should be: "[name] Library with [number of books] books and [number of users] users"
        return f"{self.name} Library with {len(self.books)} books and {len(self.users)} users"