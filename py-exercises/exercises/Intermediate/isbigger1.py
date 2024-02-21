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
Compare two integers if x is bigger than y
return True otherwise return False

Examples
-------
>>> isbigger(2, 5)
True
>>> isbigger(5, 2)
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

def isbigger(x, y):
    pass

# -----------------------------------
if __name__ == "__main__":
    from tests import assert_equals

    assert_equals(isbigger, (2, 3), -1)
    assert_equals(isbigger, (0, 5), -1)
    assert_equals(isbigger, (-1, -5), -1)
    assert_equals(isbigger, (4, 0), 1)
    assert_equals(isbigger, (0, 0), 0)
