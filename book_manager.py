from data_handler import load_data, save_data
from typing import List, Dict, Optional, Any

class BookManager:
    """
    Manages the library's book collection with CRUD operations.
    
    Handles adding, removing, borrowing, and returning books.
    Maintains book data in a JSON file using data_handler utilities.
    """
    
    def __init__(self, data_file: str = "books.json") -> None:
        """
        Initialize the book manager with data from a JSON file.
        
        Args:
            data_file: Path to the JSON file storing book data
        """
        self.data_file = data_file  # Store the data file path
        # Load existing books from file or start with empty list
        self.books: List[Dict[str, Any]] = load_data(data_file)
    
    def add_book(self, title: str, author: str, isbn: str) -> str:
        """
        Add a new book to the library collection.
        
        Validates input, checks for duplicate ISBN, and saves the new book.
        
        Args:
            title: Title of the book
            author: Author of the book
            isbn: Unique ISBN identifier (10 or 13 digits)
            
        Returns:
            Success message or error message if validation fails
        """
        # Validate required fields
        if not title or not author or not isbn:
            return "Error: All fields (title, author, ISBN) are required."
        
        # Check for duplicate ISBN
        if any(book['isbn'] == isbn for book in self.books):
            return f"Error: Book with ISBN {isbn} already exists."
        
        # Create new book dictionary
        new_book = {
            'title': title,        # Book title
            'author': author,      # Book author
            'isbn': isbn,          # Unique ISBN identifier
            'available': True      # Default availability status
        }
        
        # Add to collection and save
        self.books.append(new_book)
        save_data(self.data_file, self.books)
        return f"✅ Added '{title}' by {author} to the library."
    
    def remove_book(self, isbn: str) -> str:
        """
        Remove a book from the library by ISBN.
        
        Args:
            isbn: ISBN of the book to remove
            
        Returns:
            Success message or error if book not found
        """
        # Search for book by ISBN
        for i, book in enumerate(self.books):
            if book['isbn'] == isbn:
                # Remove book from collection
                removed = self.books.pop(i)
                # Persist changes to file
                save_data(self.data_file, self.books)
                return f"✅ Removed '{removed['title']}' by {removed['author']}."
        return f"⚠️ Error: No book found with ISBN {isbn}."
    
    def borrow_book(self, isbn: str) -> str:
        """
        Borrow a book by marking it as unavailable.
        
        Args:
            isbn: ISBN of the book to borrow
            
        Returns:
            Success message or error if book not found/already borrowed
        """
        # Find book by ISBN
        for book in self.books:
            if book['isbn'] == isbn:
                if book['available']:
                    # Mark as borrowed and save
                    book['available'] = False
                    save_data(self.data_file, self.books)
                    return f"✅ Borrowed '{book['title']}'."
                else:
                    return f"⚠️ Error: '{book['title']}' is already borrowed."
        return f"⚠️ Error: No book found with ISBN {isbn}."
    
    def return_book(self, isbn: str) -> str:
        """
        Return a borrowed book by marking it as available.
        
        Args:
            isbn: ISBN of the book to return
            
        Returns:
            Success message or error if book not found/not borrowed
        """
        # Find book by ISBN
        for book in self.books:
            if book['isbn'] == isbn:
                if not book['available']:
                    # Mark as returned and save
                    book['available'] = True
                    save_data(self.data_file, self.books)
                    return f"✅ Returned '{book['title']}'."
                else:
                    return f"⚠️ Error: '{book['title']}' was not borrowed."
        return f"⚠️ Error: No book found with ISBN {isbn}."
    
    def search_books(self, search_term: str) -> List[Dict[str, Any]]:
        """
        Search books by title, author, or ISBN (case-insensitive).
        
        Args:
            search_term: String to search in book attributes
            
        Returns:
            List of matching books or empty list if no matches
        """
        if not search_term:
            return []  # Empty search term returns no results
            
        search_term = search_term.lower()  # Case-insensitive search
        
        # Search in title, author, and ISBN fields
        return [book for book in self.books 
                if search_term in book['title'].lower() 
                or search_term in book['author'].lower()
                or search_term in book['isbn'].lower()]
    
    def list_books(self) -> List[Dict[str, Any]]:
        """
        Get all books in the library.
        
        Returns:
            Complete list of books in the collection
        """
        return self.books
