
class Node:
    def __init__(self, pid, name, quantity, price):
        self.pid = pid
        self.name = name
        self.quantity = quantity
        self.price = price
        self.next = None


class Supermarket:
    def __init__(self):
        self.head = None

    # 1. Add Product
    def add_product(self, pid, name, quantity, price):
        new_node = Node(pid, name, quantity, price)

        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

        print("Product added successfully!")

    # 2. Search Product
    def search_product(self, pid):
        temp = self.head

        while temp:
            if temp.pid == pid:
                print("\nProduct Found!")
                print("ID:", temp.pid)
                print("Name:", temp.name)
                print("Quantity:", temp.quantity)
                print("Price:", temp.price)
                return
            temp = temp.next

        print("Product not found!")

    # 3. Update Quantity
    def update_quantity(self, pid, new_quantity):
        temp = self.head

        while temp:
            if temp.pid == pid:
                temp.quantity = new_quantity
                print("Quantity updated successfully!")
                return
            temp = temp.next

        print("Product not found!")

    # 4. Delete Product
    def delete_product(self, pid):
        temp = self.head
        prev = None

        while temp:
            if temp.pid == pid:
                if prev is None:
                    self.head = temp.next
                else:
                    prev.next = temp.next

                print("Product deleted successfully!")
                return

            prev = temp
            temp = temp.next

        print("Product not found!")

    # 5. Display Products
    def display_products(self):
        temp = self.head

        print("\n--- All Products ---")

        while temp:
            print("ID:", temp.pid)
            print("Name:", temp.name)
            print("Quantity:", temp.quantity)
            print("Price:", temp.price)
            print("-------------------")
            temp = temp.next

    # 6. Highest Priced Product
    def highest_price(self):
        if self.head is None:
            print("No products available!")
            return

        temp = self.head
        highest = self.head

        while temp:
            if temp.price > highest.price:
                highest = temp
            temp = temp.next

        print("\n--- Highest Priced Product ---")
        print("ID:", highest.pid)
        print("Name:", highest.name)
        print("Price:", highest.price)

    # 7. Low Stock Products
    def low_quantity(self, limit):
        temp = self.head
        found = False

        print("\n--- Low Stock Products ---")

        while temp:
            if temp.quantity < limit:
                print("ID:", temp.pid)
                print("Name:", temp.name)
                print("Quantity:", temp.quantity)
                print("Price:", temp.price)
                print("low_quantity product is ",temp.quantity)
                found = True

            temp = temp.next

        if not found:
            print("No low stock products!")


# Main Program
s = Supermarket()

# Adding predefined products
s.add_product(101, "Rice", 50, 60)
s.add_product(102, "Oil", 10, 150)
s.add_product(103, "Sugar", 5, 45)
s.add_product(104, "Wheat", 30, 55)

# Display all products
s.display_products()

# Search product
s.search_product(102)

# Update quantity
s.update_quantity(101, 80)

# Delete discontinued product
s.delete_product(103)

# Find highest priced product
s.highest_price()

# Display products below quantity 20
s.low_quantity(20)

# Display final product list
s.display_products()
