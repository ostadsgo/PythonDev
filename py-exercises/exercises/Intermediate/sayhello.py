"""
Information
-----------
@Copyright by Saeed Gholami 
Email: saeed.ghollami@gmail.com
Github: ostadsgo
Web: ostadsgo.github.io
Last edit: 2023-02-04


Level
-----
* Beginners
intermediate
Advanced


Description
-----------
Say hello to given a name.

Examples
-------
>>> say_hello("John")
Hello, John


Requirements
------------
 - Strings

Resources
---------
 - https://www.w3schools.com/python/python_strings.asp 
"""


def say_hello(name):
    pass


# -----------------------------------
#    Do not touch this section
# -----------------------------------
if __name__ == "__main__":
    from tests import assert_equals

    assert_equals(say_hello, ("john",), "Hello, john")
    assert_equals(say_hello, ("",), "Hello, ")
    assert_equals(say_hello, ("0",), "Hello, 0")
    assert_equals(say_hello, ("John",), "Hello, John")
