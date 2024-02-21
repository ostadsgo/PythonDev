"""
Information
-----------
@Copyright by Saeed Gholami 
Email: saeed.ghollami@gmail.com
Github: ostadsgo
Web: ostadsgo.github.io
Last edit: 2023-02-21


Level
-----
* Beginners
intermediate
Advanced


Description
-----------
Conver Kilometer to Mile
Return result rounded by 3 digits
If kilometer were negative or zero return 0

Examples
-------
>>> km_to_mile(1)
0.622
>>> km_to_mile(0)
0.0
>>> km_to_mile(-1)
0.0


Requirements
------------
 - Arithmetic operators

Resources
---------
 - https://www.w3schools.com/python/python_numbers.asp
 - https://www.w3schools.com/python/python_operators.asp

"""


def km_to_mile(km):
    if km <= 0:
        return 0.0
    return round(km / 1.609, 3)


# -----------------------------------
#    Do not touch this section
# -----------------------------------
if __name__ == "__main__":
    from tests import assert_equals

    assert_equals(km_to_mile, (1,), 0.622)
    assert_equals(km_to_mile, (5,), 3.108)
    assert_equals(km_to_mile, (0,), 0.0)
    assert_equals(km_to_mile, (-10,), 0.0)
