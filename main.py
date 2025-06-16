from book_manager import BookManager

def display_menu():
    """
    Display the main menu of the Library Management System.
    
    Shows all available operations with corresponding numbers.
    """
    print("\n📚 Library Management System")
    print("1. Add Book")          # Add a new book to the library
    print("2. Remove Book")       # Remove a book by ISBN
    print("3. Borrow Book")       # Borrow a book (mark as unavailable)
    print("4. Return Book")       # Return a borrowed book (mark as available)
    print("5. List All Books")    # Show all books in the library
    print("6. Search Books")      # Search books by title, author, or ISBN
    print("7. Exit")              # Quit the application

def display_book(book):
    """
    Display details of a single book in a consistent format.
    
    Args:
        book: Dictionary containing book information
    """
    # Determine availability status with emoji
    status = "✅ Available" if book['available'] else "❌ Borrowed"
    
    # Print book details
    print(f"Title: {book['title']}")    # Book title
    print(f"Author: {book['author']}")  # Book author
    print(f"ISBN: {book['isbn']}")      # Unique ISBN identifier
    print(f"Status: {status}")          # Current availability status
    print("-" * 30)                     # Separator line

def main():
    """
    Main function that runs the Library Management System.
    
    Initializes the BookManager and handles user input.
    """
    # Create BookManager instance (loads data automatically)
    manager = BookManager()
    
    # Main application loop
    while True:
        # Show menu options
        display_menu()
        
        # Get user choice
        choice = input("\nEnter your choice (1-7): ")
        
        # Add a new book
        if choice == '1':
            print("\n➕ Add New Book")
            title = input("Title: ")   # Get book title
            author = input("Author: ") # Get author name
            isbn = input("ISBN: ")     # Get ISBN
            # Add book and show result
            result = manager.add_book(title, author, isbn)
            print(f"\n{result}")
        
        # Remove a book by ISBN
        elif choice == '2':
            print("\n➖ Remove Book")
            isbn = input("Enter ISBN of book to remove: ")
            # Remove book and show result
            result = manager.remove_book(isbn)
            print(f"\n{result}")
        
        # Borrow a book
        elif choice == '3':
            print("\n📥 Borrow Book")
            isbn = input("Enter ISBN of book to borrow: ")
            # Borrow book and show result
            result = manager.borrow_book(isbn)
            print(f"\n{result}")
        
        # Return a borrowed book
        elif choice == '4':
            print("\n📤 Return Book")
            isbn = input("Enter ISBN of book to return: ")
            # Return book and show result
            result = manager.return_book(isbn)
            print(f"\n{result}")
        
        # List all books
        elif choice == '5':
            print("\n📖 All Books in Library")
            books = manager.list_books()
            if not books:
                print("No books in the library.")
            else:
                # Display each book
                for book in books:
                    display_book(book)
        
        # Search books
        elif choice == '6':
            print("\n🔍 Search Books")
            search_term = input("Enter title, author, or ISBN to search: ")
            results = manager.search_books(search_term)
            if not results:
                print("No matching books found.")
            else:
                print(f"\nFound {len(results)} matching book(s):")
                for book in results:
                    display_book(book)
        
        # Exit the application
        elif choice == '7':
            print("\n👋 Exiting Library Management System. Goodbye!")
            break
        
        # Handle invalid input
        else:
            print("⚠️ Invalid choice. Please enter a number between 1-7.")
