from models import Base, Book, Session

def add_book():
    session = Session()
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    price = float(input("Enter book price: "))
    quantity = int(input("Enter quantity: "))

    book = Book(title=title, author=author, price=price, quantity=quantity)
    session.add(book)
    session.commit()
    session.close()
    print("Book added successfully!")

def sell_book():
    session = Session()
    title = input("Enter book title to sell: ")
    quantity_to_sell = int(input("Enter quantity to sell: "))

    book = session.query(Book).filter(Book.title == title).first()
    if book and book.quantity >= quantity_to_sell:
        book.quantity -= quantity_to_sell
        session.commit()
        session.close()
        print("Sale successful!")
    else:
        session.close()
        print("Book not found or insufficient quantity!")

def view_inventory():
    session = Session()
    books = session.query(Book).all()
    session.close()

    if not books:
        print("No books in inventory.")
    else:
        print("\nBook Inventory:")
        for book in books:
            print(f"{book.title} by {book.author} - Price: ${book.price:.2f} - Quantity: {book.quantity}")

if __name__ == '__main__':
    while True:
        print("\nBookstore Management System Menu:")
        print("1. Add Book")
        print("2. Sell Book")
        print("3. View Inventory")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_book()
        elif choice == '2':
            sell_book()
        elif choice == '3':
            view_inventory()
        elif choice == '4':
            print("Exiting the Bookstore Management System.")
            break
        else:
            print("Invalid choice. Please select a valid option.")
