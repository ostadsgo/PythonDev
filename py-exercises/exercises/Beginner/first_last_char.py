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
Return the first and last character of a string as a tuple
If the string was empty string return eimpty tuple `()`


Examples
-------
>>> first_last_char("hello")
(h, o)
>>> first_last_char("")
()


Requirements
------------
 - Strings

Resources
---------
 - https://www.w3schools.com/python/python_strings.asp
 - https://www.w3schools.com/python/python_strings_slicing.asp
"""


def first_last_cahr(s):
    pass


# -----------------------------------
#    Do not touch this section
# -----------------------------------
if __name__ == "__main__":
    from tests import assert_equals

    assert_equals(first_last_cahr, ("hello",), ("h", "o"))
    assert_equals(first_last_cahr, ("",), ())
    assert_equals(first_last_cahr, ("x",), ("x", "x"))
    assert_equals(first_last_cahr, ("hello world",), ("h", "d"))
