class Bookstore:
    def __init__(self):
        self.books = {}

    def add_book(self, title, author, price, quantity):
        if title in self.books:
            print(f"Book '{title}' already exists in the inventory.")
        else:
            self.books[title] = {'author': author, 'price': price, 'quantity': quantity}
            print(f"Added '{title}' by {author} to the inventory.")

    def list_books(self):
        if not self.books:
            print("Inventory is empty.")
        else:
            print("Inventory:")
            for title, details in self.books.items():
                print(f"Title: {title}, Author: {details['author']}, Price: ${details['price']}, Quantity: {details['quantity']}")

    def sell_book(self, title, quantity_to_sell):
        if title not in self.books:
            print(f"Book '{title}' is not in the inventory.")
        elif self.books[title]['quantity'] < quantity_to_sell:
            print(f"Insufficient stock for '{title}'.")
        else:
            self.books[title]['quantity'] -= quantity_to_sell
            print(f"Sold {quantity_to_sell} copies of '{title}'.")

def main():
    bookstore = Bookstore()
    
    while True:
        print("\nOptions:")
        print("1. Add a book")
        print("2. List books")
        print("3. Sell a book")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter author: ")
            price = float(input("Enter price: "))
            quantity = int(input("Enter quantity: "))
            bookstore.add_book(title, author, price, quantity)
        elif choice == '2':
            bookstore.list_books()
        elif choice == '3':
            title = input("Enter book title: ")
            quantity_to_sell = int(input("Enter quantity to sell: "))
            bookstore.sell_book(title, quantity_to_sell)
        elif choice == '4':
            print("Exiting the Bookstore Management System.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
