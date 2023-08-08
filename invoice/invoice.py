from datetime import datetime


class FileOperation:
    def __init__(self, filename):
        self.filename = filename

    def readall(self):
        content = []
        try:
            with open(self.filename) as f:
                content = f.readlines()
        except FileNotFoundError:
            print(f"The {self.filename} doesn't exist.")
        return content

    def write(self, text):
        content = self.readall()
        content.append(f"{text}\n")

        # write content to the file
        with open(self.filename, "w") as f:
            for row in content:
                f.write(row)
        return True


class Customer:
    def __init__(self, name):
        self.name = name
        self.customer_file = FileOperation("customers.txt")

    def __str__(self):
        return f"{self.name}"

    def save(self):
        if self.customer_file.write(self.name):
            return True
        return False

    def all_customers(self):
        customers = self.customer_file.readall()
        return customers

    def display(self):
        customers = self.all_customers()
        for customer in customers:
            print(customer, end="")


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.product_file = FileOperation("products.txt")

    def save(self):
        if self.product_file.write(f"{self.name}:{self.price}"):
            return True
        return False

    def all_products(self):
        products = self.product_file.readall()
        return products

    def display(self):
        products = self.all_products()
        for index, product in enumerate(products, 1):
            print(f"{index}. {product.strip()}")

    def make_product(self, text):
        name, price = text.strip().split(":")
        return Product(name, int(price))

    def __str__(self):
        return f"{self.name}, ${self.price}"


class Invoice:
    def __init__(self, customer):
        self.customer = customer
        self.line_items = []
        self.invoice_filename = datetime.now().strftime("%Y-%m-%d %H:%M:%S") + '.txt'

    def add_line_item(self, product, quntity):
        item_total = product.price * quntity
        line_item = [product.name, product.price, quntity, item_total]
        self.line_items.append(line_item)

    def save(self):
        invoice_file = FileOperation(self.invoice_filename)
        for line_item in self.line_items:
            invoice_file.write(line_item)


def menu():
    items = [
        "Add new customer",
        "Display all customers",
        "Add new product",
        "Display all products",
        "Create a invoice",
        "Exit",
    ]

    for index, item in enumerate(items, 1):
        print(f"[{index}] {item}")

    choice = input("Choice from menu: ")
    return choice


def run():
    running = True
    while running:
        choice = menu()
        if choice == "1":
            customer_name = input("Enter customer name: ")
            c = Customer(customer_name)
            save_result = c.save()
            if save_result:
                print("Customer saved.")
            else:
                print("Some problem happend during customer saving")
        elif choice == "2":
            c = Customer("")
            c.display()
        elif choice == "3":
            product_name = input("Enter the product name: ")
            product_price = input("Enter the product price: ")
            p = Product(product_name, product_price)
            save_result = p.save()
            if save_result:
                print("Product saved.")
            else:
                print("Some problem happend during product saving")
        elif choice == "4":
            p = Product("", 0)
            p.display()
        elif choice == "5":
            p = Product("", 0)
            customer_name = input("Enter customer name: ")
            c = Customer(customer_name)
            c.save()
            invoice = Invoice(c)

            products = p.all_products()
            q = "y"
            while q == "y":
                p.display()
                line_item_index = input("Choose line item: ")
                line_item_text = products[int(line_item_index) - 1]
                quntity = int(input("Enter quntity of the product: "))
                line_item = p.make_product(line_item_text)
                invoice.add_line_item(line_item, quntity)
                q = input("Do you want add more line item? (y/n)").lower()
            # save invoice after getting line items
            invoice.save()

        elif choice == "6":
            running = False
        else:
            print("Wrong choice!")


run()
