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
Make the string lower case

Examples
-------
>>> upper("Hello World!") 
hello world!


Requirements
------------
 - Strings

Resources
---------
 - https://www.w3schools.com/python/python_strings.asp
"""


def lower(s):
    pass


# -----------------------------------
#    Do not touch this section
# -----------------------------------
if __name__ == "__main__":
    from tests import assert_equals

    assert_equals(lower, ("This",), "this")
    assert_equals(lower, ("THIs",), "this")
    assert_equals(lower, ("123abc",), "123abc")
    assert_equals(lower, ("t",), "t")
    assert_equals(lower, ("T",), "t")
    assert_equals(lower, ("",), "")
    assert_equals(lower, (" ",), " ")
    assert_equals(lower, ("tHis Is",), "this is")
