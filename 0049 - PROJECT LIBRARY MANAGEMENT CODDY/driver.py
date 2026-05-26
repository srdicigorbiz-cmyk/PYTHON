from book import Book
from user import User
from library import Library

# Test case handler
test_case = input()

if test_case == "create_user":
    user_id = "1"
    name = "Name"
    
    user = User(user_id, name)
    print(user)
    print(f"Books borrowed: {len(user.books_borrowed)}")

elif test_case == "borrow_and_return_all":
    library = Library("Community Library")
    
    # Add books and users
    library.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald", "123456"))
    library.add_book(Book("To Kill a Mockingbird", "Harper Lee", "789012"))
    library.add_book(Book("1984", "George Orwell", "345678"))
    
    user = User("U001", "Alice")
    library.add_user(user)
    
    # Borrow books
    library.borrow_book("123456", "U001")
    library.borrow_book("789012", "U001")
    library.borrow_book("345678", "U001")
    
    print(f"Books borrowed before: {len(user.books_borrowed)}")
    
    # Return all books
    num_returned = user.return_all_books(library)
    
    print(f"Books returned: {num_returned}")
    print(f"Books borrowed after: {len(user.books_borrowed)}")
    
    # Check if all books are available
    for book in library.books:
        print(f"Book {book.isbn} available: {book.available}")

elif test_case == "return_some_books":
    library = Library("Community Library")
    
    # Add books and users
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "123456")
    book2 = Book("To Kill a Mockingbird", "Harper Lee", "789012")
    library.add_book(book1)
    library.add_book(book2)
    
    user = User("U001", "Alice")
    library.add_user(user)
    
    # Borrow only one book
    library.borrow_book("123456", "U001")
    
    print(f"Books borrowed before: {len(user.books_borrowed)}")
    
    # Return all books
    num_returned = user.return_all_books(library)
    
    print(f"Books returned: {num_returned}")
    print(f"Books borrowed after: {len(user.books_borrowed)}")

elif test_case == "empty_return":
    library = Library("Community Library")
    
    user = User("U001", "Alice")
    library.add_user(user)
    
    print(f"Books borrowed: {len(user.books_borrowed)}")
    
    # Return all books (should be 0)
    num_returned = user.return_all_books(library)
    
    print(f"Books returned: {num_returned}")

elif test_case == "multiple_users":
    library = Library("Community Library")
    
    # Add books
    library.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald", "123456"))
    library.add_book(Book("To Kill a Mockingbird", "Harper Lee", "789012"))
    
    # Add users
    user1 = User("U001", "Alice")
    user2 = User("U002", "Bob")
    library.add_user(user1)
    library.add_user(user2)
    
    # Borrow books
    library.borrow_book("123456", "U001")
    library.borrow_book("789012", "U002")
    
    print(user1)
    print(user2)
    
    # Return all books for user1
    num_returned = user1.return_all_books(library)
    
    print(f"Books returned by {user1.name}: {num_returned}")
    
    print(user1)
    print(user2)

elif test_case == "error_handling":
    library = Library("Community Library")
    
    # Add book and user
    library.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald", "123456"))
    user = User("U001", "Alice")
    library.add_user(user)
    
    # Try to borrow non-existent book
    result = library.borrow_book("999999", "U001")
    print(result)
    
    # Try to borrow for non-existent user
    result = library.borrow_book("123456", "U999")
    print(result)
    
    # Borrow existing book
    result = library.borrow_book("123456", "U001")
    print(result)
    
    # Try to borrow same book again
    result = library.borrow_book("123456", "U001")
    print(result)
    
    # Try to return a book that wasn't borrowed
    result = library.return_book("789012", "U001")
    print(result)

elif test_case == "stress_test":
    library = Library("Community Library")
    
    user = User("U001", "Alice")
    library.add_user(user)
    
    # Add 100 books
    for i in range(1, 101):
        isbn = f"{i:03d}"  # Format as 001, 002, etc.
        library.add_book(Book(f"Book {i}", f"Author {i}", isbn))
        library.borrow_book(isbn, "U001")
    
    print(f"Books borrowed: {len(user.books_borrowed)}")
    
    # Return all books
    num_returned = user.return_all_books(library)
    
    print(f"Books returned: {num_returned}")
    print(f"Books borrowed after: {len(user.books_borrowed)}")