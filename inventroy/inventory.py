import os
import tomllib
import logging
from enum import Enum
from dataclasses import dataclass
from typing import Tuple


# basic config for log file.
logging.basicConfig(filename="inventory.log", encoding="utf-8", level=logging.DEBUG)


class Menu(Enum):
    """
    Menu options
    """

    ADD = "add"
    SHOW = "show"
    HELP = "help"
    REMOVE = "remove"
    SEARCH = "search"
    CLEAR = "clear"
    SORT_ASC = "sort asc"
    SORT_DEC = "sort dec"


@dataclass
class ProductFile:
    """
    File operations for Product class
    filename must be provided to create a file.
    """

    filename: str

    def append(self, line: str) -> bool:
        """
        recive a line of text and append it to the end of the file.

        Parameters
        ----------
        line: str
            text to write to the file.

        Returns
        -------
        out: bool
            Return True if write operation was successful otherwise False

        """
        try:
            with open(self.filename, "a") as file:
                file.write(line)
                return True
        except FileExistsError as e:
            logging.error(str(e))
        except Exception as e:
            logging.error(str(e))
        return False

    def write(self, lines: list[str]):
        """
        Iterate over line of text and write them to the file.

        Parameters
        ----------
        lines: list[str]
            List of lines each line is just a normal text

        Returns
        -------
        out: bool
            Return True if write operation was successful otherwise False
        """
        try:
            with open(self.filename, "w") as file:
                file.write(lines)
                return True
        except FileExistsError as e:
            logging.error(str(e))
        except Exception as e:
            logging.error(str(e))
        return False

    def read(self):
        """
        Read content of the filename and return them as list of text

        Returns
        -------
        out: bool
            Return list of string if able to read filename's content otherwise return empty list
        """
        try:
            with open(self.filename) as file:
                content: list[str] = file.read().strip().split("\n")
                return content
        except FileNotFoundError:
            logging.error("The file inventory.txt is not exit")
            logging.error("Create inventory.txt for the first time.")
            self.write([""])


@dataclass
class Product:
    """
    Represent a product.
    A product consist of name, number and price
    Name of the product to create a product is required.
    """

    def __init__(self, name: str, number=0, price=0):
        self.name = name
        self.number = number
        self.price = price
        self.total_price = self.number * self.price
        self.productfile = ProductFile("inventory.txt")

    def calc_total_price(self) -> int:
        """
        Calculate total price of the product

        Returns
        -------
        out: int
            Return totoal price of the product.
        """
        self.total_price = self.price * self.number
        return self.total_price

    def save(self) -> bool:
        """
        Save the product in the file. Take log if there was exceptions.

        Returns
        -------
        out: bool
            Return True if product save successfully otherwise False.

        """
        line = f"{self.name},{self.number},{self.price},{self.calc_total_price()}\n"
        if self.productfile.append(line):
            return True
        return False

    def is_exist(self) -> int:
        """
        Check if product is already exist in the file or not

        Returns
        -------
        outs: int
            Retrun the index of the product if found otherwise -1
        """
        products: list[str] = self.productfile.read()
        for index, product in enumerate(products):
            name, *_ = product.split(",")
            if name == self.name:
                return index
        return -1

    def add(self) -> bool:
        """
        Check if product is not in the file add it.

        Returns
        -------
        out: bool
            Return True if file saved otherwise return False
        """
        if self.is_exist() >= 0:
            return False
        return True if self.save() else False

    def remove(self):
        """
        Remove a product if exist.

        Returns
        -------
        out: bool
            True if remove operation was successful otherwise False.
        """
        products: list[str] = self.productfile.read()
        index = self.is_exist()
        if index == -1:
            return False
        del products[index]
        self.productfile.write(products)
        return True

    def search(self) -> str:
        """
        Search product by name.

        Returns
        -------
        outs: str
            Return the product if found otherwise return empty seting
        """
        if self.is_exist() != -1:
            return f"{self.name} {self.number} {self.price} {self.total_price}"
        return ""

    @classmethod
    def sort_asc(cls):
        """
        Sort products ascending
        """
        products: list[str] = Product.read_products()
        sorted_products: list[Product] = sorted(products)
        cls.show(sorted_products)

    @classmethod
    def sort_dec():
        """Sort products descending"""
        products: list[str] = Product.read_products()
        sorted_products: list[Product] = sorted(products, reverse=True)
        Product.show(sorted_products)

    @staticmethod
    def show(products: list[str]):
        """
        Get list of products and print them in a table like format.

        Parameters
        ----------
        products: list[str]
            list of products each product is a string.
        """
        print(f"{'Product Name':20}{'Quantity':10}Price\tTotal Price")
        print("-" * 50)
        number = 0
        for product in products:
            name, number, price, total_price = product.split(",")
            print(f"{name:20}{number:10}${price}\t${total_price}")
            number += int(number)
        print(f"All items number are: {number}")

    @staticmethod
    def manual():
        """
        Display help on how to use the program
        """
        return """
        Copy right by Zahra Mohammadzadeh
        Last Edit: 2023/1/26
        An application to manage an inventory of the shop.
        Features:
        - User authorization.
        - Opetions like add, remove, search and show products.
        Press `q` or `exit` to exit out of the program.
        """


@dataclass
class User:
    """
    Authorized user management
    """

    username: str
    password: str

    def read_config(self):
        """ """
        with open("config.toml", "rb") as toml_file:
            config = tomllib.load(toml_file)
        return config

    def admin_credentials(self) -> Tuple[str, str]:
        """
        Extract admin username and admin password

        Returns
        -------
        outs: str, str
            Return admin username and password.
        """
        config = self.read_config()
        username = config.get("username")
        passwd = config.get("password")
        return username, passwd

    def check_passwd(self) -> bool:
        """
        Compare username and password with the admin credentials

        Retruns:
        --------
        outs: bool
            True if user reponse credentials was correct otherwise False
        """
        admin_username, admin_passwd = self.admin_credentials()

        if self.username == admin_username and self.password == admin_passwd:
            return True
        return False

    def authorization(self) -> bool:
        """
        Authorize user for 3 times

        Returns
        -------
        outs: bool
            Return True if user credentials was correct otherwiese False
        """
        for _ in range(3):
            if self.check_passwd():
                return True
            return False


class Ui:
    """
    User interfece that user will interact.
    """

    @staticmethod
    def clear_screen():
        """Clear console screen."""
        os.system("cls")

    @staticmethod
    def show_logo():
        return """
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
                p = Product(name=name, number=item_number, price=price)
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


if __name__ == "__main__":
    main()
