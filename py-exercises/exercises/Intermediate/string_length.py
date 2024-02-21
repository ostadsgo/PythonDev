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
Return the number of characters of a string.

Examples
-------
>>> length("Hello World!") 
12


Requirements
------------
 - Built-in functions
 - Strings

Resources
---------
 - https://www.w3schools.com/python/python_strings.asp
 - https://www.w3schools.com/python/python_ref_functions.asp
"""


def length(s):
    pass


# -----------------------------------
#    Do not touch this section
# -----------------------------------
if __name__ == "__main__":
    from tests import assert_equals

    assert_equals(length, ("This",), 4)
    assert_equals(length, ("123abc",), 6)
    assert_equals(length, ("t",), 1)
    assert_equals(length, ("",), 0)
    assert_equals(length, (" ",), 1)
    assert_equals(length, ("tHis Is",), 7)
