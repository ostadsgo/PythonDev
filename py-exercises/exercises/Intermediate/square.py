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
Calculate square of a number

Examples
-------
>>> square(4)

Requirements
------------
 - Arithmetic Operators

Resources
---------
 - https://www.w3schools.com/python/python_operators.asp
"""


def square(n):
    return n * n


# -----------------------------------
#    Do not touch this section
# -----------------------------------
if __name__ == "__main__":
    from tests import assert_equals

    assert_equals(square, (2,), 4)
    assert_equals(square, (4,), 16)
    assert_equals(square, (0,), 0)
    assert_equals(square, (-5,), 25)
