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
Incerement the n by one

Examples
-------
>>> inc(2)
3
>>> inc(-1)
0
>>> area(0)
1

Requirements
------------
 - Variables
 - Arithmetic Operators
Resources
---------
 - https://www.w3schools.com/python/python_variables.asp
 - https://www.w3schools.com/python/python_operators.asp
"""
import tests


def inc(n):
    pass


if __name__ == "__main__":
    from tests import assert_equals

    assert_equals(inc, (1,), 2)
    assert_equals(inc, (0,), 1)
    assert_equals(inc, (-1,), 0)
