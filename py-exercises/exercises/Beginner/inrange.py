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
Give x and n if x were in between 0 to n 
return true otherwise return false

Examples
-------
>>> in_range(2, 7)
True
>>> in_range(5, 3)
False


Requirements
------------
 - If stetement
 - Comparison Operators

Resources
---------
 - https://www.w3schools.com/python/python_conditions.asp 
 - https://www.w3schools.com/python/python_operators.asp
"""

def in_range(x, n):
    pass


# -----------------------------------
# Test area (Do not touch this area)
# -----------------------------------
if __name__ == "__main__":
    from tests import assert_equals

    assert_equals(in_range, (2, 10), True)
    assert_equals(in_range, (0, 3), True)
    assert_equals(in_range, (-1, -5), False)
    assert_equals(in_range, (4, 3), False)
    assert_equals(in_range, (0, 3), True)
    assert_equals(in_range, (-1, 3), False)
    assert_equals(in_range, (1, 3), True)
