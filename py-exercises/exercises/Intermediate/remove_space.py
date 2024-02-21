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
Remove space from the sting.

Examples
-------
>>> remove_space("Hello World!", "HelloWorld!") 
HelloWorld!


Requirements
------------
 - Strings

Resources
---------
 - https://www.w3schools.com/python/python_strings.asp
"""


def remove_space(s1):
    pass


# -----------------------------------
#    Do not touch this section
# -----------------------------------
if __name__ == "__main__":
    from tests import assert_equals

    assert_equals(remove_space, ("This",), "This")
    assert_equals(remove_space, ("Someth ing",), "Something")
    assert_equals(remove_space, ("",), "")
    assert_equals(remove_space, ("this a string",), "thisastring")
    assert_equals(remove_space, ("this is",), "thisis")
