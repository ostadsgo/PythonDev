import os
import tomllib
import logging
from enum import Enum
from dataclasses import dataclass


class Menu(Enum):
    """ """

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
    """ """

    FILENAME = "inventory.txt"

    def __init__(self, name: str, item_number=0, price=0):
        self.name = name
        self.item_number = item_number
        self.price = price
        self.total_price = self.item_number * self.price

    def get_total_price(self) -> int:
        """ """
        self.total_price = self.price * self.item_number
        return self.total_price

    def append_product(self):
        """ """
        with open(self.FILENAME, "a") as file:
            row = f"{self.name},{self.item_number},{self.price},{self.get_total_price()}\n"
            file.write(row)

    @staticmethod
    def write_products(products: list[str]):
        """

        Parameters
        ----------
        products: list[str] :


        Returns
        -------

        """
        with open(Product.FILENAME, "w") as file:
            for product in products:
                file.write(product + "\n")

    @staticmethod
    def read_products() -> str:
        """ """
        try:
            with open(Product.FILENAME, "r") as file:
                content: list[str] = file.read().strip().split("\n")
                return content
        except FileNotFoundError:
            print("The file inventory.txt is not exit")
            # if inventory.txt is not exist, the codes blow are going to create one.
            with open(Product.FILENAME, "w") as file:
                file.write("")
            return ""

    def is_product_exist(self) -> bool:
        """ """
        products: list[str] = Product.read_products()
        for product in products:
            p_name, *rest = product.split(",")
            if p_name == self.name:
                return True
        return False

    def add_product(self):
        """ """
        if self.is_product_exist():
            print("Product is already exists.")
            return None

        self.append_product()

    @staticmethod
    def show(products: list[str]):
        """

        Parameters
        ----------
        products: list[str] :


        Returns
        -------

        """
        print(f"{'Product Name':20}{'Quantity':10}Price\tTotal Price")
        print("-" * 50)
        item_numbers = 0
        for product in products:
            name, number, price, total_price = product.split(",")
            print(f"{name:20}{number:10}${price}\t${total_price}")
            item_numbers += int(number)
        print(f"All items number are: {item_numbers}")

    @staticmethod
    def show_products():
        """ """
        products: list[str] = Product.read_products()
        Product.show(products)

    def search_product(self):
        """ """
        products: list[str] = Product.read_products()
        for product in products:
            name, *rest = product.split(",")
            if name == self.name:
                print(product)
                break
        else:
            print(f"{self.name} not found")

    def remove_product(self):
        """ """
        products: list[str] = Product.read_products()
        for product in products.copy():
            name, *rest = product.split(",")
            if name == self.name:
                products.remove(product)
                print(f"{self.name} delete successfully.")
                break
        else:
            print("item that you are trying to remove is not in the list")

        Product.write_products(products)

    @staticmethod
    def show_help():
        """ """
        print("enter, `QUIT` to exit the app and see your list")
        print("enter, `HELP` to see help")

    @staticmethod
    def sort_product_ascending():
        """ """
        products: list[str] = Product.read_products()
        sorted_products: list[Product] = sorted(products)
        Product.show(sorted_products)

    @staticmethod
    def sort_product_descending():
        """ """
        products: list[str] = Product.read_products()
        sorted_products: list[Product] = sorted(products, reverse=True)
        Product.show(sorted_products)


class User:
    """ """

    @staticmethod
    def read_config():
        """ """
        with open("config.toml", "rb") as toml_file:
            config = tomllib.load(toml_file)
        return config

    @staticmethod
    def check_passwd(
        admin_username, admin_password, username: str, password: str
    ) -> bool:
        """

        Parameters
        ----------
        admin_username :

        admin_password :

        username: str :

        password: str :


        Returns
        -------

        """
        if username == admin_username and password == admin_password:
            return True
        return False

    @staticmethod
    def authorization() -> bool:
        """ """
        config = User.read_config()
        admin_username = config["username"]
        admin_password = config["password"]
        for i in range(3):
            username = input("Username: ")
            password = input("Password: ")
            if User.check_passwd(admin_username, admin_password, username, password):
                return True
            return False


class Ui:
    """ """

    @staticmethod
    def clear_screen():
        """ """
        return os.system("cls")

    @staticmethod
    def show_logo():
        """

        Parameters
        ----------

        Returns
        -------
        type
            *******************
            ** SHOPPING_LIST **
            *******************

        """

    @staticmethod
    def show_menu():
        """ """
        print("Menu items: ")
        print("-" * 30)
        items = ""
        for menu_item in Menu:
            items += f" -  {menu_item.value}\n"
        return items

    @staticmethod
    def add_product_ui():
        """ """
        try:
            name = input("Enter product name:").lower()
            item_number = int(input("Enter item number: "))
            price = int(input("Enter price of the product: "))
            return name, item_number, price
        except ValueError:
            print("Error, please enter a valid number.")
            logging.error("wrong value for item_number.")

    @classmethod
    def menu(cls):
        """ """
        while True:
            cls.clear_screen()
            print(cls.show_logo())
            print(cls.show_menu())
            response = input("> ")

            if response in ["q", "exit", "quit"]:
                break

            elif response == Menu.add.value:
                name, item_number, price = Ui.add_product_ui()
                p = Product(name=name, item_number=item_number, price=price)
                p.add_product()
            elif response == Menu.show.value:
                Product.show_products()
            elif response == Menu.help.value:
                Product.show_help()
            elif response == Menu.remove.value:
                name = input("Enter product name to remove:")
                p = Product(name=name)
                p.remove_product()
            elif response == Menu.search.value:
                name = input("Enter product name to search:").lower()
                p = Product(name=name)
                p.search_product()
            elif response == Menu.clear.value:
                Ui.clear_screen()
            elif response == Menu.sort_asc.value:
                Product.sort_product_ascending()
            elif response == Menu.sort_dec.value:
                Product.sort_product_descending()
            else:
                print("Wrong choice!!")
                logging.info("user chooses wrong option", response)

            input("\nPress Enter key to continue ....")


def main():
    """ """
    if User.authorization():
        Ui.menu()
    else:
        print("Username or password is incorrect.")


main()
