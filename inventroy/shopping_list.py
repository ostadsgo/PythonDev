import os
from enum import Enum
from dataclasses import dataclass
import logging


EXIT_COMMANDS = ["q", "quit", "ex", "exit"]
shopping_list = list()

logging.basicConfig(filename="shop_app.log")


class Menu(Enum):
    add = "add"
    show = "show"
    help = "help"
    remove = "remove"
    search = "search"
    clear = "clear"
    sort_asc = "sort asc"
    sort_dec = "sort dec"


@dataclass
class Product:
    name: str
    price: int
    item_number: int = 1
    total_price: int = 0


def total_price(price: int, item_number: int) -> int:
    return price * item_number


def append_product(product: str):
    try:
        with open("inventory.txt", "a") as file:
            row: str = f"{product.name},{product.item_number},{product.price},{product.total_price}\n"
            file.write(row)
    except FileNotFoundError:
        logging.error("inventory.txt not found!")


def write_products(products: list[Product]):
    try:
        with open("inventory.txt", "w") as file:
            for product in products:
                file.write(product)
    except FileNotFoundError:
        logging.error("inventory.txt not found!")


def read_products():
    with open("inventory.txt", "r") as file:
        content: list[Product] = file.readlines()
        return content


def add_product(name: str, price: int, item_number: int):
    products = read_products()
    for product in products:
        p_name, *rest = product.split(",")
        if p_name == name:
            print("Item is already in the shop.")
            return None
    product = Product(name, price, item_number, total_price(price, item_number))
    append_product(product)


def show_products():
    products: list[Product] = read_products()
    print(f"{'Product Name':20}{'Quantity':10}Price\tTotal Price")
    print("-" * 50)
    item_numbers: int = 0
    for product in products:
        name, number, price, total_price = product.split(",")
        print(f"{name:20}{number:10}${price}\t${total_price}", end="")
        item_numbers += int(number)
    print(f"All items number are: {item_numbers}")


def remove_product(item: str):
    products: list[Product] = read_products()
    for product in products.copy():
        name, *rest = product.split(",")
        if name == item:
            products.remove(product)
            print(f"{item} delete successfuly.")
            break
    else:
        print("item that you are trying to remove is not in the list")

    write_products(products)


def search_product(product_name: str):
    products: list[Product] = read_products()
    for product in products:
        name, *rest = product.split(",")
        if product_name == name:
            print(product)
            break
    else:
        print(f"{product_name} not found")


def show_help():
    print("enter, `QUIT` to exit the app and see your list")
    print("enter, `HELP` to see help")


def sort_product_ascending():
    products: list[Product] = read_products()
    sorted_products: list[Product] = sorted(products)
    print(f"{'Product Name':20}{'Quantity':10}Price\tTotal Price")
    print("-" * 50)
    for product in sorted_products:
        name, number, price, total_price = product.split(",")
        print(f"{name:20}{number:10}${price}\t${total_price}", end="")


def sort_product_descending():
    products: list[Product] = read_products()
    sorted_products: list[Product] = sorted(products, reverse=True)
    print(f"{'Product Name':20}{'Quantity':10}Price\tTotal Price")
    print("-" * 50)
    for product in sorted_products:
        name, number, price, total_price = product.split(",")
        print(f"{name:20}{number:10}${price}\t${total_price}", end="")


def clear_screen():
    return os.system("CLS")


while True:
    clear_screen()
    app_logo = """
    *******************
    ** SHOPPING_LIST **
    *******************
    """
    print(app_logo)
    print("Menu items: ")
    print("-" * 30)
    items = ""
    for shopping in Menu:
        items += " - " + shopping.value + "\n"
    print(items)
    item = input("> ")
    if item in EXIT_COMMANDS:
        break
    elif item == Menu.add.value:
        # name = input("Enter product name:")
        try:
            name = input("Enter product name:").lower()
            item_number = int(input("Enter item number: "))
            price = int(input("Enter price of the product: "))
            add_product(name, price, item_number)
        except ValueError:
            print("Error, please enter a valid number.")
            logging.error("wrong value for item_number.")
    elif item == Menu.show.value:
        show_products()
    elif item == Menu.help.value:
        show_help()
    elif item == Menu.remove.value:
        item_to_remove = input("please enter the item that you want to remove:")
        remove_product(item_to_remove)
    elif item == Menu.search.value:
        item_to_search = input("please enter the item that you want to search:").lower()
        search_product(item_to_search)
    elif item == Menu.clear.value:
        clear_screen()
    elif item == Menu.sort_asc.value:
        sort_product_ascending()
    elif item == Menu.sort_dec.value:
        sort_product_descending()
    else:
        print("Wrong choice!!")
        logging.info("user choosed wrong option", item)

    input("\nPress Enter key to continue ....")
