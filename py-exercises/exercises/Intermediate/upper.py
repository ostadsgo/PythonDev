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
Make the string upper case

Examples
-------
>>> upper("Hello World!") 
HELLO WORLD!


Requirements
------------
 - Strings

Resources
---------
 - https://www.w3schools.com/python/python_strings.asp
"""


def upper(s):
    pass


# -----------------------------------
#    Do not touch this section
# -----------------------------------
if __name__ == "__main__":
    from tests import assert_equals

    assert_equals(upper, ("This",), "THIS")
    assert_equals(upper, ("THIs",), "THIS")
    assert_equals(upper, ("123abc",), "123ABC")
    assert_equals(upper, ("t",), "T")
    assert_equals(upper, ("T",), "T")
    assert_equals(upper, ("",), "")
    assert_equals(upper, (" ",), " ")
    assert_equals(upper, ("tHis Is",), "THIS IS")
