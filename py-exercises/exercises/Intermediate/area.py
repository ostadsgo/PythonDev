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
Calculate area of a rectangle
if with or height were less than or equal zero return 0

Examples
-------
>>> area(2, 3)
6
>>> area(0, 1)
0
>>> area(-1, 2)
0


Requirements
------------
 - If statement
 - Comparison Operators

Resources
---------
 - https://www.w3schools.com/python/python_conditions.asp
 - https://www.w3schools.com/python/python_operators.asp
"""

def area(w, h):
    if w <= 0 or h <= 0:
        return 0
    return w * h
# -----------------------------------
#    Do not touch this section
# -----------------------------------
if __name__ == "__main__":
    from tests import assert_equals

    assert_equals(area, (2, 3), 6)
    assert_equals(area, (0, 0), 0)
    assert_equals(area, (-1, 3), 0)
    assert_equals(area, (-1, -1), 0)
    assert_equals(area, (2, -1), 0)
