# Book class
class Book:
    BOOK_TYPES = ['Fiction', 'Non-Fiction', 'Sci-Fi', 'Mystery', 'Biography']

    def __init__(self, title, author, price, quantity, book_type):
        self.title = title
        self.author = author
        self.price = price
        self.quantity = quantity
        self.book_type = book_type

    def getTitle(self):
        return self.title

    def getAuthor(self):
        return self.author

    def getPrice(self):
        return self.price

    def getQuantity(self):
        return self.quantity

    def getType(self):
        return self.book_type

    def setPrice(self, newPrice):
        self.price = newPrice

    def setQuantity(self, newQuantity):
        self.quantity = newQuantity

    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}', price={self.price}, quantity={self.quantity}, type='{self.book_type}')"

    @classmethod
    def create_book(cls, title, author, price, quantity, book_type):
        if book_type not in cls.BOOK_TYPES:
            raise ValueError("Invalid book type")
        return cls(title, author, price, quantity, book_type)


# User class
class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        self.orders = []

    def getUsername(self):
        return self.username

    def getEmail(self):
        return self.email

    def setEmail(self, newEmail):
        self.email = newEmail

    def setPassword(self, newPassword):
        self.password = newPassword

    def __repr__(self):
        return f"User(username='{self.username}', email='{self.email}')"

    def place_order(self, book, quantity):
        order_id = f"ORD{len(self.username)}{len(book.title)}{quantity}"
        order = Order(order_id, self, book, quantity)
        self.orders.append(order)
        print("Order placed successfully!")
        print(order)

    def remove_order(self, order_id):
        for order in self.orders:
            if order.getOrderId() == order_id:
                self.orders.remove(order)
                print("Order removed successfully!")
                return
        print("Order not found.")

    def view_orders(self):
        if self.orders:
            print("\nOrders:")
            for order in self.orders:
                print(order)
        else:
            print("\nNo orders placed yet.")

    def total_order_cost(self):
        total_cost = sum(order.getBook().getPrice() * order.getQuantity() for order in self.orders)
        return total_cost

    def update_email(self, new_email):
        self.email = new_email
        print("Email updated successfully!")

    def update_password(self, new_password):
        self.password = new_password
        print("Password updated successfully!")

    def view_user_info(self):
        print(f"\nUser Information:\nUsername: {self.username}\nEmail: {self.email}")


# Order class
class Order:
    def __init__(self, order_id, user, book, quantity):
        self.order_id = order_id
        self.user = user
        self.book = book
        self.quantity = quantity

    def getOrderId(self):
        return self.order_id

    def getBook(self):
        return self.book

    def getQuantity(self):
        return self.quantity

    def setQuantity(self, newQuantity):
        self.quantity = newQuantity

    def total_price(self):
        return self.book.getPrice() * self.quantity

    def __repr__(self):
        return f"Order(order_id='{self.order_id}', user={self.user}, book={self.book}, quantity={self.quantity}, total_price={self.total_price()})"


# Inventory management system
class Inventory:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def update_book_quantity(self, book_title, new_quantity):
        for book in self.books:
            if book.getTitle() == book_title:
                book.setQuantity(new_quantity)
                print(f"Quantity of {book.getTitle()} updated to {new_quantity}")
                break
        else:
            print("Book not found in inventory.")

    def total_inventory_value(self):
        total_value = sum(book.price * book.quantity for book in self.books)
        return total_value

    def display_inventory(self):
        print("\nInventory:")
        for book in self.books:
            print(book)

    def search_books(self, keyword):
        found_books = []
        for book in self.books:
            if keyword.lower() in book.getTitle().lower() or keyword.lower() in book.getAuthor().lower():
                found_books.append(book)
        return found_books

    def update_book_info(self, book_title, new_price, new_quantity):
        for book in self.books:
            if book.getTitle() == book_title:
                book.setPrice(new_price)
                book.setQuantity(new_quantity)
                print(f"Information for {book.getTitle()} updated successfully.")
                return
        print("Book not found in inventory.")


def main():
    # Create an inventory
    inventory = Inventory()

    # Create some books and users
    book1 = Book.create_book("The Great Gatsby", "F. Scott Fitzgerald", 15.99, 100, "Fiction")
    book2 = Book.create_book("The Da Vinci Code", "Dan Brown", 12.50, 80, "Mystery")
    user1 = User("john_doe", "john@example.com", "password123")
    user2 = User("jane_smith", "jane@example.com", "abc123")

    # Add books to inventory
    inventory.add_book(book1)
    inventory.add_book(book2)

    # Display book and user information
    print("Book Information:")
    print(book1)
    print(book2)

    print("\nUser Information:")
    print(user1)
    print(user2)

    # Place orders
    user1.place_order(book1, 5)
    user2.place_order(book2, 10)

    # Display total inventory value
    print("\nTotal Inventory Value:", inventory.total_inventory_value())

    # View user orders
    user1.view_orders()
    user2.view_orders()

    # Remove an order
    user1.remove_order("ORD8165")

    # Update user information
    user1.update_email("newjohn@example.com")
    user2.update_password("newpassword456")

    # Display inventory
    inventory.display_inventory()

    # Display total order cost for each user
    print("\nTotal Order Cost for", user1.getUsername(), ":", user1.total_order_cost())
    print("Total Order Cost for", user2.getUsername(), ":", user2.total_order_cost())

    # View user information
    user1.view_user_info()

    # Search for books
    keyword = "Scott"
    found_books = inventory.search_books(keyword)
    if found_books:
        print(f"\nBooks containing '{keyword}':")
        for book in found_books:
            print(book)
    else:
        print(f"No books found containing '{keyword}'.")

    # Update book information
    inventory.update_book_info("The Great Gatsby", 17.99, 90)
    inventory.display_inventory()

if __name__ == "__main__":
    main()
