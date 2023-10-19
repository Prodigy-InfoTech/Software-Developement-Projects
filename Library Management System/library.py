class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.checked_out = False

    def __str__(self):
        return f"{self.title} by {self.author}"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, isbn):
        book = Book(title, author, isbn)
        self.books.append(book)

    def list_books(self):
        for i, book in enumerate(self.books, 1):
            status = "Available" if not book.checked_out else "Checked Out"
            print(f"{i}. {book} ({status})")

    def check_out(self, book_index):
        if 1 <= book_index <= len(self.books):
            book = self.books[book_index - 1]
            if not book.checked_out:
                book.checked_out = True
                print(f"You have checked out {book.title}.")
            else:
                print(f"{book.title} is already checked out.")
        else:
            print("Invalid book index.")

    def return_book(self, book_index):
        if 1 <= book_index <= len(self.books):
            book = self.books[book_index - 1]
            if book.checked_out:
                book.checked_out = False
                print(f"Thank you for returning {book.title}.")
            else:
                print(f"{book.title} is not checked out.")
        else:
            print("Invalid book index.")

def main():
    library = Library()

    while True:
        print("\nLibrary Management System")
        print("1. Add a book")
        print("2. List available books")
        print("3. Check out a book")
        print("4. Return a book")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter the title of the book: ")
            author = input("Enter the author of the book: ")
            isbn = input("Enter the ISBN of the book: ")
            library.add_book(title, author, isbn)
            print(f"{title} by {author} has been added to the library.")
        elif choice == "2":
            library.list_books()
        elif choice == "3":
            library.list_books()
            book_index = int(input("Enter the index of the book you want to check out: "))
            library.check_out(book_index)
        elif choice == "4":
            library.list_books()
            book_index = int(input("Enter the index of the book you want to return: "))
            library.return_book(book_index)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
